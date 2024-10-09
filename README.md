# PYTHON_CONDITIONAL_AND_LOOPING_STATEMENTS
A basic Python program that demonstrates fundamental concepts using conditional statements and loops.

1.Name your file: MonthNames.py Write a program that reads an integer value between 1 and 12 from the user and prints output the corresponding month of the year. An example run of the program (numbers in bold are typed in by the user) Enter the month: 3 Month 3 is March

months = [ "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December" ]

user_input = int(input("Enter the month (1-12): "))

if 1 <= user_input <= 12:

    print(f"Month {user_input} is {months[user_input - 1]}.")
    
else:

    print("Invalid month number. Please enter a number between 1 and 12.")

![Q1](https://github.com/user-attachments/assets/01700638-e3bc-441f-b431-80d9298dd7a7)

2.A certain cinema currently sells tickets for a full price of 6 pounds, but always sells tickets for half price to people who are less than 16 years old, and for a third of the price for people who are 60 years old or more. An example run of the program (numbers in bold are typed in by the user) Enter your age: 63 Your ticket costs £2.00 

age = int(input("Enter your age:"))

full_price=6

if age < 16:

    price_reduction = full_price // 2
    
elif age >= 60:

    price_reduction = full_price // 3
    
else:

    price_reduction = full_price
    
print(f"Your ticket price is £{price_reduction}")

![Q2](https://github.com/user-attachments/assets/9998f9e9-1097-4718-a7b1-7c44c2c63448)

3. Name your file: BodyMassIndex.py Write a program to calculate your BMI and give weight status. Body Mass Index (BMI) is an internationally used measurement to check if you are a healthy weight for your height.The metric BMI formula accepts weight in kilograms and height in meters: BMI= weight(kg)/height2(m2) BMI Weight Status Categories table BMI range - kg/m2 Category Below 18.5 Underweight 18.5 -24.9 Normal 25 - 29.9 Overweight 30 & Above Obese An example run of the program (numbers in bold are typed in by the user) Enter your weight in (kg): 75 Enter your height in (m): 1.70 Your BMI is: 25.95 You are in the “overweight” range.
   
user_weight = float(input("Enter your weight in (kg): "))

user_height = float(input("Enter your height in (m): "))

bmi = user_weight / (user_height ** 2)

if bmi < 18.5:

    weight_status = "Underweight"
    
elif 18.5 <= bmi < 25:

    weight_status = "Normal"
    
elif 25 <= bmi < 30:

    weight_status = "Overweight"
    
else:

    weight_status = "Obese"

print(f"Your BMI is: {bmi:.2f}")

print(f"You are in the “{weight_status}” range.")

![Q3](https://github.com/user-attachments/assets/42499e2b-8cf4-4b30-86c5-e98a0bae5def)

4. Write a Python program to receive 3 numbers from the user and print the greatest among them.
   
x = int(input("Enter first number: "))

y = int(input("Enter second number: "))

z = int(input("Enter third number: "))

if x > y and x > z:

    print("The greatest number is ",x)
    
elif y > x and y > z:

    print("The greatest number is ",y)
    
else:

    print("The greatest number is ",z)

![Q4](https://github.com/user-attachments/assets/06fb9eb8-a5ba-4ee5-9180-c90db430d4bd)

5. Find the factorial of a given number using loops(note the number is received from the user)
   
num = int(input("Enter a number: "))

f = 1

for i in range(1, num + 1):

    f = f * i
    
print(f"The factorial of {num} is {f}")

![Q5](https://github.com/user-attachments/assets/d56ebb94-f21e-4e7f-9770-46af0b2269dc)

6. Reverse a number using while loop
   
n = int(input("Enter a number : "))

r = 0

while n > 0:

    d = n % 10
    
    r = r * 10 + d
    
    n = n // 10
    
print(f"The reversed number is:{r}")

![Q6](https://github.com/user-attachments/assets/e69f7c8c-5a5b-4fb5-9eed-8e3d2003f476)

7. Finding the multiples of a number using loop
   
num = int(input("Enter a number: "))

count = int(input("How many multiples do you want to see? "))

for i in range(1, count + 1):

    multiple = num * i
    
   print(multiple," ",end='')

![Q7](https://github.com/user-attachments/assets/12b059a1-c03f-4fbe-8a35-dd7a7e9e400c)

8. Write a program to print the inputted value as it is and break the loop if the value is 'done'. Example run of the program :hello there hello there :finished finished :done Done
   
while True:

    word = input("Enter a value (type 'done' to finish): ")
    
    print(word)
    
    if word == 'done' or word == 'Done' or word == 'DONE':
    
        break

![Q8](https://github.com/user-attachments/assets/37b3e7f2-83c0-422d-b1d0-db097d7011ff)

9. Write a program that prints the numbers from 1 to 10. But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz"
    
 for i in range(1, 21):
 
    if i % 3 == 0 and i % 5 == 0:
    
        print("FizzBuzz")
        
    elif i % 3 == 0:
    
        print("Fizz")
        
    elif i % 5 == 0:
    
        print("Buzz")
        
    else:
    
        print(i," ",end='')

![Q9](https://github.com/user-attachments/assets/fb1837e8-6f8a-43e9-a6f4-b1f20b7692d5)

10. Write a program to print the following pattern:
    
 5 4 3 2 1 
 
 4 3 2 1 
 
 3 2 1
 
 2 1 
 
 1
 
n = 5

for i in range(n, 0, -1):

    for j in range(i, 0, -1):
    
        print(j, end=' ')
        
    print()

![Q10](https://github.com/user-attachments/assets/0e95cc70-dbb4-4acf-bf59-93e548a6282c)




















