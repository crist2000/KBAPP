# Create Main window

from mainconst import *
from dbops import *
from kbdata import *
import widgets as gui
import actions as do
from WindowParam import *
from InsertForm import createWindow

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

window_param_main = WindowParam(main_window_size, "Knowledge Base", bg_color, True)
window_param_insert = WindowParam(sub_window_size, "Insert Data", bg_color, False)

main_form = do.make_main(window_param_main)

#GUI control elements
startY = LeftUpPos["Y"]
startX = LeftUpPos["X"]

do.make_labels(main_form, labels_main, startX, LeftUpPos["Y"], LabelOffset["X"], LabelOffset["Y"])
do.make_buttons(main_form, btn_actions_main, UpMidPos["X"], UpMidPos["Y"] + label_alignY, BtnOffset["X"], BtnOffset["Y"])

entry_clt = gui.Entry(main_form, startX + EntryOffset["X"], LeftUpPos["Y"] + label_alignY)
entry_err = gui.Entry(main_form, startX + EntryOffset["X"], LeftUpPos["Y"] + EntryOffset["Y"] + label_alignY)
lab_entry_list = [entry_clt, entry_err]

#SQL result
x = LefMidPos["X"]
y = LefMidPos["Y"]

lab_res_clt = gui.Label(main_form, "", bg_color, x, y, label_font_result)
lab_res_prd = gui.Label(main_form, "", bg_color, x + WidgetSize["Short"], y, label_font_result)
lab_res_err = gui.Label(main_form, "", bg_color, x + WidgetSize["Mid"], y, label_font_result)
lab_res_cse = gui.Label(main_form, "", bg_color, x + WidgetSize["Mid"] + WidgetSize["Long"], y, label_font_result)
lab_res_fix = gui.Label(main_form, "", bg_color, x + WidgetSize["Mid"] + 2 * WidgetSize["Long"], y, label_font_result)
lab_res_list = [lab_res_clt, lab_res_prd, lab_res_err, lab_res_cse, lab_res_fix]

main_form.mainloop()
