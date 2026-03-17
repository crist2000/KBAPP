from tkinter import Toplevel
from mainconst import *
from mainconst import *

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