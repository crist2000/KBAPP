
if __name__ == '__main__':
    print("Not runnable file. Run main.py instead")
else:

    def formatStr(lst: list) -> str:
        str_res = "".join(lst)
        return str_res.replace("'", "").replace(")", "")

    class kbData:
        __clt = []
        __prd = []
        __err = []
        __cse = []
        __fix =  []

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
                    a, b, c, d, e, f = str(row).split(", ")
                    self.__clt.append(b + "\n")
                    self.__prd.append(c + "\n")
                    self.__err.append(d + "\n")
                    self.__cse.append(e + "\n")
                    self.__fix.append(f + "\n")

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

                print("SQL raw data was not recognized. Data parsing failed.")
