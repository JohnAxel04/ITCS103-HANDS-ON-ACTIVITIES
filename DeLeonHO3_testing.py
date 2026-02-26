import tkinter as  tk

window = tk.Tk()
window.title("Button and img")
window.configure(background="green")
window.geometry("500x500")
window.resizable(True,True)

fRame = tk.Frame(window, bg="white",width=100)
fRame.pack(pady=20)

lbl = tk.Label(fRame,text="My Activity",bg= "white")
lbl.pack()
radioVal = tk.IntVar()
radioBtn = tk.Radiobutton(fRame, text="Check mee",variable=radioVal,value=0)
radioBtn.pack(padx= 10,pady=10)
radioBtn1 = tk.Radiobutton(fRame, text="Check mee not",variable=radioVal,value=1)
radioBtn1.pack(padx= 10,pady=10)
radioBtn2 = tk.Radiobutton(fRame, text="Check neither",variable=radioVal,value=2)
radioBtn2.pack(padx= 10,pady=10)
radioBtn3 = tk.Radiobutton(fRame, text="Check maybe",variable=radioVal,value=3)
radioBtn3.pack(padx= 10,pady=10)
listBoxLabel = tk.Label(text="Choose -->")
listBoxLabel.pack(padx=10,pady=10)

listBox = tk.Listbox(fRame,selectmode= "multiple")
listBox.insert(0,"python")
listBox.insert(1,"CSS")
listBox.insert(2,"HTML")
listBox.insert(3,"Js")
listBox.pack(padx=10,pady=10)

checkVal = tk.IntVar()
checkBtn = tk.Checkbutton(fRame,text="Remember Them",variable=checkVal)
checkBtn.pack(padx=10,pady=10)

btn = tk.Button(window,text="submit")
btn.pack(padx=10,pady=10)

window.mainloop()