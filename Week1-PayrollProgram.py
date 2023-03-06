#Morrese Morrison
#Creation Date 1/15/2022
#The purpose of this program is to calculate the gross pay
#based off of the user's payrate and hours worked.
#The user will enter both their Payrate and Hours Worked as integer variables.
#Both of these values will then be multiplied to calculate the user's gross pay.
#Note:

#Importing 3 Modules1
import sys
import os
import time

#Restart function. This will run when the user inputs an incorrect value into the payroll calculator.
def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

#Part 1 = Asking for hours worked. Can not exceed 40 Hours. Program will restart of the input is incorrect.
print("Welcome to the Pierce College company payroll calculator")
hoursworked = float(input("(Only Enter Numbers) How many hours did you work this week? : "))
if hoursworked >= 41:
        print("Nobody is working overtime. Please enter an amount less than or equal to 40 Hours")
        restart_program()

#Part 2 - Asking for Payrate. Can not exceed $20.00. Program will restart of the input is incorrect.
else:
        payrate = float(input("(Only Enter Numbers) What is your payrate? : "))
        if payrate >= 21:
                print("No one is earning more than $20.00 per hour. Please enter an amount less than or equal to $20")
                restart_program()

#Part 3 - Calculating Gross Pay. "payrate" input will be multiplied by "hoursworked" input.
#That value will be stored in the "grosspay" variable. That value will be printed out.
#Formatted the gross pay to only 2 decimal points.
        else:
                grosspay = payrate * hoursworked
                grosspay = "{:.2f}".format(grosspay)

#Calculation timer is set to three seconds.
                print("Calculating Please Wait...")
                time.sleep(5)
                print("Your gross pay is $",grosspay,"Dollars")
                answer = int(input("Do you want to restart this program ? Enter the number 1 if you do."))
                if answer == 1:
                        restart_program()
                else:
                        print("Goodbye")
