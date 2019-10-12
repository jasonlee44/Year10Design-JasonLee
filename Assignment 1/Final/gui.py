from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("photo tagger")
root.geometry("500x350")

def test(event):
    print(event) #ensure that this line is indented
topframe = Frame(root,bg='blue',height='20')
topframe.pack(fill=X)

can1 = Canvas(topframe,height='20',width='20',bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind("<Button-1>",test ) # keyword 
can1.grid(row=0,column=0, padx=5, pady=5)

spaceframe = Frame(root,height=10) #invisible
spaceframe.pack()

frame = LabelFrame(root,borderwidth = 2, relief=RAISED, width=400,height=150)
frame.pack()

lab1 = Label(frame, text="fjkdsjkfsdjkfasdkfjkasd fdsakjfasj fkasjlf",width=40,height=5)
lab1.grid(row=0,column=0)

e1 = Entry(frame)
e1.grid(row=1,column=0,sticky=W,padx=60)

b = Button(frame, text="Sumbit",command=AirQuality_API.enter)
b.grid(row=1, column=0,sticky=E,padx=60)


root.mainloop()