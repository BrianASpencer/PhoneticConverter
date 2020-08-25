import tkinter as tk

from tkinter import Text


root = tk.Tk()
root.geometry("800x480")

textBox = tk.Text(root, height=10)
textBox.pack()

def clearText():
    textBox.delete(1.0,"end")

def setText(s):
    textBox.insert(1.0, s)

def readText(string):
    d = {
        "a" : "Alpha" ,                                                                                                                                                       
        "b" : "Bravo" ,                                                                                                                                                       
        "c" : 'Charlie' ,                                                                                                                                                     
        "d" : "Delta" ,                                                                                                                                                       
        "e" : "Echo" ,                                                                                                                                                        
        "f" : "Foxtrot" ,                                                                                                                                                     
        "g" : "Golf" ,                                                                                                                                                        
        "h" : "Hotel" ,                                                                                                                                                       
        "i" : "India" ,                                                                                                                                                       
        "j" : "Juliett" ,                                                                                                                                                     
        "k" : "Kilo" ,                                                                                                                                                        
        "l" : "Lima" ,                                                                                                                                                        
        "m" : "Mike" ,                                                                                                                                                        
        "n" : "November" ,                                                                                                                                                    
        "o" : "Oscar" ,                                                                                                                                                       
        "p" : "Papa" ,                                                                                                                                                        
        "q" : "Quebec" ,                                                                                                                                                      
        "r" : "Romeo" ,                                                                                                                                                       
        "s" : "Sierra" ,                                                                                                                                                      
        "t" : "Tango" ,                                                                                                                                                       
        "u" : "Uniform" ,                                                                                                                                                     
        'v' : "Victor" ,                                                                                                                                                      
        'w' : "Whiskey" ,                                                                                                                                                     
        "x" : "X-ray" ,                                                                                                                                                       
        "y" : "Yankee" ,                                                                                                                                                      
        "z" : "Zulu"
    }
    
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

btnConv = tk.Button(root, 
                   height=1, 
                   width=10, 
                   text="Convert", 
                   command=lambda:processText())
btnConv.pack()

btnClear = tk.Button(root, 
                   height=1, 
                   width=10, 
                   text="Clear", 
                   command=lambda:clearText())
btnClear.pack()

root.mainloop()
