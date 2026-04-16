import tkinter as new
def Add():
    file = open("new.txt","a")
    newinp = inputt.get()
    file.write(newinp)
    file.close
    print("Successfully Added")
window = new.Tk()
window.title("Simple Write")
label = new.Label(window,text="Write anything")
label.pack()
inputt = new.Entry(window)
inputt.pack()
btn = new.Button(window,text="Enter",command=Add)
btn.pack()
window.mainloop()

