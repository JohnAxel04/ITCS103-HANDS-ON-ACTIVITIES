import time
import os
os.system("cls")
txt1 = "Welcome to AxelsFileManager\n"
for text in txt1:
    print(text,end="", flush=True)
    time.sleep(.05)
while True:
    txt2 = "\nContinue?\n"
    for text in txt2:
        print(text,end="", flush=True)
        time.sleep(.03)
    ask = input("Yes/No: ").lower()
    if ask == "yes":
        os.system("cls")
        load = "loading.."
        for text in load:
            print(text,end="",flush=True)
            time.sleep(.2)
        os.system("cls")
        load2 = "..."
        for text in load2:
            print(text,flush=True)
            time.sleep(.4)
        os.system("cls")
        def menu():
            print("┌────────────────────────────────────────────────────────────────────┐")
            time.sleep(.1)
            print("│                        AxelsFileManager                            │")
            time.sleep(.1)
            print("│────────────────────────────────────────────────────────────────────│")
            time.sleep(.1)
            print("│   1 - Read Inspiring Messages                                      │")
            time.sleep(.1)
            print("│   2 - Add New Inspiring Messages                                   │")
            time.sleep(.1)
            print("│   3 - Rewrite Entire File                                          │")
            time.sleep(.1)
            print("│   4 - Exit                                                         │")
            time.sleep(.1)
            print("└────────────────────────────────────────────────────────────────────┘")
            time.sleep(.3)
        while True:
            menu()
            ask2 = int(input("Select: "))
            
            if ask2 == 1:
                while True:
                    os.system("cls")
                    title10 = "Your File\n"
                    for text in title10:
                        print(text,end="",flush=True)
                        time.sleep(.02)
                    with open("dreams.txt","r") as file:
                        new = file.read()
                        for text in new:
                            print(text,end="",flush=True)
                            time.sleep(.02)
                    ask3 = input("\n\nBack to menu(y/n)? ").lower()
                    if ask3 == "y":
                        os.system("cls")
                        break
                    elif ask3 == "n":
                        os.system("cls")
                        continue
                    else:
                        os.system("cls")
                        error1 = "Invalid Input\n"
                        for text in error1:
                            print(text,end="",flush=True)
                            time.sleep(.02)
                        time.sleep(.5)
                        continue
            elif ask2 == 2:
                while True:
                    os.system("cls")
                    item = "Add new inspiring messages\n\n"
                    for text in item:
                        print(text,end="",flush=True)
                        time.sleep(.02)
                    ask4 = input("Put message: ")
                    with open("dreams.txt","a") as file1:
                        write = file1.write(f"\n{ask4}")
                    wait = "\nadding.."
                    for text in wait:
                        print(text,end="",flush=True)
                        time.sleep(0.2)
                    os.system("cls")
                    wait1 = "..."
                    for text in wait1:
                        print(text,flush=True)
                        time.sleep(0.5)
                    os.system("cls")
                    wait2 = "Message Added"
                    for text in wait2:
                        print(text,end="",flush=True)
                        time.sleep(0.1)
                    ask5 = input("\n\nBack to menu(y/n)? ").lower()
                    if ask5 == "y":
                            os.system("cls")
                            break
                    elif ask5 == "n":
                        os.system("cls")
                        continue
                    else:
                        os.system("cls")
                        error1 = "Invalid Input\n"
                        for text in error1:
                            print(text,end="",flush=True)
                            time.sleep(.02)
                        time.sleep(.5)
                        continue
            elif ask2 == 3:
                while True:
                    os.system("cls")
                    itemmm = "Rewriting the File\n\n"
                    for text in itemmm:
                        print(text,end="",flush=True)
                        time.sleep(.02)
                    ask7 = input("Put message: ")
                    time.sleep(.2)
                    os.system("cls")
                    askl = "Are you sure?"
                    for text in askl:
                        print(text,end="",flush=True)
                        time.sleep(.02)
                    time.sleep(.3)
                    askll = "\nThis will overwrite your text file(y/n):\n"
                    for text in askll:
                        print(text,end="",flush=True)
                        time.sleep(.02)
                    ask6 = input("\nTyping... ").lower()
                    if ask6 == "y":
                        with open("dreams.txt","w") as file2:
                            wrt = file2.write(f"\n{ask7}")
                        wait11 = "\nCreating.."
                        for text in wait11:
                            print(text,end="",flush=True)
                            time.sleep(0.2)
                        os.system("cls")
                        wait12 = "..."
                        for text in wait12:
                            print(text,flush=True)
                            time.sleep(0.5)
                        os.system("cls")
                        wait23 = "New file created"
                        for text in wait23:
                            print(text,end="",flush=True)
                            time.sleep(0.1)
                        ask15 = input("\n\nBack to menu(y/n)? ").lower()
                        if ask15 == "y":
                            os.system("cls")
                            break
                        elif ask15 == "n":
                            os.system("cls")
                            continue    
                        else:
                            os.system("cls")
                            print("Invalid Input")
                            continue
                    elif ask6 == "n":
                        break
                    else:
                        os.system("cls")
                        error1 = "Invalid Input\n"
                        for text in error1:
                            print(text,end="",flush=True)
                            time.sleep(.02)
                        time.sleep(.5)
                        continue
            elif ask2 == 4:
                os.system("cls")
                ex = input("Exit(y/n): ").lower()
                if ex == "y":
                    os.system("cls")
                    print("Thank you for using my system")
                    exit()
                elif ex == "n":
                    continue
                else:
                    os.system("cls")
                    error1 = "Invalid Input\n"
                    for text in error1:
                        print(text,end="",flush=True)
                        time.sleep(.02)
                    time.sleep(.5)
                    continue
    elif ask == "no":
        os.system("cls")
        print("Thank you for using my system")
        break
    else:
        os.system("cls")
        error1 = "Invalid Input\n"
        for text in error1:
            print(text,end="",flush=True)
            time.sleep(.02)
        time.sleep(.5)
        continue