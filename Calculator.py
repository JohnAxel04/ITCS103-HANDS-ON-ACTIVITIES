import tkinter as new

window = new.Tk()
# window.geometry("300x250")
window.title("Basic Calculator")
calculation = ""

def add_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text.delete(1.0,"end")
    text.insert(1.0, calculation)
def clear():
    global calculation
    calculation = ""
    text.delete(1.0,"end")
def evali():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        text.delete(1.0,"end")
        text.insert(1.0, result)
    except:
        clear()
        text.insert(1.0,"Error")
text = new.Text(window,height=2,font=("Arial",17),width=16)
text.grid(column=0,row=0,columnspan=5)

btn1 = new.Button(window,text="1",command=lambda : add_calculation(1),width=5)
btn1.grid(column=0,row=1)
btn2 = new.Button(window,text="2",command=lambda : add_calculation(2),width=5)
btn2.grid(column=1,row=1)
btn3 = new.Button(window,text="3",command=lambda : add_calculation(3),width=5)
btn3.grid(column=2,row=1)

btn4 = new.Button(window,text="4",command=lambda : add_calculation(4),width=5)
btn4.grid(column=0,row=2)
btn5 = new.Button(window,text="5",command=lambda : add_calculation(5),width=5)
btn5.grid(column=1,row=2)
btn6 = new.Button(window,text="6",command=lambda : add_calculation(6),width=5)
btn6.grid(column=2,row=2)
btn7 = new.Button(window,text="7",command=lambda : add_calculation(7),width=5)

btn7.grid(column=0,row=3)
btn8 = new.Button(window,text="8",command=lambda : add_calculation(8),width=5)
btn8.grid(column=1,row=3)
btn9 = new.Button(window,text="9",command=lambda : add_calculation(9),width=5)
btn9.grid(column=2,row=3)
btnpar = new.Button(window,text="(",command=lambda : add_calculation("("),width=5)
btnpar.grid(column=0,row=4)
btn0 = new.Button(window,text="0",command=lambda : add_calculation(0),width=5)
btn0.grid(column=1,row=4)

btnpar1 = new.Button(window,text=")",command=lambda : add_calculation(")"),width=5)
btnpar1.grid(column=2,row=4)
btnpar1 = new.Button(window,text="/",command=lambda : add_calculation("/"),width=5)
btnpar1.grid(column=3,row=1)
btnpar1 = new.Button(window,text="*",command=lambda : add_calculation("*"),width=5)
btnpar1.grid(column=3,row=2)
btnpar1 = new.Button(window,text="-",command=lambda : add_calculation("-"),width=5)
btnpar1.grid(column=3,row=3)
btnpar1 = new.Button(window,text="+",command=lambda : add_calculation("+"),width=5)
btnpar1.grid(column=3,row=4)

clear1 = new.Button(window,text="C",command=clear,width=12)
clear1.grid(column=0,row=5,columnspan=2)
equal = new.Button(window,text="=",command=evali,width=12)
equal.grid(column=2,row=5,columnspan=2)
window.mainloop()