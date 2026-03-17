from gui.actions import *
from mainconst import *
from dbops import *
from kbdata import *
import widgets as gui
import actions as do
from WindowParam import *
from InsertForm import createWindow

startY = 10
startX = 10
offsetY = 30
resultX = 100

def clearAll():
    do.clearAll(lab_res_list)
    do.clearAll(lab_entry_list)

def doSubmit():
    sql = do.makeSql(entry_clt, entry_err)
    doSql(sql)

def doSql(sql_all):
    with dBops(ACCDB, db_filepath) as dbo:
        raw_data = kbData(dbo.executeSelect(sql_all))

        lab_res_clt.setTxt(raw_data.client)
        lab_res_prd.setTxt(raw_data.prod)
        lab_res_err.setTxt(raw_data.error)
        lab_res_cse.setTxt(raw_data.cause)
        lab_res_fix.setTxt(raw_data.fix)

def createWindowInsert():
    createWindow(window_param_insert)

#make main window
btn_actions_main = {"Submit": doSubmit, "Clear": clearAll, "Insert": createWindowInsert}
labels_main = ["CLIENT", "ERROR"]

window_param_main = WindowParam(main_window_size, "Knowledge Base", bg_color, False)
window_param_insert = WindowParam(sub_window_size, "Insert Data", bg_color, False)

main_form = do.make_main(window_param_main)

#GUI control elements
do.make_labels(main_form, labels_main, 10, 10, 0, 30)
do.make_buttons(main_form, btn_actions_main, 200, 40, 100, 0)

entry_clt = gui.Entry(main_form, 90, 20)
entry_err = gui.Entry(main_form, 90, 50)
lab_entry_list = [entry_clt, entry_err]

#SQL result
lab_res_clt = gui.Label(main_form, "", bg_color, 10, resultX, label_font_result)
lab_res_prd = gui.Label(main_form, "", bg_color, 70, resultX, label_font_result)
lab_res_err = gui.Label(main_form, "", bg_color, 150, resultX, label_font_result)
lab_res_cse = gui.Label(main_form, "", bg_color, 450, resultX, label_font_result)
lab_res_fix = gui.Label(main_form, "", bg_color, 750, resultX, label_font_result)
lab_res_list = [lab_res_clt, lab_res_prd, lab_res_err, lab_res_cse, lab_res_fix]

main_form.mainloop()
