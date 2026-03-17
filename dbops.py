import pyodbc as dba
from fileops import fileExists

ACCDB = "accdb"
MSSQL = "mssql"

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:

    class dBops:
        cnx = None
        dsn = None
        cursor = None

        def __getdsn(self, dbtype):
            myDSN = dba.dataSources()

            if dbtype == ACCDB:
                return myDSN['MS Access Database']
            elif dbtype == MSSQL:
                return None
            else:
                return None

        def closeConnection(self):
            if self.cnx is not None:
                print("Closing database connection")
                self.cursor.close()
                self.cnx.close()

        def __init__(self, dbtype, filepath):

            if not fileExists(filepath):
                return

            self.dsn = self.__getdsn(dbtype)

            if self.dsn is not None:
                print(self.dsn)
                self.cnx = dba.connect(driver=self.dsn, dbq=filepath)
                self.cursor = self.cnx.cursor()
            else:
                print("Unsupported database type")
                return

        def executeSelect(self, query):
            try:
                if self.cursor is None:
                    print("Cursor is null. Query execution aborted")
                    return []
                else:
                    self.cursor.execute(query)

                    sql_result = []
                    for row in self.cursor.fetchall():
                        sql_result.append(row)

                    return sql_result

            except:
                print(f"{query} run failed. Check SQL statement")

        def executeInsert(self, query):
            try:
                if self.cursor is None:
                    print("Cursor is null. Query execution aborted")
                else:
                    self.cursor.execute(query)
                    self.cnx.commit()

            except:
                print(f"{query} run failed. Check SQL statement")

        #to be used with the 'with' statement.
        def __enter__(self):
            return self

        def __exit__(self, exception_type, exception_value, exception_traceback):
            self.closeConnection()

