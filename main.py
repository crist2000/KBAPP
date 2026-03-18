from gui.mainform import makeMainForm
from fileops import *

print("Make sure that python.exe and ODBC driver share the same architecture type")
print(f"Your python.exe is {GetPythonArchType()} bit")

makeMainForm()