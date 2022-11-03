#!/usr/bin/env python3
#--------------------------------------------------------------------
import statistics 
import re 
import sys

print("# --------------------------------------------------------------------")
print(" Dictionary of lists and matrix transposition.")
print("# --------------------------------------------------------------------")

reset = "\033[0m\n"
bright_cyan = "\033[0;96m"

print("# --------------------------------------------------------------------")
print(" \U0001F33C Q1. \U0001F33C")
print("# --------------------------------------------------------------------")

relational_book = {}

try:
    
    infile = open("test3.dat", "r")
    
except IOError as error_ag:
    print(bright_cyan + "There is a minor problem with opening the file:", str(error_ag) + reset)
    sys.exit(1)

for line in infile:
    accession_with_numbers = line.split()  
    
    accession_name = accession_with_numbers[0]
    corresponding_numbers =accession_with_numbers[1:]
    
    if accession_name in relational_book:
        relational_book[accession_name] += round(statistics.mean(list(map(float,corresponding_numbers))),2)
    else:
        relational_book[accession_name] = round(statistics.mean(list(map(float,corresponding_numbers))),2)

for acc in relational_book:
    print("Accession number {}, Mean Value:{}".format(f"{acc}", f"{relational_book[acc]}"))
    
infile.close()

print("# --------------------------------------------------------------------")
print(" \U0001F33C Q2. \U0001F33C")
print("# --------------------------------------------------------------------")
# 1. Read a file into a list of lists.
# 2. Transpose
# 3. Print the output
#--------------------------------------------------------------------
def transpose(s):
    ''' A function to transpose square matrices.'''
    o = list(zip(*s))
    res = [' '.join(i) for i in o]
    return res
#--------------------------------------------------------------------

try:
    
    infile =open(sys.argv[1], "r")
    
except IndexError as error_idx:
    print(bright_cyan + "Use the command line on your terminal to run the program.\n" + str(error_idx))
    print("Usage: python3 python_program.py [filename]"  + reset)
    sys.exit(1)
    
except IOError as error_ag:
    print(bright_cyan + "There is a minor problem with opening the file:", str(error_ag) + reset)
    sys.exit(1)

# --------------------------------------------------------------------"
M = []
print("ORIGINAL MATRIX:")

for line in infile:
    print(line, end = "")
    
    line_values = line.strip('{}\n\r').split(" ") # create a list of lists
    M.append(line_values)

rows = int(len(M))
cols = int(len(M[0]))
# How many rows and columns are in the matrix? 
# --------------------------------------------------------------------"
# SQUARE MATRICES (M)

Transposed = []
    
if rows == cols:
    Transposed = transpose(M)
    print("TRANSPOSED MATRIX:")
    
for digit in Transposed:
    print("".join(digit))
    
infile.close()

#--------------------------------------------------------------------
# RECTANGULAR MATRICES (N)
N = []

if rows != cols:
    infile = open(sys.argv[1], "r")
    
    for line in infile:
        line_values = line.strip('{}\n\r').split("\t")  # create list of lists
        
        N.append(line_values)
        
infile.close()

#--------------------------------------------------------------------
# Convert the data from the file into integers rather than strings. 
# Transpose the lists
# Make a list of tuples into list of strings. 

capture = []
i = 0

while i < len(N):
    capture.append(list(map(int,N[i])))    
    i +=1
    
stacks = list(zip(*capture))

if rows != cols:
    print("\nTRANSPOSED MATRIX")
    
for sublist in stacks:
    result = ' '.join(str(numbr) for numbr in sublist)
    
    print(result)
    
print("\U0001F33B","by Miss Oriade Latifah Simpson, Thursday 3 November 2022" ,"\U0001F4BB")