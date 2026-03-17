import tkinter as tk
from mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run mainform.py instead")
else:

    class Label:
        lable = None

        def __init__(self, window: object, text: str, bgcolor: str, x: int, y: int, font: tuple):
            self.lable = tk.Label(window, text= text, font= font, bg= bgcolor, justify="left", pady=10)
            self.lable.place(x=x, y=y)

        def clear(self):
            self.lable.config(text = "")

        def setTxt(self, txt: str):
            self.lable.config(text = txt)

    class Button:
        btn = None
        __width = 50
        __height = 25

        def __init__(self, window: object, text: str, bgcolor: str, x: int, y: int, cmd: callable):
            btn = tk.Button(window, text= text, bg= bgcolor)
            btn.config(activebackground= "green", command= cmd)
            btn.place(x=x, y=y, width = self.__width, height = self.__height)

    class Entry:
        entry = None

        def __init__(self, window: object, x: int, y: int): #, font: tuple
            self.entry = tk.Entry(window)
            self.entry.config(width=10, justify="left")
            self.entry.place(x=x, y=y)
            self.entry.place(x=x, y=y)

        def getText(self):
            return self.entry.get()

        def clear(self):
            self.entry.delete(0, 'end')