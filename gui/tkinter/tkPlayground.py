from tkinter import *

def handleButton():
    print("fuck you")


mainWindow = Tk()
mainWindow.title("Testing")

label = Label(mainWindow,text="MyLabel")
label.place(x=10,y=10)
button = Button(mainWindow, 
                text="test???????????", 
                command=handleButton)
button.pack()

mainWindow.mainloop()
