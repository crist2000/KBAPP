#from dbops import *
#import serial.tools.list_ports
import pyodbc as dba

sql_all = r"select * from TesterErrors"
sql_all1 = "select * from TesterErrors where Error like '%TBD%'"

sql_client = r"select Client from TesterErrors"
filepath = r"C:\Work\KnowledgeBase.accdb"



#ports = serial.tools.list_ports.comports()

#for port, desc, hwid in sorted(ports):
#        print("{}: {} [{}]".format(port, desc, hwid))

#sql_result = []
#sql_result.append("Client1,Product1,Error1")
#sql_result.append("Client2,Product2,Error2")

#client = []

# for row in sql_result:
#     a,b,c = row.split(",")
#     client.append(a+"\n")
#
# print("".join(client))


dsn = dba.dataSources()

for key, value in dsn.items():
    print(key + ": " + value)

# with dBops(ACCDB, filepath) as dbo:
#    res = dbo.executeQuery(sql_all1)
#    for row in res:
#        s = str(row)
#        a, b, c, d, e, f, g = s.split(", ")
#        print(b, c, d, e)
#        print(row)