#Operations with GUi

import tkinter as tk
import widgets as gui
from mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:

    sql_select_base = "select * from TesterErrors"
    sql_insert_base = "insert into TesterErrors"

    def clearAll(input:list):
        err = None
        try:
            for item in input:
                err = item
                item.clear()
        except:
            print(f"Item{err} has no clear method")

    def makeSql(entryClnt, entryErr):
        cl = entryClnt.getText()
        err = entryErr.getText()

        if cl == '' and err == '':
            sql = sql_select_base
        elif cl != '' and err == '':
            sql = f"{sql_select_base} where Client like '%{cl}%'"
        elif cl == '' and err != '':
            sql = f"{sql_select_base} where Error like '%{err}%'"
        else:
            sql = f"{sql_select_base} where Client like '%{cl}%' and Error like '%{err}%'"

        print("Executing SQL: " + sql)
        return sql

    def makeInsertSql(entryClnt, entryPrd, entryErr, entryCse, entryFix):
        clt = entryClnt.getText()
        prd = entryPrd.getText()
        err = entryErr.getText()
        cse = entryCse.getText()
        fix = entryFix.getText()

        sql = f"{sql_insert_base}(Client, Product, Error, Cause, Solution) values('{clt}', '{prd}', '{err}', '{cse}', '{fix}')"

        print("Executing SQL: " + sql)
        return sql

    def make_main(window_param):  # size:str, title:str, color:str, resizable = True
        form = tk.Tk()
        form.geometry(window_param.size)
        form.title(window_param.title)
        form.configure(background=window_param.color)
        form.resizable(window_param.resizable, window_param.resizable)
        return form

    def make_sub(window_param):
        top = tk.Toplevel()
        top.title(window_param.title)
        top.geometry(window_param.size)
        top.configure(background=window_param.color)
        top.resizable(window_param.resizable, window_param.resizable)
        return top

    def make_buttons(form, button_dict, startX, startY, offsetX, offsetY):
        x = startX
        y = startY

        for key, value in button_dict.items():
            gui.Button(form, key, bg_color, x, y, value)
            x += offsetX
            y += offsetY

    def make_labels(form, label_list, startX, startY, offsetX, offsetY):
        x = startX
        y = startY

        for value in label_list:
            gui.Label(form, value, bg_color, x, y, label_font)
            x += offsetX
            y += offsetY

