import os
import struct

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:

    def fileExists(filepath):
        if os.path.exists(filepath):
            return True
        else:
            print(f"File {filepath} does not exist")
            return False

    def GetPythonArchType():
        type = struct.calcsize("P") * 8
        print (type)

        return type