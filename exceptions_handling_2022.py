#!/usr/bin/env python3
import sys
import re 
from datetime import date
now = date.today()
print(now)

print("# --------------------------------------------------------------------")
print("Q1.")

print("The Swiss Protein Database File is clearly understood.")

print("# --------------------------------------------------------------------")
print("Q2.")

# 1. Find the entire line with the ID details
# 2. find the index of the first space. This is 2 as ID takes index 0 and 1.  
# 3. Use a while loop and counter
#    Add 1 to the counter until the first none-space is reached.
#    (DK: Advance, EN: increase)
#    The while loop stops itself when reaching the first none-space.
# 4. Instantiate (create) a new counter using the previous counter + 1. 
# 5. Make a second while loop and add 1 to the new counter  until the first space is reached.
#    (DK: Advance, EN: increase)
# 6. The first space reached represents the end of the ID. 
# 7. Use the counters as indexes to slice the line with the swissprot details. 

# --------------------------------------------------------------------
bright_green = "\033[0;32m"
reset = "\033[0m\n"
bright_cyan = "\033[0;96m"
# --------------------------------------------------------------------
acc_number = None
swiss_prot_id = None
start = 0
stop  = 0
# --------------------------------------------------------------------
polypeptide_sequence = ""
flag = False
sentence  = ""
amino_number = ""
# --------------------------------------------------------------------

file_yo = input("Please enter the filename:> ")

try:
    infile = open(file_yo, "r")
except IOError as error_ag:
    print(bright_cyan + "There is a minor problem with opening the file:", str(error_ag) + reset)
    sys.exit(1)

for line in infile:	
    
    if "ID" in line and line.startswith("ID"):
        #print(line)
        start = 2  
        
        while line[start] == " ":
            start = start + 1
            #print("While Loop: At index", start, "The character is ", line[start])
        stop = start + 1
    
        while line[stop] != " ":
            stop = stop +  1
            #print("While Loop: At index", stop, "The character is ", line[stop])
            
        swiss_prot_id = line[start:stop]
        print(swiss_prot_id)
                
        print("# --------------------------------------------------------------------")
        print("Q3.")
        # 1. Look for the line containing AC
        # 2. Reset the start index
        # 3. Use the same method as previously, except using ; to stop the loop. 
        
    elif ";" in line and line.startswith("AC"):
        #print(line)
        start = 2
        
        while line[start] == " ":
            start = start + 1
            #print("While Loop: At index", start, "The character is ", line[start])
                
        stop = start + 1
        
        while line[stop] != ";":
            stop = stop +  1
            #print("While Loop: At index", stop, "The character is ", line[stop])
        
        acc_number = line[start:stop]
        print("Accession Number: ", acc_number)
        
        with open("sprot.fsa", "w") as outfile:
                print(">" + swiss_prot_id + " " + acc_number, file = outfile)
        
        print("# --------------------------------------------------------------------")
        print("Q4.")
        
        # If the flag is set to true, collect the data
        # Use a for loop to print out 60 letters per line. 
        
    if line[:2] == "//":
        flag = False 
    
    if flag is True:
        polypeptide_sequence += line.strip()
        sentence = re.sub("\s", "", polypeptide_sequence)
        
    if line[:2] == "SQ":
        flag = True 


for building_block in range(0,len(sentence),60):
    print(sentence[building_block:building_block + 60])
    
infile.close()

print("# --------------------------------------------------------------------")
print("Q5.")	

with open(file_yo, "r") as infile:
    
    for line in infile:
        if line[:2] == "SQ":
            start = 13  
            
            while line[start] == " ":
                start = start + 1
                #print("While Loop: At index", start, "The character is ", line[start])
            stop = start + 1
            
            while line[stop] != " ":
                stop = stop +  1
                #print("While Loop: At index", stop, "The character is ", line[stop])
                
            amino_number = line[start:stop]

print("The amino number is:", amino_number)
            
# --------------------------------------------------------------------
            
actual_number = len(sentence)
print("The actual number of amino acids in the sequence :", actual_number,"\n")

# --------------------------------------------------------------------
try:
    
    if int(amino_number) != actual_number:
        raise ValueError("The number recorded in the SQ line is a mismatch to the number of amino acids in the actual sequence. See filename:",infile.name)
        
except ValueError as error:
    print("Error Message Translation :\n", bright_green + str(error)+ reset)
else:
    print(bright_green + "The number recorded in the SQ line matches the number of amino acids in the actual sequence."+ reset)
finally:
    print(bright_green + "Question 5 complete", "\U00002615"+ reset)

    
print("# --------------------------------------------------------------------")
print("Q6.")	

