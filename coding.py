# Import Time
import time
import pyttsx3
from datetime import date
from datetime import datetime
from prettytable import PrettyTable
text_speech = pyttsx3.init()
Vehicle_Number = ['XXXX-XX-XXXX']
Vehicle_Type = ['Bike']
Vehicle_Name = ['Intruder']
Owner_Name = ['Unknown']
Date = ['22-22-3636']
Time = ['22:22:22']
bikes = 100
cars = 250
bicycles = 78


def main():
    global bikes, cars, bicycles
    while True:

        print("-------------------------------------------------------------------------------------------------------")
        print("Parking Management System ")
        print("-------------------------------------------------------------------------------------------------------")
        print("1.Vehicle Entry ")
        print("2.Remove Entry ")
        print("3.View Parked Vehicle ")
        print("4.View Left Parking Space ")
        print("5.Amount Details ")
        print("6.Bill")
        print("7.Close Programme ")

        print("-------------------------------------------------------------------------------------------------------")
        ch = int(input("Select option:"))
        if ch == 1:
            typee = True
            while typee == True:
                text_speech.say("Please enter the type of vehicle ")
                text_speech.runAndWait()
                Vtype = str(
                    input("Enter vehicle type(Bicycle=A/Bike=B/Car=C): ")).lower()
                if Vtype == "":
                    text_speech.say("Enter a valid option")
                    text_speech.runAndWait()
                    print("###### Enter Vehicle Type ######")
                elif Vtype == "a":
                    Vehicle_Type.append("Bicycle")
                    bicycles -= 1
                    typee = not True
                elif Vtype == "b":
                    Vehicle_Type.append("Bike")
                    bikes -= 1
                    typee = not True
                elif Vtype == "c":
                    Vehicle_Type.append("Car")
                    cars -= 1
                    typee = not True
                else:
                    text_speech.say(" Enter a Valid Option ")
                    text_speech.runAndWait()
                    print("###### Please Enter Valid Option ######")
            no = True
            while no == True:
                if Vtype == 'a':
                    Vno = '0000000000'
                else:
                    text_speech.say("Please enter your vehicle number")
                    text_speech.runAndWait()
                    Vno = input("Enter vehicle number  : ").upper()
                if Vno == "":
                    print("###### Enter Vehicle No. ######")
                elif Vno in Vehicle_Number:
                    print("###### Vehicle Number Already Exists")
                elif len(Vno) == 10:
                    no = not True
                    Vehicle_Number.append(Vno)
                else:
                    print("###### Enter Valid Vehicle Number ######")

            name = True
            while name == True:
                text_speech.say("Please Enter Vehicle Name")
                text_speech.runAndWait()
                vname = input("Enter vehicle name: ")
                if vname == "":
                    print("########Please Enter Vehicle Name ########")
                else:
                    Vehicle_Name.append(vname)
                    name = not True
            o = True
            while o == True:
                text_speech.say("Please Enter owner name")
                text_speech.runAndWait()
                OName = input("Enter owner name: ")
                if OName == "":
                    print("###### Please Enter Owner Name ######")
                else:
                    Owner_Name.append(OName)
                    o = not True
            d = True
            while d == True:
                date1 = date.today()
                Date.append(date1)
#                     date=input("Enter Date (DD-MM-YYYY) - ")
#                     if date=="":
#                         print("###### Enter Date ######")
#                     elif len(date)!=10:
#                         print("###### Enter Valid Date ######")
#                     else:
#                         Date.append(date)
                d = not True
            t = True
            while t == True:
                Time.append(datetime.now().strftime("%H:%M:%S"))
