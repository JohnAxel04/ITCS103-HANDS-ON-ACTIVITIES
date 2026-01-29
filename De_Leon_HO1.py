import time

listKo = []

a = ("Welcome to my Activity\n")
for text in a:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)

a1 = ("Named...\n")
for text in a1:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.3)

a2 = ("Name Or Number\n")
for text in a2:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)

a3 = ("\nLets Start\n")
for text in a3:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.2)
z = 0

a7 = ("\nWhat is you Name? ")
for text in a7:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)
x = input("\nTyping... ")

#to get the length of the input name 
y = len(x)

a8 = (f"\nYour name is '{x}' Hello!\n")
for text in a8:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)

#numbers "for loop"
for i in range(y):
    tanong = int(input(f"\nPut the Number {i + 1} : ")) # +1 so that the input will start at count of 1 rather than  0
    listKo.append(tanong)
    z += tanong

z /= i+1 # +1 again because when i saw my first output it looks like over of 1 then i try to put +1 and it became correct 

#list
a6 = (f"\nThis is your Numbers\n")
for text in a6:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)
print(listKo)

#length
a4 = (f"\nThe Length of your Name is '{y}'")
for text in a4:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)

#average
a5 = (f"\nThe Average of your Numbers is '{z:.2f}'")
for text in a5:
    print(text,end="", flush=True)
    time.sleep(0.07)
time.sleep(.5)
if y > z:
    print(f"\nYour Name '{x}' is greater than the average")
else:
    print(f"\nYour Name '{x}' is less than the average")
