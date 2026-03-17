import tkinter as tk
from mainconst import *

if __name__ == '__main__':
    print("Not runnable file. Run main.py instead")
else:

    def make_main(window_param):  # size:str, title:str, color:str, resizable = True
        form = tk.Tk()
        form.geometry(window_param.size)
        form.title(window_param.title)
        form.configure(background=window_param.color)
        form.resizable(window_param.resizable, window_param.resizable)
        return form

    def make_sub(window_param):
        top = tk.Toplevel()
        top.title(window_param.title)
        top.geometry(window_param.size)
        top.configure(background=window_param.color)
        top.resizable(window_param.resizable, window_param.resizable)
        return top

    def make_buttons(form, button_dict, startX, startY, offsetX, offsetY):
        x = startX
        y = startY

        for key, value in button_dict.items():
            Button(form, key, bg_color, x, y, value)
            x += offsetX
            y += offsetY

    def make_labels(form, lable_list, startX, startY, offsetX, offsetY):
        x = startX
        y = startY

        for value in lable_list:
            Label(form, value, bg_color, x, y, label_font)
            x += offsetX
            y += offsetY




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