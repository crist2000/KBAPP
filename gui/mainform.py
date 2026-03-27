# Create Main window

from dbops import *
from .kbdata import *
from .actions import *
from .WindowParam import *
from .InsertForm import createWindow
from .mainconst import *

#to transfer widget objects between functions
lab_entry_list = []
lab_res_txt = []
main_form = None

def doClear():
    clearAll(lab_entry_list)
    clearAll(lab_res_txt)

def doSubmit():
    sql = makeSelectSql(*lab_entry_list)

    with dBops(ACCDB, db_filepath) as dbo:
        raw_data = kbData(dbo.executeSelect(sql))
        clearAll(lab_res_txt)

        for i in range(len(raw_data.clt)):
            res = f"{raw_data.clt[i]}   {raw_data.prd[i]}   <{raw_data.err[i]}> <{raw_data.cse[i]}> <{raw_data.fix[i]}>\n"
            lab_res_txt[0].setText(res)

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

    txt_ltn = Text(main_form, bg_color, 15, 200, font_result)
    lab_res_txt.append(txt_ltn)

    entry_clt = Entry(main_form, startX + EntryOffset["X"], startY + label_alignY)
    entry_prd = Entry(main_form, startX + EntryOffset["X"], startY + EntryOffset["Y"] + label_alignY)
    entry_err = Entry(main_form, startX + EntryOffset["X"], startY + 2 * EntryOffset["Y"] + label_alignY)
    lab_entry_list.append(entry_clt)
    lab_entry_list.append(entry_prd)
    lab_entry_list.append(entry_err)

    main_form.mainloop()
