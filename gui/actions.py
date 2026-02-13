from mainconst import *

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
        sql = main_sql
    elif cl != '' and err == '':
        sql = f"{main_sql} where Client like '%{cl}%'"
    elif cl == '' and err != '':
        sql = f"{main_sql} where Error like '%{err}%'"
    else:
        sql = f"{main_sql} where Client like '%{cl}%' and Error like '%{err}%'"

    print("Executing SQL: " + sql)
    return sql