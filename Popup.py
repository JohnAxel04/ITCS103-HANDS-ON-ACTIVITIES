import tkinter as new

def pop():
    def exit():
        popup.destroy()
    btn['text'] = "Hii CLICK MEE AGAIN!"
    popup = new.Toplevel()
    popup.title("Hello")
    popup.geometry("500x500")
    popup.transient(window)
    popup.grab_set()


    img = new.PhotoImage(file="tree.png")
    img = img.subsample(3,3)

    imglbl = new.Label(popup,image=img)
    imglbl.image = img
    imglbl.pack()

    cong = new.Label(popup, text="WElCOME BROTHA",font=("Arial", 10 , "bold"))
    cong.pack()

    btnpop = new.Button(popup,text="Exit", command=exit)
    btnpop.pack(pady=10)
window = new.Tk()
window.title("Pop up Button")
window.geometry("450x450")
window.resizable(False,False)
btn = new.Button(text="Hello CLICK MEE!", command=pop)
btn.pack(pady=20)

window.mainloop()