#                     time=input("Enter Time (HH:MM:SS) - ")
#                     if t=="":
#                         print("###### Enter Time ######")
#                     elif len(time)!=8:
#                         print("###### Please Enter Valid Date ######")
#                     else:
#                         Time.append(time)
                t = not True
                text_speech.say("Record detail saved. Thankyou for using our Service Have a nice day.")
                text_speech.runAndWait()
            print("\n.......................................Record detail saved..............................................")
        elif ch == 2:
            no = True
            while no == True:
                text_speech.say("Enter vehicle number to Delete")
                text_speech.runAndWait()
                Vno = input("Enter vehicle number to Delete: ").upper()
                if Vno == "":
                    print("###### Enter Vehicle No. ######")
                elif len(Vno) >= 4:
                    if Vno in Vehicle_Number:
                        i = Vehicle_Number.index(Vno)
                        Vehicle_Number.pop(i)
                        Vehicle_Type.pop(i)
                        Vehicle_Name.pop(i)
                        Owner_Name.pop(i)
                        Date.pop(i)
                        Time.pop(i)
                        no = not True
                        print(
                            "\n....................................Removed Sucessfully.........................................")
                    elif Vno not in Vehicle_Number:
                        print("###### No Such Entry ######")
                    else:
                        print("Error")
                else:
                    print("###### Enter Valid Vehicle Number ######")
        elif ch == 3:
            count = 0
            print("")
            print("----------------------------------------------------------------------------------------------------------------------")
            print("Parked Vehicle")
            myTable = PrettyTable(
                ["Vehicle No.", "Vehice type", "Vehicle Name", "Owner Name", "Date", "Time"])
            for i in range(len(Vehicle_Number)):
                count += 1
                myTable.add_row([Vehicle_Number[i], Vehicle_Type[i],
                                Vehicle_Name[i], Owner_Name[i], Date[i], Time[i]])
            print(myTable)
            # print("----------------------------------------------------------------------------------------------------------------------")
            # print("Vehicle No.          Vehicle Type          Vehicle Name          Owner Name          Date          Time")
            # print("----------------------------------------------------------------------------------------------------------------------")
            # for i in range(len(Vehicle_Number)):
            #     count += 1
            #     print(Vehicle_Number[i], "          ", Vehicle_Type[i], "            ", Vehicle_Name[i],
            #           "          ", Owner_Name[i], "          ", Date[i], "          ", Time[i])
            # print("----------------------------------------------------------------------------------------------------------------------")
            print("---------------------------------- Total Records - ",
                  count, "-------------------------------------------")
            # print("----------------------------------------------------------------------------------------------------------------------")
            print("")
        elif ch == 4:
            print("----------------------------------------------------------------------------------------------------------------------")
            print("Spaces Left For Parking")
            print("----------------------------------------------------------------------------------------------------------------------")
            print("Spaces Available for Bicycle - ", bicycles)
            print("Spaces Available for Bike - ", bikes)
            print("Spaces Available for Car - ", cars)
            print("----------------------------------------------------------------------------------------------------------------------")
        elif ch == 5:
            print("----------------------------------------------------------------------------------------------------------------------")
            print("Parking Rate")
            print("----------------------------------------------------------------------------------------------------------------------")
            print("*1.Bicycle      Rs20 / Hour")
            print("*2.Bike         Rs40/ Hour")
            print("*3.Car          Rs60/ Hour")
            print("----------------------------------------------------------------------------------------------------------------------")
        elif ch == 6:
            print("................................................... Generating Bill ..................................................")
            no = True
            while no == True:
                text_speech.say("Enter vehicle number to Delete")
                text_speech.runAndWait()
                Vno = input("Enter vehicle number to Delete: ").upper()
                if Vno == "":
                    print("###### Enter Vehicle No. ######")
                elif len(Vno) == 10:
                    if Vno in Vehicle_Number:
                        i = Vehicle_Number.index(Vno)
                        no = not True
                    elif Vno not in Vehicle_Number:
                        print("###### No Such Entry ######")
                    else:
                        print("Error")
                else:
                    print("###### Enter Valid Vehicle Number ######")
            print("Vehicle Check in time - ", Time[i])
            print("Vehicle Check in Date - ", Date[i])
            print("Vehicle Type - ", Vehicle_Type[i])
            inp = True
            amt = 0
            while inp == True:
                text_speech.say("Enter No. of Hours Vehicle Parked")
                text_speech.runAndWait()
                hr = input("Enter No. of Hours Vehicle Parked - ").lower()
                if hr == "":
                    print("###### Please Enter Hours ######")
                elif int(hr) == 0 and Vehicle_Type[i] == "Bicycle":
                    amt = 20
                    inp = not True
                elif int(hr) == 0 and Vehicle_Type[i] == "Bike":
                    amt = 40
                    inp = not True
                elif int(hr) == 0 and Vehicle_Type[i] == "Car":
                    amt = 60
                    inp = not True
                elif int(hr) >= 1:
                    if Vehicle_Type[i] == "Bicycle":
                        amt = int(hr)*int(20)
                        inp = not True
                    elif Vehicle_Type[i] == "Bike":
                        amt = int(hr)*int(40)
                        inp = not True
                    elif Vehicle_Type[i] == "Car":
                        amt = int(hr)*int(60)
                        inp = not True
            print(" Parking Charge: ", amt)
            ac = 18/100*int(amt)
            print("Add. charge 18 % : ", ac)
            print("-----------------------------------------------------------------------------------------------------")
            print("Total Charge : ", int(amt)+int(ac))
            print("-----------------------------------------------------------------------------------------------------")
            print(".......................................Thank you for using our service.............................................")
            text_speech.say("Thank you for your service")
            Vehicle_Number.pop(i)
            Vehicle_Type.pop(i)
            Vehicle_Name.pop(i)
            Owner_Name.pop(i)
            Date.pop(i)
            Time.pop(i)
            a = input("Press Any Key to Proceed - ")
        elif ch == 7:
            print(".......................................Thank you for using our service.............................................")
            print("                                     ***(: Bye Bye :)***")
            text_speech.say(
                "Thank you for using our service. Have a nice day.")
            text_speech.runAndWait()
            break
        else:
            print('Please Select correct option')


print(".............................................Welcome...................................................")
print("..............................................Hello....................................................")
text_speech.say("Welcome to our parking")
text_speech.runAndWait()
# if _name_ == "_main_":
#     main()
main()
