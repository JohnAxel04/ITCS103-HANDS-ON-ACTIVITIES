file = open("NewNew.txt","w")
writes = file.write("Hello World")

file.close
print("sucess")
ihn = input("Yes/no: ").lower()
if ihn == "yes":
    newfile = open("NewNew.txt","r")
    readfile = newfile.read()
    newfile.close()
    print(readfile)
else:
    print("Thank you")