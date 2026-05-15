import tkinter as new
import openpyxl as op
from tkinter import ttk,messagebox

work = op.Workbook()
sheet = work.active
sheet["a1"] = "ID"
sheet["b1"] = "Full Name"
sheet["c1"] = "Birth Date"
sheet["d1"] = "Age"
sheet["e1"] = "Gender"
work.save("letsgo.xlsx")


def inputvalidation():
    full = nameEntry.get()
    birth = birthEntry.get()
    
    if not full or not birth:
        messagebox.showerror("Input Invalid","Entry must not be empty")
        return False
    if not birth.isdigit():
        messagebox.showerror("Input Invalid","Birth date must be a number")
        return False
    
    return True
    
def save():
    if not inputvalidation():
        return
    
    full = nameEntry.get()
    birth = int(birthEntry.get())
    age = 2026 - birth
    gender = var.get()

    
    nameEntry.delete(0,new.END)
    birthEntry.delete(0,new.END)

    loads = op.load_workbook("letsgo.xlsx")
    sheets = loads.active
    id = sheets.max_row
    sheets.append([id,full,birth,age,gender])
    loads.save("letsgo.xlsx")
    show()
    messagebox.showinfo("Success","You file is successfully saved")

def show():
    workload = op.load_workbook("letsgo.xlsx")
    sht = workload.active
    for i in table.get_children():
        table.delete(i)

    for i in sht.iter_rows(min_row=2,values_only=True):
        table.insert("",new.END,values=i)

window = new.Tk()
window.title("Simple User Input")
titles = new.Label(window,text="User Input")
titles.grid(column=0,columnspan=3,row=0)
namelabel = new.Label(window,text="Full Name:")
namelabel.grid(column=0,row=1)
nameEntry = new.Entry(window)
nameEntry.grid(column=1,columnspan=2,row=1)

var = new.StringVar()
var.set("Male")
male = new.Radiobutton(window,text="Male",value="Male",variable=var)
male.grid(column=0,row=3)
female = new.Radiobutton(window,text="Female",value="Female",variable=var)
female.grid(column=1,row=3)


birthlabel = new.Label(window,text="BirthYear:")
birthlabel.grid(column=0,row=2)
birthEntry = new.Entry(window)
birthEntry.grid(row=2,column=1,columnspan=2)
updatebtn = new.Button(window,text="Update")
updatebtn.grid(column=0,row=4)
savebtn = new.Button(window,text="Save",command=save)
savebtn.grid(column=1,row=4)
delbtn = new.Button(window,text="Delete")
delbtn.grid(column=2,row=4)

table = ttk.Treeview(window,columns=("ID","Full Name","Birth Year","Age","Gender"),show="headings")
for col in ("ID","Full Name","Birth Year","Age","Gender"):
    table.heading(col,text=col)
table.grid(row=5,pady=10,columnspan=3)
show()
window.mainloop()
