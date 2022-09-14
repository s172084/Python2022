#!/usr/bin/env python3
print("Q.1") 

with open("ex1.acc", 'r') as infile:
    for line in infile:
        print(line, end= " ")
        
print("# --------------------------------------------------------------------")
print("Q.2")	

filename = input("Please enter a filename via the keyboard >: ")

with open(filename, 'r') as infile_q2:
    for line in infile_q2:
        print(line, end = " ")
        
print("# --------------------------------------------------------------------")
print("Q.3")	

filename = input("Please enter the filename >: ")

print("The file entered is :", filename)
number_of_lines = 0

with open(filename, 'r') as infile_q3:
    for line in infile_q3:
        #number_of_lines = number_of_lines + 1
        number_of_lines +=1
        
print("There are", number_of_lines, "lines in this file", end= '\n')

print("# --------------------------------------------------------------------")
print("Q.4")	
# cut -f1 ex1.dat, cut -f2 ex1.dat, cut -f3 ex1.dat 
the_sum = 0

filename = input("Please enter the filename >: ")

with open(filename, 'r') as infile_q4:
    for line in infile_q4:
        the_sum = the_sum + float(line)
        #the_sum += float(line)
        
print("The sum of the numbers is :", the_sum)

print("# --------------------------------------------------------------------")
print("Q.5")

import statistics 

list_of_nums = []

filename_q5 = input("Please enter the filename >: ")

print("The file entered is :", filename_q5)

with open(filename_q5, 'r') as infile_q5:
    for line in infile_q5:
        list_of_nums.append(float(line))
        
print(statistics.mean(list_of_nums))

print("# --------------------------------------------------------------------")
print("Q.6")

positive_numbers = 0
negative_numbers = 0
zeroes = 0

filename_q6 = input("Please enter the filename >: ")

with open(filename_q6, 'r') as infile_q6:
    for line in infile_q6:
        number = float(line)
        if number > 0:
            positive_numbers +=1
        elif number == 0:				
            zeroes +=1
        elif number < 0:
            negative_numbers +=1
            
print("The number of the positive values in the file are :", positive_numbers)		
print("The number of the negative values in the file are :", negative_numbers)		
print("The number of the zeroes in the file are :", zeroes)	

print("# --------------------------------------------------------------------")
print("Q.7")

list_of_figs = []

filename = input("Please enter the filename >: ")

with open(filename, 'r') as infile:
    for line in infile:
        list_of_figs.append(float(line))
        
print("The maximum number is :",  max(list_of_figs))

print("# --------------------------------------------------------------------")
print("Q.8")

list_of_digits = []

filename = input("Please enter the filename >: ")

with open(filename, 'r') as infile:
    for line in infile:
        list_of_digits.append(float(line))
        
print("The minimum number is :",  min(list_of_digits))

print("# --------------------------------------------------------------------")
print("Q.9")

positive_count = 0
negative_count = 0
zero_count = 0

list_of_stats = []

filename = input("Please enter the filename >: ")

with open(filename, 'r') as infile:
    for line in infile:
        list_of_stats.append(float(line))
        number = float(line)
        if number > 0:
            positive_count+=1
        elif number == 0:
            zero_count+=1
        elif number < 0:
            negative_count +=1

lowest_number =  min(list_of_stats)
highest_number =  max(list_of_stats)
pos_numbers = positive_count
neg_numbers = negative_count
null_numbers = zero_count

print("The minimum is {} , The maximum is {} ".format(lowest_number, highest_number))
print("There are {} zeros, {} positive numbers and {} negative numbers in the file.".format(zero_count, negative_count,positive_count))

print("# --------------------------------------------------------------------")
print("Q.10")
# comments: 
# create a variable for a special word. 
# loop through 10 times to ask a question. 
# if create actions based on if the special word is yes, lower or higher
# finally answer the question and remember zero is not allowed 

wordx = None

for i in range(1,11):                                                       
    print("The number suggested is", i , ". Is that the number you thought of ? ")
    wordx = input("Enter yes, lower, or higher:> :")
    if wordx == "higher":
        continue
    if wordx == "yes":
        break
    elif wordx == "lower":
        if not (i > 1):
                print("The allowed range is from 1 to 10 !!!")
        else:
            i = i -1
            print("The number suggested is :", i)
        break
    
print("By Miss Oriade Latifah Simpson s172084@dtu.dk (Wednesday 7 September 2022)")