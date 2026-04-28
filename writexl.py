import openpyxl as op
wrk = op.Workbook()
sheet = wrk.active    
ques = input("Put your name: ")
age = input("Put your age: ")
course = input("Put your course: ")
sheet.append([ques,age,course])
wrk.save("new.xlsx")
print("success")
