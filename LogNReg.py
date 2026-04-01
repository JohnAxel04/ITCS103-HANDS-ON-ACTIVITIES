import tkinter as log
usernames = []
passwords = []

def loginNaman():
    
    def loggin():
        user = userEntry.get()
        passw = passEntry.get()
        if user == usernames[-1] and passw == passwords[-1]:
            logMain['text'] = "Succesfully logged"
            logMain['bg'] = "green"
            loginTop['bg'] = "green"
            userLabel['bg'] = "green"
            passLabel['bg'] = "green"
        else:
            logMain['text'] = "Credential Invalid"
            logMain['bg'] = "red"
            loginTop['bg'] = "red"
            userLabel['bg'] = "red"
            passLabel['bg'] = "red"
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
    loginButton = log.Button(loginTop,text="Log In",command=loggin)
    loginButton.grid(row=7,columnspan=3)

def registerMuna():
    
    def regMo():
        user = usernameEntry.get()
        passw = passwordEntry.get()
        if len(passw) < 8 and len(passw) > 0:
            regLabel['text'] = "Password must be 8 character"
            regLabel['bg'] = "red"
            regTop['bg'] = "red"
            username['bg'] = "red"
            password['bg'] = "red"
        elif len(passw) >= 8:
            usernames.append(user)
            passwords.append(passw)
            regLabel['text'] = "Account Succesfully Registered"
            regTop['bg'] = "green"
            regLabel['bg'] = "green"
            username['bg'] = "green"
            password['bg'] = "green"
        else:
            regLabel['text'] = "Input must not be blank"
            regTop['bg'] = "red"
            regLabel['bg'] = "red"
            username['bg'] = "red"
            password['bg'] = "red"
        print(usernames,passwords)
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
    registerButton = log.Button(regTop,text="register",command=regMo)
    registerButton.grid(columnspan=3,row=4)
window = log.Tk()

mainLabel = log.Label(window,text="Welcome",font=("arial",12,"bold"))
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