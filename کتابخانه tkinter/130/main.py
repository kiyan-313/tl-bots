from tkinter import *

window = Tk()
window.geometry("300x300")
window.maxsize(300,300)
window.minsize(200,200)
window.title('haya')


label=Label(window, text='heloo jamal',fg='red',bg='blue')
label.pack()

def hello():
    label.config(text=input.get())
    button.config(text='sami')


button = Button(window,text='hello',fg='red',bg='yellow',command=hello)
button.pack()

input=Entry(window)
input.pack()

window.mainloop()