#SQL response parser
from .mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run main.py instead")
else:

    def formatStr(lst: list) -> str:
        str_res = "".join(lst)
        return str_res.replace("'", "").replace(")", "").replace("None", "")

    class kbData:
        __clt = []
        __prd = []
        __err = []
        __cse = []
        __fix = []

        def __clearKBdata(self):
            self.__clt = []
            self.__prd = []
            self.__err = []
            self.__cse = []
            self.__fix = []

        def __init__(self, sql_raw):
            self.__clearKBdata()

            try:
                for row in sql_raw:
                    resp = row[1:] #filter out row ID
                    self.__clt.append(str(resp[ColIdx.clt.value]) + "\n")
                    self.__prd.append(str(resp[ColIdx.prd.value]) + "\n")
                    self.__err.append(str(resp[ColIdx.err.value]) + "\n")
                    self.__cse.append(str(resp[ColIdx.cse.value]) + "\n")
                    self.__fix.append(str(resp[ColIdx.fix.value]) + "\n")

                self.client = formatStr(self.__clt)
                self.prod = formatStr(self.__prd)
                self.error = formatStr(self.__err)
                self.cause = formatStr(self.__cse)
                self.fix = formatStr(self.__fix)
            except:
                 self.client = ""
                 self.prod = ""
                 self.error = ""
                 self.cause = ""
                 self.fix = ""

                 print(f"{APP}SQL raw data was not recognized. Data parsing failed.")
