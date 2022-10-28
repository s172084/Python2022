#!/usr/bin/env python3
import sys
import string 
import math
import re 

# SPECIAL NOTE:  QUESTIONS MUST BE RUN INDIVIDUALLY 

bright_cyan = "\033[0;96m"
bright_green = "\033[0;32m"
reset = "\033[0m\n"
bright_purple ="\033[0;35m" 

print("--------------------------------------------------------------------")
print("\U0001F33C Q1.\U0001F33C")
print("--------------------------------------------------------------------")

def reverse_complement_sequence(sequence):
    #Take a DNA sequence and return reverse complement
    
    translation_table = str.maketrans('ATCGN', 'TAGC*')
    
    return sequence.translate(translation_table)[::-1]
# --------------------------------------------------------------------")
accessions_header = []
dna_sequences = []

print("Usage: python3 python_program.py [file ...]")

try:
    infile = open(sys.argv[1], "r")
except IndexError as error:
    print(bright_purple + "Translation: Include the dna7.fsa file. ", reset)

line = infile.readline()

while line != "":
    
        if line.startswith(">"):
            accessions_header.append(line.strip() + bright_green+" ** REVERSE COMPLEMENT STRAND **"+reset)
            dna_sequences.append('')
            
        else:
            sequence = re.sub("\s", "", line)
            dna_sequences[-1] += sequence 
            
        line = infile.readline()
        
rev_comp_dna = list(map(lambda dna_sequences : reverse_complement_sequence(dna_sequences), dna_sequences))

outfile = open("reverse_complement_dna.fsa", "w")

for acc, deena in zip(accessions_header, rev_comp_dna):
    print(acc, end="", file = outfile)
    print(acc, end="")
    for i in range(0,len(deena),60):
        print(deena[i:i + 60], file = outfile)
        print(deena[i:i + 60])

infile.close()
outfile.close()

print("--------------------------------------------------------------------")
print("\U0001F33C Q2.\U0001F33C")
print("--------------------------------------------------------------------")

def find_the_factorial(number):
    '''Calculate the factorial'''
    if number == 0:
        return 1
    if number <= -1:
        return bright_cyan +"The factorial is calculated for positive numbers only.\n"+reset
    else:
        return number * find_the_factorial(number - 1)
        
print(find_the_factorial(100))
print(find_the_factorial(-20))

print("--------------------------------------------------------------------")
print("\U0001F33C Q3.\U0001F33C")
print("--------------------------------------------------------------------")

codon = {"ATT" :"I", "ATC": "I", "ATA":"I", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "TTA":"L", "TTG":"L", 
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "TTT":"F", "TTC":"F", "ATG":"M", "TGT":"C", "TGC":"C",
    "GCT":"A","GCC":"A", "GCA":"A", "GCG":"A", "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G", "CCT":"P", 
    "CCC":"P", "CCA":"P", "CCG":"P", "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S", "TAT":"Y", "TAC":"Y", "TGG":"W", "CAA":"Q", "CAG":"Q", 
    "AAT":"N", "AAC":"N", "CAT":"H", "CAC":"H", "GAA":"E", "GAG":"E", "GAT":"D", "GAC":"D", "AAA":"K", "AAG":"K", 
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", "TAA":"Stop", "TAG":"Stop", "TGA":"Stop"}

# Find every 3 letters in the string. 
# Apply the dictionary to every triplet in the list. 

def perform_translation(s):
    ''' Find codons/triplets in a string and return the corresponding aa.'''
    codon_list = re.findall('...?', s)
    
    return "".join([codon.get(aa) for aa in codon_list])

# Test it
print(perform_translation("ATGATGATGATGATGATGATGATGATGATGATG"))

print("--------------------------------------------------------------------")
print("\U0001F33C Q4.\U0001F33C")
print("--------------------------------------------------------------------")
import statistics 

# 1. Search for numbers in the lines of the file. 
# 2. Append the numbers to a list. 
# 3. Change all of the strings into floats 
# 4. Calculate the standard deviation and variance. 

list_of_nums = []

try: 
    infile = open(sys.argv[1], 'r')
except IndexError as error:
    print(bright_purple + "Translation: Include the ex1.dat file. ", reset)
    sys.exit(1)

for line in infile:
    list_of_nums += re.findall(r'(-?\d+\.\d+)', line)

infile.close()

whole_file_numbers = list(map(float, list_of_nums))

# Two pass solution 
print("The variance             : ", statistics.pvariance(whole_file_numbers))
print("The standard deviation   : ", statistics.pstdev(whole_file_numbers))

print("--------------------------------------------------------------------")
print("\U0001F33C Q4.\U0001F33C Alternative Solution")
print("--------------------------------------------------------------------")

def calc_variance_and_standard_deviation(a):
    '''A function to calculate the variance and standard deviation'''
    
    list_of_squares = []
    
    for i in a:
        list_of_squares.append(math.pow(i -  (1/int(len(a)) * sum(a)), 2))
        
    variance = ((1/(len(a)-1)) * sum(list_of_squares))
    standard_deviation = math.sqrt(((1/(len(a)-1)) * sum(list_of_squares)))
    
    return ("The variance             : " + f"{variance}" +"\n"+ 
            "The standard deviation   : "+ f"{standard_deviation}")
            
# One pass solution 
print(calc_variance_and_standard_deviation(whole_file_numbers))

print("Perhaps the values are different due to rounding errors above.")


print("--------------------------------------------------------------------")
print("\U0001F33C Q5.\U0001F33C")
print("--------------------------------------------------------------------")
# Create a dictionary called noted occurrence in order to note the occurrence of the accession. 
# Remove nnewline characters from the accession. 
# Add 1 next to the accession number if the accession is present 
# If the accession number is there again, add another 1
# Sort the accession numbers based on the number of times they occur. 

print("python3 python_program.py [file ...]")

try:
    infile = open(sys.argv[1], 'r')
except IndexError as error:
    print(bright_purple + "Translation: Include the ex5.acc file. "+ reset)
    sys.exit(1)

noted_occurrence= {}

for line in infile:
    accession_name = line.strip()
    
    if accession_name in noted_occurrence:
        noted_occurrence[accession_name] += 1
    else:
        noted_occurrence[accession_name] = 1
        
infile.close()

for accession in sorted(noted_occurrence, key = noted_occurrence.get, reverse = True):
    print(f"{accession}, {(noted_occurrence[accession])}")
    
print("\U0001F33B","by Miss Oriade Latifah Simpson, Thursday 27 October 2022" ,"\U0001F4BB")