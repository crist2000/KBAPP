from gui.mainform import makeMainForm
from fileops import *

#Make sure that python.exe and ODBC driver share the same platform type
if CheckCompatibility():
    makeMainForm()

