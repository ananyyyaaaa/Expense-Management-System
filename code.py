import turtle
import os
import time
import pyttsx3 
text_speech = pyttsx3.init()

#MAIN SCREEN
def main_interface():
    pass
text_speech.say("WE WELCOME YOU.    PRESS 1 TO SIGN IN OR 2 TO SIGN UP")
text_speech.runAndWait()
def register():
    t.clear()
    t.goto(-500, 200)
    t.color("white")
    t.write("                       ****WE WELCOME YOU***\n\nFILL THE DETAILS TO CREATE A NEW ACCOUNT****",font=("arial", 30, "bold"))
    t.goto(-500,-100)
    text_speech.say("Please enter your Name")
    text_speech.runAndWait()
    t.write("NAME\n\nMOBILE NUMBER\n\nPIN",font=("arial",20,"bold"))
    turtle.textinput(title="Please enter your Name",prompt="")
    
    x=""
    
    while len(x)!=10:
        text_speech.say("Please enter your Mobile Number")
        text_speech.runAndWait()
        x=turtle.textinput(title="Please enter your Mobile Number",prompt="Number should be of 10 digits")
        x=str(x)
    
    y=""
    
    while len(y)!=4:
        text_speech.say("Please enter your PIN Number")
        text_speech.runAndWait()
        y=turtle.textinput(title="Please enter your PIN Number",prompt="Number should be of 4 digits")
        y=str(y)
    f=open("login.txt","a")
    f.write(" "+x)
    f.write(" "+y)
    f.close()
    


def error_screen():
    text_speech.say("User  not found")
    text_speech.runAndWait()
    t.clear()
    t.color("red")
    t.goto(-350, 50)
    t.write("****USER NOT FOUND***\n\n***Redirecting to the main page****",
            font=("arial", 40, "bold"))
    login_register()


def login():
    text_speech.say("PLEASE ENTER YOUR CREDENTIALS FOR LOGIN")
    text_speech.runAndWait()
    t.up()
    t.clear()
    t.color("white")
    t.goto(-550, 300)
    t.write("****PLEASE ENTER YOUR CREDENTIALS FOR LOGIN****",
            font=("arial", 30, "bold"))
    x = ""
    while len(x) != 10:
        text_speech.say("PLEASE ENTER YOUR MOBILE NUMBER")
        text_speech.runAndWait()
        x = turtle.textinput(title="Please enter your Mobile Number",prompt="Number shouls be of 10 digits")
        x = str(x)

    y = ""
    while len(y) != 4:
        text_speech.say("PLEASE ENTER YOUR PIN")
        text_speech.runAndWait()
        y = turtle.textinput(title="Please enter your PIN",prompt="PIN should be of 4 digits")
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
    t.color("white")
    t.write("Press 1 for Sign in", font=("arial", 20, "bold"))

    t.goto(-600, -100)
    t.color("white")
    t.write("Press 2 for Sign up", font=("arial", 20, "bold"))

    time.sleep(3)

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
# t.speed(1000)
win = turtle.Screen()
win.bgpic("0100.gif")

login_register()

turtle.done()


# if _name_ == "_main_":
#     main()
main()