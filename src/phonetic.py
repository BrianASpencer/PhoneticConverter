import tkinter as tk

from tkinter import Text


root = tk.Tk()
root.geometry("400x240")

textExample = tk.Text(root, height=10)
textExample.pack()

def setText(s):
    textExample.insert(1.0, s)

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
    
    out = string
    out = out + ": "
    for i in string:
        if i in d:
            out = out + d[i] + " "
    setText(out)

def processText():
    result = textExample.get(1.0, tk.END+"-1c")
    textExample.delete(1.0,"end")
    readText(result)

btnSet = tk.Button(root, 
                   height=1, 
                   width=10, 
                   text="Set", 
                   command=lambda:processText())
btnSet.pack()

root.mainloop()
