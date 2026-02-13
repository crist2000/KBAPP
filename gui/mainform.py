from mainconst import *
from dbops import *
from kbdata import *
import widgets as gui
import actions as do

startY = 10
startX = 10
offsetY = 30
resultX = 100

def clearAll():
    do.clearAll(lab_res_list)
    do.clearAll(lab_entry_list)

def doSql(sql_all):
    with dBops(ACCDB, db_filepath) as dbo:
        raw_data = kbData(dbo.executeQuery(sql_all))

        lab_res_clt.setTxt(raw_data.client)
        lab_res_prd.setTxt(raw_data.prod)
        lab_res_err.setTxt(raw_data.error)
        lab_res_cse.setTxt(raw_data.cause)
        lab_res_fix.setTxt(raw_data.fix)

def doSubmit():
    sql = do.makeSql(entry_clt, entry_err)
    doSql(sql)

#make main window
main_form = gui.make_main(main_window_size, "Knowledge Base", bg_color, False)

#GUI control elements
gui.Label(main_form, "CLIENT", bg_color, startX, startY, label_font)
gui.Label(main_form, "ERROR", bg_color, 100, startY, label_font)

entry_clt = gui.Entry(main_form, startX, startY + offsetY)
entry_err = gui.Entry(main_form, 100, startY + offsetY)
lab_entry_list = [entry_clt, entry_err]

gui.Button(main_form, "Submit", bg_color, 200, startY + offsetY, doSubmit)
gui.Button(main_form, "Clear", bg_color, 300, startY + offsetY, clearAll)
gui.Button(main_form, "New", bg_color, 400, startY + offsetY, clearAll)

#SQL result
lab_res_clt = gui.Label(main_form, "", bg_color, 10, resultX, label_font_result)
lab_res_prd = gui.Label(main_form, "", bg_color, 70, resultX, label_font_result)
lab_res_err = gui.Label(main_form, "", bg_color, 150, resultX, label_font_result)
lab_res_cse = gui.Label(main_form, "", bg_color, 450, resultX, label_font_result)
lab_res_fix = gui.Label(main_form, "", bg_color, 750, resultX, label_font_result)
lab_res_list = [lab_res_clt, lab_res_prd, lab_res_err, lab_res_cse, lab_res_fix]

main_form.mainloop()
