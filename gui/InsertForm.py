import widgets as gui
import actions as do
from dbops import *
from mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:
    values_insert = []

    def clearAll():
        do.clearAll(values_insert)

    def doInsert():
        sql = do.makeInsertSql(*values_insert)
        with dBops(ACCDB, db_filepath) as dbo:
            dbo.executeInsert(sql)

    btn_actions_insert = {"Insert": doInsert, "Clear": clearAll}
    labels_insert = ["CLIENT", "PRODUCT", "ERROR", "CAUSE", "SOLUTION"]

    def createWindow(window_param):
        sub_form = do.make_main(window_param)

        do.make_buttons(sub_form, btn_actions_insert, 200, 20, 100, 0)
        do.make_labels(sub_form, labels_insert, 10, 10, 0, 30)

        entry_clt = gui.Entry(sub_form, 90, 20)
        entry_prd = gui.Entry(sub_form, 90, 50)
        entry_err = gui.Entry(sub_form, 90, 80)
        entry_cse = gui.Entry(sub_form, 90, 110)
        entry_fix = gui.Entry(sub_form, 90, 140)
        values_insert.append(entry_clt)
        values_insert.append(entry_prd)
        values_insert.append(entry_err)
        values_insert.append(entry_cse)
        values_insert.append(entry_fix)