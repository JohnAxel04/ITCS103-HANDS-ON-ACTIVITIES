import tkinter as taka

window = taka.Tk()
window.geometry("500x500")
window.resizable(False,False)
window.configure()
window.title("My Second Practice")
lbl = taka.Label(window, text="Hello World",font=("arial",30,"bold"),width=100,pady=10)
lbl.pack()
img = taka.PhotoImage(file="tree.png")
img = img.subsample(2,2)
imgLabel = taka.Label(window,image=img)
# imgLabel.pack()
def showPicture():
    btn['text'] = "Button Clickced!"
btn = taka.Button(window,text="CLick me Yow",fg="lightgreen",activeforeground="green",bg="grey",activebackground="lightgrey",command=showPicture)
btn.pack()


window.mainloop()