# Wifi Tree
# Jordan Williford
# 1/24/2025
# Wi-Fi Diagnostic Tree Programming Project
# SDEV 1200 
#

# Use comments liberally throughout the program.
# This code will ask the user a series of questions to determine the cause of internet issues
reply = ""
print("Reboot the computer and try to connect.")
#This will see if its the computer
reply = input("Did that fix the problem?")
if reply == "yes":
    print("Okay!")
elif reply == "no":
    print("Reboot the router and try to connect")
#This will see if it is the router
    reply = input("did that fix the problem?")
    if reply =="yes":
        print("Okay!")
    elif reply =="no":
        print("Make sure that all the cables are plugged in firmly on both the router and modem.")
#This will see if it is the cables
        reply = input("Did that fix the problem?")
        if reply =="yes":
            print("okay")
        elif reply == "no":
            print("Move the router to a new location and try to connect")
#This will see if it is the router location
            reply = input("Did that fix the problem?")
            if reply =="yes":
                print("okay")
            elif reply == "no":
                print("You might want to get a new router.")
# This will inform the user to get a new router