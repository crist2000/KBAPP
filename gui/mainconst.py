from enum import Enum

db_filepath = r".\KnowledgeBase.accdb"
#db_filepath = r"C:\Work\KnowledgeBase.accdb"
bg_color = "#c2ccc6"
label_font = ("Arial", 10)
label_font_result = ("Arial", 9, "bold")
main_window_size = "1300x600"
sub_window_size = "500x300"

class ColIdx(Enum):
    clt = 0
    prd = 1
    err = 2
    cse = 3
    fix = 4

#GUI coordinate system
label_alignY = 10  #In Tkinker label looks misplaced vs other widgets

LeftUpPos = {"X": 10, "Y": 10}
LefMidPos = {"X": 10, "Y": 200}
UpMidPos = {"X": 200, "Y": 10}

LabelOffset = {"X": 0, "Y": 30}
EntryOffset = {"X": 80, "Y": 30}
BtnOffset = {"X": 90, "Y": 0}

WidgetSize = {"Short": 70, "Mid": 150, "Long": 320}

#Print formatting
TAB = "    "
APP = "KBAPP>"