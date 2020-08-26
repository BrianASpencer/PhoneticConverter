import tkinter as tk
import pyautogui
from tkinter import Text


d = {
    "a": "Alpha",
    "b": "Bravo",
    "c": 'Charlie',
    "d": "Delta",
    "e": "Echo",
    "f": "Foxtrot",
    "g": "Golf",
    "h": "Hotel",
    "i": "India",
    "j": "Juliett",
    "k": "Kilo",
    "l": "Lima",
    "m": "Mike",
    "n": "November",
    "o": "Oscar",
    "p": "Papa",
    "q": "Quebec",
    "r": "Romeo",
    "s": "Sierra",
    "t": "Tango",
    "u": "Uniform",
    'v': "Victor",
    'w': "Whiskey",
    "x": "X-ray",
    "y": "Yankee",
    "z": "Zulu"
}

root = tk.Tk()
# dimensions
width, height = pyautogui.size()
widthStr = str(width//3)
heightStr = str(height//12)
resolution = widthStr + "x" + heightStr
root.geometry(resolution)

textBox = tk.Text(root, height=5, width=width//30)
textBox.grid(row=1, column=0)


def clearText():
    textBox.delete(1.0, "end")


def setText(s):
    textBox.insert(1.0, s)


def readText(string):

    string = string.lower()

    out = ""

    for i in string:
        if i in d:
            out = out + d[i] + " "
    setText(out)


def processText():
    result = textBox.get(1.0, tk.END+"-1c")
    clearText()
    readText(result)

#buttons in new column
btnConv = tk.Button(root,
                    height=1,
                    width=10,
                    text="Convert",
                    command=lambda: processText())
btnConv.grid(row=1, column=1)

btnClear = tk.Button(root,
                     height=1,
                     width=10,
                     text="Clear",
                     command=lambda: clearText())
btnClear.grid(row=1, column=2)

root.mainloop()
