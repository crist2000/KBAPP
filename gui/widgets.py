#Decorator classes for Tkinker widgets.

import tkinter as tk

from gui.mainconst import WidgetSize

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

        def __init__(self, window: object, x: int, y: int, size = WidgetSize["Short"]): #, font: tuple
            self.entry = tk.Entry(window)
            self.entry.config(width=10, justify="left")
            self.entry.place(x=x, y=y, width=size)

        def getText(self):
            return self.entry.get()

        def clear(self):
            self.entry.delete(0, 'end')

    class Text:
        text = None
        count = 0

        def char_count(self, dummy: str):
            str_cur = self.getText()
            strlen = len(str_cur)

        def __init__(self, window: object, bgcolor: str, x: int, y: int, font: tuple):
            self.text = tk.Text(window, height= 25, width= 180, font= font, bg= bgcolor, bd= 0)
            self.text.configure(state='normal')
            self.text.place(x=x, y=y)
            #self.text.bind('<KeyPress>', self.char_count)
            #self.text.bind('<KeyRelease>', self.char_count)

        def getText(self):
            return self.text.get("1.0", tk.END)

        def setText(self, txt: str):
            self.text.insert(tk.END, txt)

        def clear(self):
            self.text.delete("1.0", 'end')

        def bingkey(self, key : str, action: callable):
            self.text.bind(key, action)