# Use a for loop to write 60 characters per line from the polypeptide sequence 
with open("sprot.fsa", "a") as outfile:
    
    for building_block in range(0,len(sentence),60):
        print(sentence[building_block:building_block + 60], file = outfile)
        
print("\nsprot.fsa was written in FASTA format.\n")

print("# --------------------------------------------------------------------")
print("Q7.")

# Pseudocode:
# Turn the data type into one long string. 
# Find a function to use such as re.finditer
# Use the function on the string to get the indexes.

the_DNA = ""
try:
    with open("dna.fsa", "r") as infile:
        
        for line in infile:
            
            if line.startswith(">"):
                pass
            else:
                the_DNA += line
except IOError as error_dna:
    print(bright_cyan + "There is a minor problem with opening the file:", str(error_dna) + reset)
    sys.exit(1)
            
#print("The Original DNA:")
#print(the_DNA, end = "\n")

# Find the start index and the end index of ATG in the entire string.     
for methionine in re.finditer(r"ATG", the_DNA):
    print(methionine.start(), methionine.end(), methionine.group(0))
    
print("# --------------------------------------------------------------------")
print("Q8.")	

# Pseudocode:
# Get all DNA
# Run through the line figure out where the first atg is.
# Make a note of that position. 
# Now find the first position of the stop codon that is in frame. 
# Now i know where the stop codon is, i end my loop.
# Always take the first stop codon.
# Which one is the stop codon found. 

the_DNA = ""

with open("dna.fsa", "r") as infile:
    
    for line in infile:
        
        if line.startswith(">"):
            pass
        else:
            the_DNA += line
            
# Get all DNA, without spaces or newlines. 
DNA = re.sub("\s", "", the_DNA)

# What is the length of the DNA?
#print("The length of the DNA is:", len(DNA))


# Run through the line figure out where the first ATG is.
# Make a note of that position
i_pos = DNA.index("ATG")

i = i_pos

while DNA[i:i+3] != 'TAG':
    
    print(DNA[i:i+3])
    
    if DNA[i:i+3] == "TAA":
        print("The indexes of codon TAA are :", i, i+1, i+2)
        print(bright_green + "Warning: Codon Suppression" + reset)
        
    if [DNA[i:i+3]] == "TGA":
        print("The index of codon TGA are:", i, i+1, i+2)
            
    i = i + 3

print("# --------------------------------------------------------------------")
print("Q9.")

# Ask for input
# Find all lines containing the input
# count the number of lines containing the organism using a counter. 
orga_number = 0

orga = input("Enter HUMAN or RAT:")
try:
    assert orga == "HUMAN" or orga == "RAT", "The allowed input is 'HUMAN' or 'RAT' !"
    with open("orphans.sp", "r") as infile:
        
        for line in infile:
            
            if orga in line:
                orga_number += line.count(orga)
                
except IOError as error_orph:
    print(bright_cyan + "There is a minor problem with opening the file:", str(error_orph) + reset)
    sys.exit(1)
    
except AssertionError as err:
    print(bright_green + str(err) + reset)
    sys.exit(1)
    
print("There are", orga_number, "lines in the file containing:", orga)

print("# --------------------------------------------------------------------")
print("Q10.")	

# create a variable for the while loop to stop. 
# Use input to enter a variable. 
# Keep a record of attemps made (or variables entered)
# Allow the loop to flow using input for higher and lower. 
# Add assert statemeents to ensure rules for the game.
# raise errors for incorrect assertions and keys. 

starting_number = 3
unknown_word = None
attempts = 0

print("The number suggested is", starting_number, ". Is that the number you thought of ? ")
try:
    while unknown_word != "yes":
        
        unknown_word = input("Enter 'yes', 'lower', or 'higher':> :")
        
        if unknown_word:
            attempts = attempts + 1
        
        if unknown_word == "higher":
            starting_number = starting_number + 1
            assert starting_number > 0 and starting_number < 11, "The allowed range is from 1 to 10 !"
            print("The number suggested is", starting_number , ". Is that the number you thought of ? ")
            
        elif unknown_word == "lower":
            starting_number = starting_number - 1
            assert starting_number > 0 and starting_number < 11, "The allowed range is from 1 to 10 !"
            print("The number suggested is", starting_number, ". Is that the number you thought of ? ")
            
        elif unknown_word not in ["yes", "lower", "higher"]:
            raise LookupError("You did not enter the correct word.")
            
except LookupError as error:
    print("Exception Error Message:", bright_green + str(error) + reset)
    
except AssertionError as err:
    print(bright_green + str(err) + reset)
    
print("Attempt Number:", attempts)
print("The guess is:", starting_number)
    