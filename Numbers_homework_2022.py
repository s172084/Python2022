#!/usr/bin/env python3

# --------------------------------------------------------------------
import sys
import statistics
import re
# --------------------------------------------------------------------
brightish = "\033[0;36m"
reset = "\033[0m\n"
bright_purple = "\033[0;35m"  
# --------------------------------------------------------------------
# NOTE: QUESTIONS MUST BE RUN INDIVIDUALLY. 
print("--------------------------------------------------------------------")
print("Q1.")

print("Please enter a word.")
print("When you are finished write 'STOP'")

word = ""
with open("words.txt", 'w') as outfile:
    while word != 'STOP':
        word = input("Word:")
        outfile.write(word+"\n")
# --------------------------------------------------------------------
print("Q2.")
# Sort the words and reverse their order. Print to a file. 

wl = []

print("Please enter a word.")
print("When you are finished write 'STOP'")

word = ""
outfile = open("words.txt", 'w')
    
while word != 'STOP':
    word = input("Word:")
    wl.append(word)
        
sl = sorted(wl, key = str.lower)
print(sl)

rl = list(reversed(sl))
print(rl)

for i in rl:
    print(i, file = outfile, end= "\n")

outfile.close()

print("# --------------------------------------------------------------------")
print("Q3")
# put accessions in a set so they only appear once.
# Sort the accession numbes in alphabetical order.
# --------------------------------------------------------------------

infile = open("ex5.acc", "r")
number_of_lines = 0
set_of_accessions = set()

line = infile.readline()
while line != "":
        #print(line, end = "")
        number_of_lines += 1
        
        set_of_accessions.add(line)
    
        line = infile.readline()

infile.close()

sor_acc = sorted(set_of_accessions)
# --------------------------------------------------------------------

print("There are", number_of_lines, "lines in this file", end= '\n')
print("There are", len(set_of_accessions), "individual accessions in this file.", end= '\n')

outfile = open("clean.acc", 'w')

for i in sor_acc:
    print(i, file = outfile, end= "")

outfile.close()

print("# --------------------------------------------------------------------")
print("Q4.")

# using del or the pop method to eliminate duplicates.
# HINT: Keep one list and poop duplicates out of it instead of appending them into a new list.
# If you run into trouble imagine your code executed on the list: 1, 2, 2, 3, 3, 3, 4, 4, 4, 4
# --------------------------------------------------------------------

infile = open("ex5.acc", "r")
number_of_lines = 0
list_of_accessions = list()
# --------------------------------------------------------------------

line = infile.readline()
while line != "":
        #print(line, end = "")
        number_of_lines += 1
        
        list_of_accessions.append(line)
        
        line = infile.readline()
    
infile.close()

sor_acc = sorted(list_of_accessions)
# --------------------------------------------------------------------
outfile = open("clean_acc.txt", 'w')

i = 1

while sor_acc[i] != sor_acc[-1]:
    
    if sor_acc[i] == sor_acc[i+1]:
        while sor_acc[i] == sor_acc[i+1]:
            del sor_acc[i] 
    else:
        pass
        #print(sor_acc[i] , "and ", sor_acc[i], "are equal oh no!")
    
    # print to screen and to file. 
    print("The accession is", sor_acc[i], end = "")
    print(sor_acc[i], file = outfile, end= "")
    
    
    i = i + 1
    
outfile.close()

print("# --------------------------------------------------------------------")
print("Q5.")
# Read file clean.acc.
# Enter accession numbers.
# Are accession numbers in the list? Y/N
# Use while loop until STOP.
# perform linear search 

infile = open("clean.acc", "r")
list_of_accessions = list()
# --------------------------------------------------------------------

line = infile.readline()
while line != "":
        #print(line, end = "")
        
        list_of_accessions.append(line.strip())
    
        line = infile.readline()
    
print(list_of_accessions)

infile.close()
# --------------------------------------------------------------------

# Create a function to do a linear search.
def linear_search(longlist, wordx):
    
    for i in range(len(longlist)):
        
        if longlist[i] == wordx:
            return True
    return False
    
# --------------------------------------------------------------------
unknown_word = None

while unknown_word != "STOP":
    
    unknown_word = input("Enter accession number :> :")
    print("The accession entered:", unknown_word)
    
    if linear_search(list_of_accessions, unknown_word):
        print(brightish +"This accession number is present in the database"+ reset)
    else:
        print(bright_purple + "You did not enter a valid accession number" + reset)

print("# --------------------------------------------------------------------")
print("Q6.")

print("Binary Search is a searching algorithm used in a sorted array by repeatedly dividing the search interval in half.")
print("The idea of binary search is to use the information that the array is sorted and reduce the time complexity to O(Log n).")


infile = open("clean.acc", "r")
list_of_accessions = list()
# --------------------------------------------------------------------

line = infile.readline()
while line != "":
        #print(line, end = "")
    
        list_of_accessions.append(line.strip())
    
        line = infile.readline()
    
