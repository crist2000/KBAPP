#INSERT sub window

from .actions import *
from dbops import *
from .mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:
    values_insert = [] #to transfer entry objects between functions
    startY = LeftUpPos["Y"]
    startX = LeftUpPos["X"]

    def doClear():
        clearAll(values_insert)

    def doInsert():
        try:
            sql = makeInsertSql(*values_insert)

            with dBops(ACCDB, db_filepath) as dbo:
                dbo.executeInsert(sql)
        except:
            print(f"{APP}Data for makeSQL is invalid. Buffer list contains {len(values_insert)} items. Expected 5.")


    btn_actions_insert = {"Insert": doInsert, "Clear": doClear}
    labels_insert = ["CLIENT", "PRODUCT", "ERROR", "CAUSE", "SOLUTION"]

    def createWindow(window_param):
        values_insert.clear()
        sub_form = make_window(window_param, False)

        make_buttons(sub_form, btn_actions_insert, LefMidPos["X"], LefMidPos["Y"] + label_alignY, BtnOffset["X"], BtnOffset["Y"])
        make_labels(sub_form, labels_insert, LeftUpPos["X"], LeftUpPos["Y"], LabelOffset["X"], LabelOffset["Y"])

        entry_clt = Entry(sub_form, startX + EntryOffset["X"], startY + label_alignY)
        entry_prd = Entry(sub_form, startX + EntryOffset["X"], startY + EntryOffset["Y"] + + label_alignY)
        entry_err = Entry(sub_form, startX + EntryOffset["X"], startY + 2 * EntryOffset["Y"] + label_alignY, WidgetSize["Long"])
        entry_cse = Entry(sub_form, startX + EntryOffset["X"], startY + 3 * EntryOffset["Y"] + label_alignY, WidgetSize["Long"])
        entry_fix = Entry(sub_form, startX + EntryOffset["X"], startY + 4 * EntryOffset["Y"] + label_alignY, WidgetSize["Long"])
        values_insert.append(entry_clt)
        values_insert.append(entry_prd)
        values_insert.append(entry_err)
        values_insert.append(entry_cse)
        values_insert.append(entry_fix)
