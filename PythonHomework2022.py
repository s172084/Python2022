#!/usr/bin/env python3

print("# --------------------------------------------------------------------")
print("Q1:")
print("'Hello World'")

print("# --------------------------------------------------------------------")
print("Q2:")
for i in range(10):
    print("'Hello World'")

print("# --------------------------------------------------------------------")
print("Q3:")
for i in range(1,11):
    print(i)

print("# --------------------------------------------------------------------")
print("Q4:")
name = input("What is your name? ")
print(name,", nice to meet you. My name is Oriade Simpson and I study Bioinformatics at DTU")

print("# --------------------------------------------------------------------")
print("Q5:")
number1 = float(input("Please enter in a number: "))
number2 = float(input("Please enter another number: "))
the_total = number1 + number2
print("The sum of the two numbers entered is: ", int(the_total))

print("# --------------------------------------------------------------------")
print("Q6:")
num1 = float(input("Please enter a number:"))
num2 = float(input("Please enter a new number:"))
print("Which operation do you want to perform? , type (+, - , *, /) :")

the_operation = input()
if the_operation == '+' : 
    my_calc = num1 + num2
elif the_operation == '-':
    my_calc  = num1 - num2
elif the_operation == '/':
    my_calc = num1 / num2
elif the_operation == '*':
     my_calc = num1 * num2
else:
    print("The input is not recognised as a qualifying operator. Please enter + - * or / ")
print(num1, the_operation , num2, " is equal to ", int(my_calc), "\n")	

print("# --------------------------------------------------------------------")
print("Q7:")
print("I would like you to enter two integers and I shall print all integers in between them")
my_num1 = int(input("Please enter an integer: "))
my_num2 = int(input("Please enter an integer:"))
for i in range(my_num1 +1 , my_num2, 1):
    print(i)

print("# --------------------------------------------------------------------")
print("Q8:")
pint1 = int(input("Please enter an integer: "))
pint2 = int(input("Please enter a new integer: "))
print("The integers entered were :" , pint1, " and " , pint2)
print("The integers in between them are:")
if pint1 < pint2:
    smallest_number = pint1
    biggest_number = pint2
    
    for i in range(smallest_number+1, biggest_number, 1):
        print(i)
else:
    smallest_number = pint2	
    biggest_number = pint1	
    for i in range(smallest_number+1, biggest_number, 1):
        print(i)

print("# --------------------------------------------------------------------")
print("Q9:")

print("This program will stop if the number you enter is less than the previous number entered.")
for i in range(1,10):
    ent_num  = int(input("Enter a number e:"))
    print("The number you entered is: ", int(ent_num))
    second_num = int(input("Enter a number s:"))
    if second_num <=  ent_num :  
        print("The number you entered is: ", int(second_num))
        break
    else:
        third_num  = int(input("Enter a number e:"))
        print("The number you entered is: ", int(third_num))
        if third_num <= ent_num :
            break
        else:
            continue
print("# --------------------------------------------------------------------")
print("Q10:")

import math
positive_integer = int(input("Please enter a positive integer:"))
print("The value entered was :", positive_integer)

try:
    my_factorial_answer = math.factorial(positive_integer)
    print("The factorial of", positive_integer, "is", my_factorial_answer)
except(ValueError):		
    print("The value entered appears to be negative. Why not try a positive integer value ?")
    
print("# --------------------------------------------------------------------")
print("Q11:")
new_positive_integer = int(input("Please enter an integer: > "))
my_array = []
for i in range(0, new_positive_integer+1):
    my_array.append(i)
    result = 0
    for n in my_array:
        result += n
print("The sum of the numbers from 0 to", new_positive_integer, " is:", result)

new_negative_integer = int(input("Please enter a negative integer: > "))
my_minus_array = []

for i in range(0, new_negative_integer-1, -1):
    my_minus_array.append(i)
    neg_result = 0
    for p in my_minus_array:
        neg_result += p
print("The sum of the numbers from", new_negative_integer, "to 0 is:", neg_result)
print("By Miss Oriade Latifah Simpson s172084@dtu.dk (Thursday 1 September 2022)" )