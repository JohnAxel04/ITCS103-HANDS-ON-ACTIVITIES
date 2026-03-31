import tkinter as log
username = []
password = []
def loginNaman():
    loginTop = log.Toplevel(window)
    loginTop.grab_set()
    loginTop.transient(window)
    loginTop.title("Log In")
    logMain = log.Label(loginTop,text="Log In")
    logMain.grid(columnspan=3)
    img = log.PhotoImage(file="pic.png")
    img = img.subsample(10,10)
    imgLabel = log.Label(loginTop,image=img)
    imgLabel.image = img
    imgLabel.grid(columnspan=3,rowspan=3)
    userLabel = log.Label(loginTop,text="Username:")
    userLabel.grid(row=4)
    userEntry = log.Entry(loginTop)
    userEntry.grid(row=4,column=1,columnspan=2)
    passLabel = log.Label(loginTop,text="Password:")
    passLabel.grid(row=5)
    passEntry = log.Entry(loginTop)
    passEntry.grid(row=5,column=1,columnspan=2)
    showEntryPass = log.Checkbutton(loginTop,text="Show Password")
    showEntryPass.grid(row=6,column=1,columnspan=2)
    loginButton = log.Button(loginTop,text="Log In")
    loginButton.grid(row=7,columnspan=3)
def registerMuna():
    regTop = log.Toplevel(window)
    regTop.grab_set()
    regTop.transient(window)
    regTop.title("Register")
    regLabel = log.Label(regTop,text="Register",font=("arial",12,"bold"))
    regLabel.grid(columnspan=3)
    username = log.Label(regTop,text="Username:")
    username.grid(row=1)
    usernameEntry = log.Entry(regTop)
    usernameEntry.grid(column=1,row=1,columnspan=2)
    password  = log.Label(regTop,text="Password:")
    password.grid(column=0,row=2)
    passwordEntry = log.Entry(regTop)
    passwordEntry.grid(row=2,column=1,columnspan=2)
    showpass = log.Checkbutton(regTop,text="Show Password")
    showpass.grid(column=1,row=3,columnspan=2)
    registerButton = log.Button(regTop,text="register")
    registerButton.grid(columnspan=3,row=4)
window = log.Tk()

mainLabel = log.Label(window,text="Welcome")
mainLabel.pack(fill="x")
img = log.PhotoImage(file="pic.png")
img = img.subsample(7,7)
imglabel = log.Label(window,image=img)
imglabel.pack()
def inn2(event):
    logButton['bg'] = "blue"
def out2(event):
    logButton['bg'] = "lightblue"
logButton = log.Button(window,text="Log In",bg="lightblue",activebackground="lightblue",command=loginNaman)
logButton.bind("<Enter>",inn2)
logButton.bind("<Leave>",out2)
logButton.pack(fill="x")
def inn(event):
    regButton['bg'] = "darkgreen"
def out(event):
    regButton['bg'] = "green"
regButton = log.Button(window,text="register",bg="green",activebackground="green",command=registerMuna)
regButton.bind("<Enter>",inn)
regButton.bind("<Leave>",out)
regButton.pack(fill="x")

window.mainloop()