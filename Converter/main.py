from tkinter import *

def button_clicked():
    label["text"] = input_box.get()

window = Tk()
window.minsize(width=500, height=500)

label = Label()
label["text"] = "Teste de Componentes"
label.pack()

button = Button(text="Click me!", command=button_clicked)
button.pack()

input_box = Entry(width=10)
input_box.pack()

window.mainloop()