print(list_of_accessions)

infile.close()
# --------------------------------------------------------------------
# Give me good and thorough feedback on this question.
# 
print("# --------------------------------------------------------------------")
print("Q7.I")

print("usage: python3 [file ...]")
print("Find the average of numbers from a file.")

file_numbers = []
try:
    infile = open(sys.argv[1], "r")
except IndexError as error:
    print(bright_purple + "Translation: Include a file that contains numbers to calculate the mean: ", str(error), reset)
    sys.exit(1)

line = infile.readline()

while line != "":
    #print(line, end = "")
    
    file_numbers.append(int(line.strip()))
    
    # doing something with the line
    line = infile.readline() 
    
print("The mean of the numbers is:", statistics.mean(file_numbers), "\n")

# getting the next line
infile.close()

# --------------------------------------------------------------------
# The numbers are read in as strings
# They must be converted to integers before calculation

print("Enter a number:")
line1 = sys.stdin.readline()
inty_line1 = int(line1)

print("Enter a number:")
line2 = sys.stdin.readline()
inty_line2 = int(line2)

line_list = [inty_line1, inty_line2]

print("The mean of these numbers is:", statistics.mean(line_list))

print("# --------------------------------------------------------------------")
print("Q7. II")

print("usage: python3 [file ...]")

# Declare the variables. 
minus_signs = 0

try:
    infile = open(sys.argv[1], "r")
except IndexError as error:
    print(bright_purple + "Translation: Include a file that contains numbers: ", str(error), reset)
    sys.exit(1)
    
line = infile.readline()

while line != "":
    print(line, end = "")
    
    minus_signs += line.count("-")
    
    # doing something with the line
    line = infile.readline()
    
print("The file contains", minus_signs, "negative numbers.")

print("# --------------------------------------------------------------------")
print("Q8.")

# 20. cat ex1.tot | cut -f1,5 > ex1.res
print("usage: python3 [arg1] , [arg2] [file ...]")
# "Arg1: sys.argv[1] and Arg2: sys.argv[2]    

infile = open(sys.argv[3], "r")

line = infile.readline()

while line != "":

    #print(line, end= "")   
    data_list = line.split(sep = '\t')
        
    # Get arguments from the commmand line and subtract 1 to index properly
    input_number = int(sys.argv[1]) - 1  
    other_input_number = int(sys.argv[2]) - 1  
    
    # Turn the indexed lists into strings. 
    column_string = "".join(data_list[input_number])
    column_string2 = "".join(data_list[other_input_number])

    # print them next to each other in one string. 
    complete_string = column_string.strip() + "\t" + column_string2.strip() + "\n"
    print(complete_string, end ="")
    
    # doing something with the line
    line = infile.readline()
    
infile.close()

print("# --------------------------------------------------------------------")
print("Q9.")
# 1. Get arguments from the commmand line and subtract 1 to index properly
# 2. Print the row specified by the input and change string to a float. 
# 3. Calculate the result 

print("usage: python3 [arg1], [arg2], [arg3] [file ...]")

infile = open(sys.argv[4], "r")

line = infile.readline()

result_summary1 = 0
result_summary2 = 0
result_summary3 = 0

while line != "":
    
    #print(line, end= "")   
    data_list = line.split(sep = '\t')
    
    input_number = int(sys.argv[1]) - 1                       #*1
    other_input_number = int(sys.argv[2]) - 1  
    another_input_number = int(sys.argv[3]) -1
    
    col1_reading = float(data_list[input_number])             #*2
    col2_reading = float(data_list[other_input_number])
    col3_reading = float(data_list[another_input_number])
    
    result_summary1 = result_summary1 + col1_reading          #*3
    result_summary2 = result_summary2 + col2_reading
    result_summary3 = result_summary3 + col3_reading
    
    # doing something with the line
    line = infile.readline()

infile.close()

print("The sum of column1:", str(round(result_summary1,5)) + "\n"+
        "The sum of column 2:", str(round(result_summary2,5)) + "\n"+
        "The sum of column 3:",  str(round(result_summary3,5)))

print("# --------------------------------------------------------------------")
print("Q10.")
# Calculate the sum of all columns in the file.
# How many columns are there?

print("usage: python3 [file ...]")

entire_sum = []
infile = open(sys.argv[1], "r")

line = infile.readline()

while line != "":
    
    # How many columns are there? 
    columns_in_the_file = len(line.split())
    
    data_list = line.split(sep = '\t')
    
    for i in range(0, columns_in_the_file):
        entire_sum.append(float(data_list[i]))
        
        
    line = infile.readline()
    
infile.close()

print("There are", columns_in_the_file, "columns in the file")
print("The sum of all columns in the file is:", round(sum(entire_sum),4))
print("# --------------------------------------------------------------------")
# by Miss Oriade Latifah Simpson, Sunday 2 October 2022