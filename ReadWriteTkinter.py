import tkinter as new
def Add(): 
    newinp = inputt.get()
    if len(newinp) == 0:
        label['text'] = "Cant enter empty input"
    else:
        with open("new.txt","a") as file:
            
            file.write(f"\n{newinp}")
            label['text'] = "Successfully Added"
def read():
    with open("new.txt","r") as file:
        newfile = file.read()
        top = new.Toplevel(window)
        laman = new.Label(top,text=newfile)
        laman.pack()
window = new.Tk()
window.title("Simple Write")
label = new.Label(window,text="Write anything")
label.pack()
inputt = new.Entry(window)
inputt.pack()
btn = new.Button(window,text="Enter",command=Add)
btn.pack()
btnshow= new.Button(window,text="Show File",command=read)
btnshow.pack()
window.mainloop()

