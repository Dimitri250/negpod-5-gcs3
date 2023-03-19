#!/usr/bin/env python3

# Days in months ranging from 28 to 31
month = input("Enter the name of a month: ")

if month == "January" or month == "March" or month == "May" or month == "July" or month == "August" or month == "October" or month == "December":
    print("The month of", month, "has 31 days.")
elif month == "April" or month == "June" or month == "September" or month == "November":
    print("The month of", month, "has 30 days.")
elif month == "February":
    print("The month of February has 28 or 29 days.")
else:
    print("Invalid month name. Please enter a valid month name.")
