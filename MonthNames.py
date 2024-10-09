
#Name your file: MonthNames.py
# Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year.
# An example run of the program (numbers in bold are typed in by the user) Enter the month: 3 Month 3 is March

months = [ "January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December" ]
user_input = int(input("Enter the month (1-12): "))
if 1 <= user_input <= 12:
    print(f"Month {user_input} is {months[user_input - 1]}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
