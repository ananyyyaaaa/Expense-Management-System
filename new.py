# import turtle
# import os
# import time
# import pyttsx3 
# text_speech = pyttsx3.init()

# #MAIN SCREEN
# def main_interface():
#     pass
# text_speech.say("WE WELCOME YOU.       PRESS 1 TO SIGN IN OR       2 TO SIGN UP")
# text_speech.runAndWait()
# def register():
#     t.clear()
#     t.goto(-500, 200)
#     t.color("white")
#     t.write("                       ****WE WELCOME YOU***\n\nFILL THE DETAILS TO CREATE A NEW ACCOUNT****",font=("arial", 30, "bold"))
#     t.goto(-500,-100)
#     text_speech.say("Please enter your Name")
#     text_speech.runAndWait()
#     t.write("NAME\n\nMOBILE NUMBER\n\nPIN",font=("arial",20,"bold"))
#     turtle.textinput(title="Please enter your Name",prompt="")
    
#     x=""
    
#     while len(x)!=10:
#         text_speech.say("Please enter your Mobile Number")
#         text_speech.runAndWait()
#         x=turtle.textinput(title="Please enter your Mobile Number",prompt="Number should be of 10 digits")
#         x=str(x)
    
#     y=""
    
#     while len(y)!=4:
#         text_speech.say("Please enter your PIN Number")
#         text_speech.runAndWait()
#         y=turtle.textinput(title="Please enter your PIN Number",prompt="Number should be of 4 digits")
#         y=str(y)
#     f=open("login.txt","a")
#     f.write(" "+x)
#     f.write(" "+y)
#     f.close()
    


# def error_screen():
#     text_speech.say("User  not found")
#     text_speech.runAndWait()
#     t.clear()
#     t.color("red")
#     t.goto(-350, 50)
#     t.write("****USER NOT FOUND***\n\n***Redirecting to the main page****",
#             font=("arial", 40, "bold"))
#     login_register()


# def login():
#     text_speech.say("PLEASE ENTER YOUR CREDENTIALS FOR LOGIN")
#     text_speech.runAndWait()
#     t.up()
#     t.clear()
#     t.color("white")
#     t.goto(-550, 300)
#     t.write("****PLEASE ENTER YOUR CREDENTIALS FOR LOGIN****",
#             font=("arial", 30, "bold"))
#     x = ""
#     while len(x) != 10:
#         text_speech.say("PLEASE ENTER YOUR MOBILE NUMBER")
#         text_speech.runAndWait()
#         x = turtle.textinput(title="Please enter your Mobile Number",prompt="Number shouls be of 10 digits")
#         x = str(x)

#     y = ""
#     while len(y) != 4:
#         text_speech.say("PLEASE ENTER YOUR PIN")
#         text_speech.runAndWait()
#         y = turtle.textinput(title="Please enter your PIN",prompt="PIN should be of 4 digits")
#         y = str(y)

#     f = open("login.txt", "r")
#     users = f.readline().split()
#     z = 0
#     while z < len(users):
#         if users[z] == x and users[z+1] == y:
#             main_interface()
#             break
#         z += 2
#     else:
#         error_screen()
#     f.close()


# def login_register():
   
#     t.clear()
#     t.color("white")
#     t.goto(-600, 300)
#     t.write("****WELCOME TO THE MONEY MANAGEMENT SYSTEM****",
#             font=("arial", 30, "bold"))
#     t.goto(-600, 100)
#     t.color("white")
#     t.write("Press 1 for Sign in", font=("arial", 20, "bold"))

#     t.goto(-600, -100)
#     t.color("white")
#     t.write("Press 2 for Sign up", font=("arial", 20, "bold"))

#     time.sleep(3)

#     switch1 = turtle.numinput(title="Please enter your input",
#                               prompt="")

#     match(switch1):
#         case 1:
#             login()
#         case 2:
#             register()


# t = turtle.Turtle()
# t.hideturtle()
# t.up()
# # t.speed(1000)
# win = turtle.Screen()
# win.bgpic("0100.gif")

# login_register()

# turtle.done()


# # if _name_ == "_main_":
# #     main()
# main()


import turtle
import os
import time
def addcredit():
    pass

def adddebit():
    f=open("current_balance.txt","r+")
    x=int(f.readline())
    x-=turtle.numinput(title="Enter your choice",prompt="")


def add_dccc():
    win.bgpic("debit_image.gif")
    f=open("debit_info.txt","w")
    x=turtle.textinput(title="Enter your Card",prompt="Number")
    t.goto(-140,350)
    t.write(x,font=("airel",20,"bold"))
    f.write(str(x)+"\n")

    x=turtle.textinput(title="Enter your Card",prompt="EXP DT")
    t.goto(-300,250)
    t.write(x,font=("ariel",20,"bold"))
    f.write(str(x)+"\n")

    x=turtle.textinput(title="Enter Name On",prompt="The Card")
    t.goto(100,250)
    t.write(x,font=("airel",20,"bold"))
    f.write(str(x)+"\n")

    x=turtle.textinput(title="Enter Card",prompt="CVV Code")
    t.goto(100,-300)
    t.write(x,font=("airel",20,"bold"))
    f.write(str(x))

