import tkinter as log



def entered():
    def Cards():
        card = log.Toplevel(topframe)
        card.grab_set()
        cardLabel = log.Label(card,text="Profile")
        cardLabel.grid(columnspan=5)
        nameVar = NameEntry.get()
        lnameVar = LastEntry.get()
        ageVar = ageEntry.get()
        addVar = AddressEntry.get()
        lastImg = log.PhotoImage(file="pic.png")
        lastImg = lastImg.subsample(18,18)
        lastImgLabel = log.Label(card,image=lastImg)
        lastImg.image = lastImg
        lastImgLabel.grid(row=1,columnspan=2,rowspan=3)
        fullname = log.Label(card,text="Name:")
        fullname.grid(row=1,column=2)
        fullnameText = log.Label(card,text=f"{nameVar} {lnameVar}")
        fullnameText.grid(row=1,column=3,columnspan=2)
        genderT = log.Label(card,text="Gender:")
        genderT.grid(column=2,row=2)
        genderText = log.Label(card,text="")
        genderText.grid(row=2,column=3,columnspan=2)
        newgenderval = genderVal.get()
        if newgenderval == 0:
            genderText['text'] = "Male"
        elif newgenderval == 1:
            genderText['text'] = "Female"
        addr = log.Label(card,text="Adress:")
        addr.grid(row=3,column=2)
        addrText = log.Label(card,text=addVar)
        addrText.grid(row=3,column=3,columnspan=2)
    def switchColorFemale():
        main['bg'] = "pink"
    def switchColorMale():
        main['bg'] = "lightblue"

    global genderVal
    main = log.Toplevel(window)
    main.grab_set()
    main.transient(window)
    main.resizable(False,False)
    main.config(bg="lightblue")
    main.title("Main")
    menuBar = log.Menu(main)
    main.config(menu=menuBar)
    menuLabel = log.Menu(menuBar,tearoff=0)
    
    menuLabel.add_command(label="Open")
    menuLabel.add_command(label="Save")
    menuLabel.add_separator()
    menuLabel.add_command(label="Exit")

    menuBar.add_cascade(label="File" ,menu=menuLabel)

    menuLabel2 = log.Menu(menuBar,tearoff=0)
    menuLabel2.add_command(label="Zoom In")
    menuLabel2.add_command(label="Zoom Out")
    menuBar.add_cascade(label="Zoom", menu=menuLabel2)

    topframe = log.Frame(main)
    topframe.pack(padx=10,pady=10)
    topLabel = log.Label(topframe,text="Welcome your Create Profile",font=("Poppins",12,"bold"))
    topLabel.grid(columnspan=5,row=0,column=0)
    newImg = log.PhotoImage(file="pic.png")
    newImg = newImg.subsample(12,12)
    newImgLabel = log.Label(topframe,image=newImg)
    newImgLabel.image = newImg
    newImgLabel.grid(column=0,row=1,columnspan=2,rowspan=2)
    NameLabel = log.Label(topframe,text="First Name:")
    NameLabel.grid(row=1,column=2)
    NameEntry = log.Entry(topframe)
    NameEntry.grid(column=3,row=1,columnspan=2)
    LastLabel = log.Label(topframe,text="Last Name:")
    LastLabel.grid(column=2,row=2)
    LastEntry = log.Entry(topframe)
    LastEntry.grid(column=3,row=2,columnspan=2)
    
    MaleGender = log.Radiobutton(topframe,text="Male",variable=genderVal,value=0,command=switchColorMale)
    MaleGender.grid(row=4,column=0)
    FemaleGender = log.Radiobutton(topframe,text="Female",variable=genderVal,value=1,command=switchColorFemale)
    FemaleGender.grid(row=4,column=1)
    ageLabel = log.Label(topframe,text="Age:")
    ageLabel.grid(column=2,row=4)
    ageEntry = log.Entry(topframe)
    ageEntry.grid(column=3,row=4,columnspan=2)
    Address = log.Label(topframe,text=" Home Address")
    Address.grid(column=2,row=5)
    AddressEntry = log.Entry(topframe)
    AddressEntry.grid(column=3,row=5,columnspan=2,pady=(0,0))
    messageText = log.Text(topframe,width=30,height=4)
    messageText.grid(column=0,row=6,columnspan=5,rowspan=2,pady=5)
    
    Create = log.Button(topframe,text="Create Profile",command=Cards)
    Create.grid(row=8,columnspan=5,pady=10)

window = log.Tk()
window.title("Log In System")
window.resizable(False,False)
frame = log.Frame(window,bg="#777")
frame.pack(pady=10,padx=20)
mainLabel = log.Label(frame,text="Syster Log In",bg="#777",font=("Poppins",15,"bold"))
mainLabel.grid(columnspan=3,pady=10)
imgg = log.PhotoImage(file="pic.png")
imgg = imgg.subsample(5,5)
imgLabel = log.Label(frame,image=imgg,bg="#777")
imgLabel.grid(row=1,columnspan=3,rowspan=3,pady=5)
userLabel = log.Label(frame,text="UserName:",bg="#777",fg="white")
userLabel.grid(row=4,column=0)
userEntry = log.Entry(frame)
userEntry.grid(row=4,column=1,columnspan=2,padx=5)
passLabel = log.Label(frame,text="Password:",bg="#777",fg="white")
passLabel.grid(column=0,row=5)
passEntry = log.Entry(frame,show="*")
passEntry.grid(column=1,row=5,columnspan=2,pady=10)
enterBtn = log.Button(frame,text="Log In",command=entered,relief="flat")
enterBtn.grid(row=6,columnspan=3,pady=5,column=0)
genderVal = log.IntVar()  

window.mainloop()