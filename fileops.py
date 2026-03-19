import os, pyodbc, struct
from gui.mainconst import APP

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:

    def fileExists(filepath):
        if os.path.exists(filepath):
            return True
        else:
            print(f"{APP}File {filepath} does not exist")
            return False

    def GetPythonPlatform():
        type = struct.calcsize("P") * 8
        return type

    def CheckCompatibility():
        dsn_count = len(pyodbc.dataSources())
        if dsn_count == 0:
            print(f"{APP}Python.exe platform type is not compatible with available DSNs")
            print(f"{APP}Your python.exe is {GetPythonPlatform()} bit")
            return False
        else:
            print(f"{APP}Starting program....")
            return True