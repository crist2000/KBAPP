# Create Main window

from dbops import *
from .kbdata import *
from .actions import *
from .WindowParam import *
from .InsertForm import createWindow
from .mainconst import *

#to transfer widget objects between functions
lab_entry_list = []
lab_res_list = []


def doClear():
    clearAll(lab_res_list)
    clearAll(lab_entry_list)

def doSubmit():
    sql = makeSelectSql(*lab_entry_list)

    with dBops(ACCDB, db_filepath) as dbo:
        raw_data = kbData(dbo.executeSelect(sql))
        lab_res_list[ColIdx.clt.value].setTxt(raw_data.client)
        lab_res_list[ColIdx.prd.value].setTxt(raw_data.prod)
        lab_res_list[ColIdx.err.value].setTxt(raw_data.error)
        lab_res_list[ColIdx.cse.value].setTxt(raw_data.cause)
        lab_res_list[ColIdx.fix.value].setTxt(raw_data.fix)

def createWindowInsert():
    createWindow(window_param_insert)

#make main window
btn_actions_main = {"Submit": doSubmit, "Clear": doClear, "Insert": createWindowInsert}
labels_main = ["CLIENT", "PRODUCT", "ERROR"]
window_param_main = WindowParam(main_window_size, "Knowledge Base", bg_color, True)
window_param_insert = WindowParam(sub_window_size, "Insert Data", bg_color, False)

def makeMainForm():
    main_form = make_window(window_param_main)

    #GUI control elements
    startY = LeftUpPos["Y"]
    startX = LeftUpPos["X"]

    make_labels(main_form, labels_main, startX, startY, LabelOffset["X"], LabelOffset["Y"])
    make_buttons(main_form, btn_actions_main, UpMidPos["X"], UpMidPos["Y"] + label_alignY, BtnOffset["X"], BtnOffset["Y"])

    entry_clt = Entry(main_form, startX + EntryOffset["X"], startY + label_alignY)
    entry_prd = Entry(main_form, startX + EntryOffset["X"], startY + EntryOffset["Y"] + label_alignY)
    entry_err = Entry(main_form, startX + EntryOffset["X"], startY + 2 * EntryOffset["Y"] + label_alignY)
    lab_entry_list.append(entry_clt)
    lab_entry_list.append(entry_prd)
    lab_entry_list.append(entry_err)

#SQL result
    resX = LefMidPos["X"]
    resY = LefMidPos["Y"]

    lab_res_clt = Label(main_form, "", bg_color, resX, resY, label_font_result)
    lab_res_prd = Label(main_form, "", bg_color, resX + WidgetSize["Short"], resY, label_font_result)
    lab_res_err = Label(main_form, "", bg_color, resX + WidgetSize["Mid"], resY, label_font_result)
    lab_res_cse = Label(main_form, "", bg_color, resX + WidgetSize["Mid"] + WidgetSize["Long"], resY, label_font_result)
    lab_res_fix = Label(main_form, "", bg_color, resX + WidgetSize["Mid"] + 2 * WidgetSize["Long"], resY, label_font_result)
    lab_res_list.append(lab_res_clt)
    lab_res_list.append(lab_res_prd)
    lab_res_list.append(lab_res_err)
    lab_res_list.append(lab_res_cse)
    lab_res_list.append(lab_res_fix)

    main_form.mainloop()
