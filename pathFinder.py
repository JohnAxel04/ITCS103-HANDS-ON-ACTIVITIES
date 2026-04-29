import os 
current = os.getcwd()
print(current)

filepath = os.path.join(current,"NewNew.txt")
if os.path.exists(filepath):
    okay = open(filepath,"r")
    read = okay.read()
    okay.close()
    print(read)
else:
    print("okay")
