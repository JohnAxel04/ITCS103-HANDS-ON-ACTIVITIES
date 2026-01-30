import time

listKo = []

print("Welcome to my Activity")


print("Name Or Number")

print("\nLets Start")

z = 0 #total of the numbers

x = input("What is you Name? ")

y = len(x)#to get the length of the input name 

print(f"\nYour name is '{x}' Hello!")


#numbers "for loop"
for i in range(y):
    tanong = int(input(f"Put the Number {i + 1} : ")) # +1 so that the input will start at count of 1 rather than  0
    listKo.append(tanong)
    z += tanong

def average(name , num):
    return name / num

aver = average(z , y)

#list
print(f"\nThis is your Numbers")
print(listKo)

#length
print(f"\nThe Length of your Name is '{y}'")

#average
print(f"The Average of your Numbers is '{aver:.2f}'")

def com():
    if y > aver:
        print(f"Your Name '{x}' is greater than the average")
    elif y == aver:
        print(f"Your Name '{x}' is the same as the average\n")
    else:
        print(f"Your Name '{x}' is less than the average")
com()
