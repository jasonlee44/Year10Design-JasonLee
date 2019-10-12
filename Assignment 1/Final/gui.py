from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("photo tagger")
root.geometry("500x350")

def test(event):
    print(event) #ensure that this line is indented
    
topframe = Frame(root,bg='#3bf5ff',height='20')
topframe.pack(fill=X) # make as wide as root
can1 = Canvas(topframe,height='20',width='20',bg="#3bf5ff",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind("<Button-1>",test ) # keyword
can1.pack(side=LEFT, padx=5, pady=5)

imgframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
imgframe.pack(fill=None, expand=False)
canvas = Canvas(imgframe,height=150,width=200)
canvas.grid(row=0,column=0)
l1 = Label(imgframe,text="Welcome to photo tagger\nA test of Material Design in Tkinter",fg="blue")
l1.grid(row=0,column=1)
myimage = Image.open("sky-banner.jpg")
myimage = myimage.resize((200, 150), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
canvas.create_image(0, 0, image=myimg, anchor = NW)


root.mainloop()