def currentbalance():
    f=open("current_balance.txt","r")
    t.clear()
    t.goto(-200,0)
    t.color("green")
    t.write("Your Current Balace Is RS-"+f.readline(),font=("airel",30,"bold"))
    f.close()

def view_dccc():
    f=open("debit_info.txt","r")
    t.clear()
    t.color("black")
    win.bgpic("debit_image.gif")
    t.goto(-140,330)
    x=f.readline()
    t.write(x,font=("airel",20,"bold"))
    t.goto(-300,250)
    x=f.readline()
    t.write("EXP DT "+x,font=("airel",20,"bold"))
    t.goto(100,250)
    x=f.readline()
    t.write(x,font=("airel",20,"bold"))
    t.goto(100,-300)
    x=f.readline()
    t.write("CVV "+x,font=("airel",20,"bold"))
    t.color("red")
    turtle.numinput(title="Press Any Key For Exit",prompt="")
    f.close()
    main_interface()

def main_interface():
    win.bgpic("0100.gif")
    t.clear()
    t.goto(-600,300)
    t.color("blue")
    t.write("****WELCOME TO THE MONEY MANAGEMENT SYSTEM****",font=("airel",30,"bold"))
    t.goto(-500,-200)
    t.write("Press 1 to Add a Credit\n\n\nPress 2 to Add a Debit\n\n\nPress 3 to Add a Debit or Credit card\n\n\nPress 4 to View Current Balance",font=("airel",20,"bold"))
    switch2=turtle.numinput(title="Enter your choice",prompt="")
    
    match(switch2):
        case 1:
            addcredit()
        case 2:
            adddebit()
        case 3:
            add_dccc()
        case 4:
            currentbalance()
        case 5:
            view_dccc()

def register():
    t.clear()
    t.goto(-500, 200)
    t.color("white")
    t.write("                       ****WE WELCOME YOU***\n\nFILL THE DETAILS TO CREATE A NEW ACCOUNT*",
            font=("arial", 30, "bold"))
    t.goto(-500,-100)
    t.write("NAME\n\nMOBILE NUMBER\n\nPIN",font=("arial",20,"bold"))
    turtle.textinput(title="Please enter your Name",
                        prompt="")
    x=""
    while len(x)!=10:
        x=turtle.textinput(title="Please enter your Mobile Number",prompt="Number should be of 10 digits")
        x=str(x)
    y=""
    while len(y)!=4:
        y=turtle.textinput(title="Please enter your PIN Number",prompt="Number should be of 4 digits")
        y=str(y)
    f=open("login.txt","a")
    f.write(" "+x)
    f.write(" "+y)
    f.close()
    
def error_screen():
    t.clear()
    t.color("red")
    t.goto(-350, 50)
    t.write("****USER NOT FOUND***\n\n***Redirecting to the main page****",
            font=("arial", 40, "bold"))
    login_register()

def login():
    t.up()
    t.clear()
    t.color("white")
    t.goto(-550, 300)
    t.write("****PLEASE ENTER YOUR CREDENTIALS FOR LOGIN****",
            font=("arial", 30, "bold"))
    x = ""
    while len(x) != 10:
        x = turtle.textinput(title="Please enter your Mobile Number",
                             prompt="")
        x = str(x)

    y = ""
    while len(y) != 4:
        y = turtle.textinput(title="Please enter your PIN",
                             prompt="PIN should be of 4 digits")
        y = str(y)

    f = open("login.txt", "r")
    users = f.readline().split()
    z = 0
    while z < len(users):
        if users[z] == x and users[z+1] == y:
            main_interface()
            break
        z += 2
    else:
        error_screen()
    f.close()

def login_register():
    t.clear()
    t.color("white")
    t.goto(-600, 300)
    t.write("****WELCOME TO THE MONEY MANAGEMENT SYSTEM****",
            font=("arial", 30, "bold"))
    t.goto(-600, 100)
    t.color("red")
    t.write("Press 1 for Sign in", font=("arial", 20, "bold"))

    t.goto(-600, -100)
    t.color("red")
    t.write("Press 2 for Sign up", font=("arial", 20, "bold"))

    time.sleep(2)

    switch1 = turtle.numinput(title="Please enter your input",
                              prompt="")

    match(switch1):
        case 1:
            login()
        case 2:
            register()

t = turtle.Turtle()
t.hideturtle()
t.up()
win = turtle.Screen()
win.bgpic("0100.gif")

currentbalance()

turtle.done()