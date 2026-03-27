#SQL response parser
from .mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run main.py instead")
else:

    def formatStr(lst: list) -> str:
        str_res = "".join(lst)
        return str_res.replace("'", "").replace(")", "").replace("None", "")

    class kbData:
        clt = []
        prd = []
        err = []
        cse = []
        fix = []

        def __clearKBdata(self):
            self.clt = []
            self.prd = []
            self.err = []
            self.cse = []
            self.fix = []

        def __init__(self, sql_raw):
            self.__clearKBdata()

            try:
                for row in sql_raw:
                    resp = row[1:] #filter out row ID
                    self.clt.append(str(resp[ColIdx.clt.value]))
                    self.prd.append(str(resp[ColIdx.prd.value]))
                    self.err.append(str(resp[ColIdx.err.value]))
                    self.cse.append(str(resp[ColIdx.cse.value]))
                    self.fix.append(str(resp[ColIdx.fix.value]))

            except:
                 self.clt = ""
                 self.prd = ""
                 self.err = ""
                 self.cse = ""
                 self.fix = ""

                 print(f"{APP}SQL raw data was not recognized. Data parsing failed.")