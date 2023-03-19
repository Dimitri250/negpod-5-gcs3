#!/usr/bin/python3
month = input("Enter the name of a month: ")

if month in ["January", "March", "May", "July", "August", "October", "December"]:
    days = 31
    print("The month of", month, "has", days, "days.")
elif month == "February":
    print("The month of February has 28 or 29 days, depends if it's a leap year.")
else:
    days = 30
    print("The month of", month, "has", days, "days.")
