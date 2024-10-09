
# A certain cinema currently sells tickets for a full price of 6 pounds,
# but always sells tickets for half price to people who are less than 16 years old, and
# for a third of the price for people who are 60 years old or more.
# An example run of the program (numbers in bold are typed in by the user) Enter your age: 63 Your ticket costs £2

# age = int(input("Enter your age:"))
# if age < 16:
#     print("Your ticket price is £3 ")
# elif age >=60:
#     print("Your ticket price is £2 ")
# else:
#     print("Your ticket price is £6")

age = int(input("Enter your age:"))
full_price=6
if age < 16:
    price_reduction = full_price // 2
elif age >= 60:
    price_reduction = full_price // 3
else:
    price_reduction = full_price
print(f"Your ticket price is £{price_reduction}")

#Write a Python program to receive 3 numbers from the user and print the greatest among them.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y and x > z:
    print("The greatest number is ",x)
elif y > x and y > z:
    print("The greatest number is ",y)
else:
    print("The greatest number is ",z)

#Find the factorial of a given number using loops(note the number is received from the user)

num = int(input("Enter a number: "))
f = 1
for i in range(1, num + 1):
    f = f * i
print(f"The factorial of {num} is {f}")

#Reverse a number using while loop

n = int(input("Enter a number : "))
r = 0
while n > 0:
    d = n % 10
    r = r * 10 + d
    n = n // 10
print(f"The reversed number is:{r}")

#Finding the multiples of a number using loop

num = int(input("Enter a number: "))
count = int(input("How many multiples do you want to see? "))

for i in range(1, count + 1):
    multiple = num * i
    print(multiple," ",end='')

#Write a program to print the inputted value as it is and break the loop if the value is 'done'.
# Example run of the program :hello there hello there :finished finished :done Done

while True:
    word = input("Enter a value (type 'done' to finish): ")
    print(word)
    if word == 'done' or word == 'Done' or word == 'DONE':
        break

# Write a program that prints the numbers from 1 to 20.
# But for multiples of three print "Fizz" instead of the number and for the multiple of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz"

for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i," ",end='')

# Write a program to print the following pattern:
#  5 4 3 2 1
#  4 3 2 1
#  3 2 1
#  2 1
#  1

n = 5
for i in range(n, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

