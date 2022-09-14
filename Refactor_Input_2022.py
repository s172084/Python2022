#!/usr/bin/env python3
import sys
import math 
import os 
import statistics

# NOTE: The questions will need to be run individually.

print("# --------------------------------------------------------------------")
print("Q1.")
# Read in the numbers using sys. 

print("Can I have two numbers?")

number1 = sys.stdin.readline()
number2 = sys.stdin.readline()

sys.stdout.write("The mean is: ")
answer = statistics.mean([float(number1), float(number2)])

the_mean = int(answer)  
sys.stdout.write(str(the_mean)+ "\n")

print("# --------------------------------------------------------------------")
print("Q2.")
print("command : python3 pythonfile.py  < twonumbers.txt")
# Take input from the file via unix
count = None
my_total  =  0 

line = sys.stdin.readline()

while line != "":
    print(line) 
    count = int(line)
    my_total = my_total + count 
    
    my_mean = my_total / count
    line = sys.stdin.readline() 
    
print("The sum is:", my_total)
print("The count is:", count)
print("The mean is:", my_mean)

print("# --------------------------------------------------------------------")
print("Q3")
print("command: python3 pythonfile.py < ex1.dat")

# Take input from the file via unix
# count all - signs and add them together. 

minus_signs = 0 

line = sys.stdin.readline()

while line != "":
    minus_signs += line.count("-")
    line = sys.stdin.readline() 
        
print("The number of the negative values in the file are :", minus_signs)		

print("# --------------------------------------------------------------------")
print("Q4.")

temperature = input("Enter a temperature in Fahrenheit or Celsius e.g. 80F or 30C:> ")

my_temp = int(temperature[:-1])

if temperature[-1] == "F":
    celsius = (my_temp - 32)*(5 / 9)
    print("The temperature in Celsius is :", round(celsius, 3), " Celsius.")
elif temperature[-1] == "C":	
    fahrenheit = (my_temp * 9/5) + 32 
    print("The temperature in Fahrenheit is:", round(fahrenheit, 3))

print("# --------------------------------------------------------------------")
print("Q5.")

infile = open("orphans.sp", "r")
outfile = open("accession.txt", "w")
    
for line in infile:
    if line.startswith('>'):
        accession_line = line                  # save the lines with accession numbers 
        accession = accession_line[0:16]       # Slice the string to get accessions only.
        print(accession, file = outfile)
infile.close()
outfile.close()

print("The new file is called accession.txt")

print("# --------------------------------------------------------------------")
print("Q6")
# PSEUDOCODE
# Ask for two filenames
# Read the files
# Add each string together so they display one line, for all the lines. 
# write the data to a new file called ex1tot.txt
# close the file handles. 
print("command: python3 pythonfile.py ex1.acc ex1.dat")

infile_1 = sys.argv[1]
infile_2 = sys.argv[2]

infile_one= open(infile_1 , 'r')
infile_two= open(infile_2 , 'r')
outfile = open("ex1tot.txt", 'w')

for line1 in infile_one:
    for line2 in infile_two:
        my_line = str(line1[0:-1])+ "\t"+ str(line2[0:])
        print(my_line, file = outfile, end = " ")
        
infile_one.close()
infile_two.close()
outfile.close()

print("The new file is called ex1tot.txt")

print("# --------------------------------------------------------------------")
print("Q7")
print("command: python3 pythonfile.py dna.dat")
# Put the DNA in a string variable
# This static method returns a translation table using the str library. 
# Return a copy of the string in which each character has been mapped through agiven translation table.

infile_1 = sys.argv[1]  
infile_one= open(infile_1 , 'r')

the_DNA = ""

for line in infile_one:
        the_DNA += line
        
print("The Original DNA:")
print(the_DNA, end = "\n")

translation_table = str.maketrans('ATCGN', 'TAGC*')
complement_dna = the_DNA.translate(translation_table)

print("The Complement DNA:")
print(complement_dna)

print("# --------------------------------------------------------------------")
print("Q8")

# Reverse the string to create the reverse complement.
print("The Reverse Complement:")
reverse_complement = complement_dna[::-1]
print(reverse_complement) 

print("# --------------------------------------------------------------------")
print("Q9")
rev_outfile = open("revdna.dat", 'w')

# straight up write the variable to a file. 
print(reverse_complement, file = rev_outfile)
print("The new file is called revdna.dat")

rev_outfile.close()
infile_one.close()

print("# --------------------------------------------------------------------")
print("Q10")

the_dna = ""

infile_one= open(sys.argv[1] , 'r')
outfile_one = open("revdna.fsa", "w")

for line in infile_one:
    if line.startswith(">"):
        print(line.strip("\n") + " Complementary_Strand", file = outfile_one)
    else:
        the_dna += line
        
translation_table = str.maketrans('ATCGN','TAGC*')
complement_dna = the_dna.translate(translation_table)
print(complement_dna, file = outfile_one)
print("Reverse Complement Strand:>", file = outfile_one)
reverse_complement = complement_dna[::-1]
print(reverse_complement, file = outfile_one)
infile_one.close()
outfile_one.close()

print("The complementary strand is in revdna.fsa")

print("# --------------------------------------------------------------------")
print("Q11")

last_dna = ""

infile_one= open(sys.argv[1] , 'r')

for line in infile_one:
    if line.startswith(">"):
        pass
    else:
        last_dna += line        
print("Adenine = ", last_dna.count("A"))
print("Cytosine =", last_dna.count("C"))
print("Guanine = ", last_dna.count("G"))
print("Thymine = ", last_dna.count("T"))

infile_one.close()

print("# --------------------------------------------------------------------")
print("Q12")

for i in range(10):
    print("+" * 20)
    
print("# --------------------------------------------------------------------")
print("By Miss Oriade Latifah Simpson s172084@dtu.dk (Wednesday 14 September 2022")