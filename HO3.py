import tkinter as cal

def addition():
    value = enter.get()
    value2 = enter2.get()
    value = eval(value)
    value2 = eval(value2)
    total = value + value2
    lbl['text'] = f"The sum of {value} and {value2} is {total}"
    
def subt():
    value = enter.get()
    value2 = enter2.get()
    value = eval(value)
    value2 = eval(value2)
    total = value - value2
    lbl['text'] = f"The difference of {value} and {value2} is {total}"
def mult():
    value = enter.get()
    value2 = enter2.get()
    value = eval(value)
    value2 = eval(value2)
    total = value * value2
    lbl['text'] = f"The product of {value} and {value2} is {total}"
def divd():
    value = enter.get()
    value2 = enter2.get()
    value = eval(value)
    value2 = eval(value2)
    total = value / value2
    lbl['text'] = f"The cousient of {value} and {value2} is {total}"
window = cal.Tk()
window.title("Simple Calculator")
window.config(bg="#333")
frame = cal.Frame(window,bg="lightgrey")
frame.pack(padx=10,pady=10)
lbl = cal.Label(frame,text="Simple Calculator",font=("Arial",13,"bold"),bg="#777",width=25,height=2)
lbl.grid(column=0,row=0,columnspan=3)

firstLabel = cal.Label(frame,text="Enter 1st Number:",font=("Arial",10),bg="lightgrey")
firstLabel.grid(column=0,row=1,columnspan=2,pady=5)

enter = cal.Entry(frame)
enter.grid(column=2,row=1,pady=5)

secondLabel = cal.Label(frame,text="Enter 2nd Number:",font=("Arial",10),bg="lightgrey")
secondLabel.grid(column=0,row=2,columnspan=2,pady=5)

enter2 = cal.Entry(frame)
enter2.grid(column=2,row=2,pady=5)

btnAdd = cal.Button(frame,text="Addition",command=addition,font=("Arial",10),relief="groove",fg="#111",bg="#888")
btnAdd.grid(column=0,row=3,columnspan=2,pady=5)

btnSub = cal.Button(frame,text="Subtraction",command=subt,font=("Arial",10),relief="groove",fg="#111",bg="#888")
btnSub.grid(column=2,row=3,pady=5)

btnMul = cal.Button(frame,text="Multiplication",command=mult,font=("Arial",10),relief="groove",fg="#111",bg="#888")
btnMul.grid(column=0,row=4,columnspan=2,pady=5)

btnDiv = cal.Button(frame,text="Division",command=divd,font=("Arial",10),relief="groove",fg="#111",bg="#888")
btnDiv.grid(column=2,row=4,pady=5)

window.mainloop()
