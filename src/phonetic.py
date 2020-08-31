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

root.title("Phonetic Converter")

label = tk.Label(text="Enter text to convert: ")
label.grid(row=1, column=0, sticky="W")

# dimensions
root.geometry("790x115")

textBox = tk.Text(root, font="Helvetica 12", height=5, width=78)
textBox.grid(row=2, column=0)


def clearText():
    textBox.delete(1.0, "end")


def setText(string):
    textBox.tag_configure("bold", font="Helvetica 14 bold")
    for i in range(len(string)-1, -1, -1):
        if i == 0:
            textBox.insert(1.0, string[i], "bold")
        else:
            if string[i-1] == " ":
                textBox.insert(1.0, string[i], "bold")
            else:
                textBox.insert(1.0, string[i])


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
btnConv.grid(row=2, column=1, sticky="N")

btnClear = tk.Button(root,
                     height=1,
                     width=10,
                     text="Clear",
                     command=lambda: clearText())
btnClear.grid(row=2, column=1)



root.mainloop()
