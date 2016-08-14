import sys
from Tkinter import *

root = Tk("Text Editor")
text = Text(root)
fileobj = open("E:\CSU LA Lecture Notes\~CS594 Game Development\PythonBasicsNotes.txt",'r+')
saveText = fileobj.read()
text.insert(INSERT,saveText)

text.grid()
root.mainloop()
fileo = open("E:\CSU LA Lecture Notes\~CS594 Game Development\PythonBasicsNotes.txt","w")
fileo.write("hi there")
fileo.close()
#writ = str(raw_input("write anything you want in the file. and then press save button"))
#fileobj.write(writ)

