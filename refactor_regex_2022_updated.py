#!/usr/bin/env python3
# --------------------------------------------------------------------
import sys
import re
import collections 
'''
# NOTE: RUN EACH QUESTION INDIVIDUALLY. 
bright_green = "\033[0;32m"
reset = "\033[0m\n"
bright_cyan = "\033[0;96m"
bright_purple = "\033[0;35m"  

print("# --------------------------------------------------------------------")
print("Q1:")

# 1. The string will be split into two groups.
# 2. Extract the parts that give an integer or float.
# A. Regular Expression Translation: There may or may not be a subtraction sign before one or more digits.
# B. In the second group there is a decimal point followed by one or more digits.
# C. The second group may or may not be present, but it comes at the end. 
try: 
    my_numb = input("Enter a number:> ").strip()
    
    if my_numb == "":
        raise ValueError(bright_green+ "* There was no input *"+ reset)

except ValueError as error:
    print("Error :>", str(error))
else:
    print("** "+ my_numb +" **")
try:
    result = re.search('^(-?\d+)(\.\d+)?$', my_numb)
    
    if result is None:
        raise AttributeError(bright_green+ "* That is not a valid number *" + reset)
        
except AttributeError as Aerror:
    print("Error :>", str(Aerror))
else:
    print(result.groups(0))

print("# --------------------------------------------------------------------")
print("Q2:")

print("usage: python3 python_program.py [file ...]")
outfile = open("sprot.fsa", "w")

try:
    with open(sys.argv[1], "r") as infile:
         for line in infile:
            
            match_one = re.search('(^ID)\s+(\w+)\s+(\w+).\s+(\w+).\s+(\d+)\s+\w+', line)
            if match_one:
                print("The swiss_prot_id is: ", match_one[2])
                print(">"+ match_one[2], file = outfile, end = "")
                
            match_two = re.search('AC\s+(\w+)[;]', line)
            if match_two:
                print("The accession number is:", match_two[1])
                print(" " +match_two[1], file = outfile)
                
except IndexError as error:
    print(bright_purple + "Translation: Include the sprot1.dat file. ", reset)
    sys.exit(1)

with open(sys.argv[1], "r") as infile:
       for line in infile:
            
            match_three = re.search('(SQ)\s+(\w+)\s+(\d+)\s+(\w+)[;]\s+\d+\s+(\w+)[;]\s+(\w+)\s+(\w+)([;])(.+)', 
                infile.read()[1750:2750], re.DOTALL)
            
            if match_three:
                polypeptide_sequence = re.sub("//", "", match_three[9])    
                print("The polypeptide sequence is", polypeptide_sequence)
                sentence = re.sub("\s+", "",polypeptide_sequence)
                print("The number of amino acids recorded in the file:", match_three[3])
                
                for aa in range(0,len(sentence),60):
                    print(sentence[aa:aa + 60], file = outfile)
                    
# --------------------------------------------------------------------
# Verification of sequence length.
try:
    
    if int(match_three[3]) != len(sentence):
        raise ValueError("The number recorded in the SQ line is a mismatch to \n",
              "the number of amino acids in the actual sequence. See filename:",infile.name)
                
except ValueError as error:
    print("Error Message Translation :\n", bright_green + str(error)+ reset)
else:
    print(bright_purple + "The number recorded in the SQ line matches the number of amino acids in the actual sequence." + reset, end = "")
finally:
    print(bright_purple + "Please, continue to view the other questions.", "\U00002615"+ reset, end = "")

outfile.close()

print("# --------------------------------------------------------------------")
print("Q3:")

# PSEUDOCODE
# Make a list for the accssions and make an empty list of strings for the sequences. 
# read one line of DNA (only the first line and remove whitespace. 
# major point: push the string into the list at the end in order to join the DNA seequences of 1 accession. 
# reverse complement the list of strings using a lambda function and translation table. 
# Write the sequences to a file called rev_dna.fsa

print("usage: python3 python_program.py [file ...]")

try:
    infile = open(sys.argv[1], "r")
except IndexError as error:
    print(bright_purple + "Translation: Include the dna7.fsa file. ", reset)
    sys.exit(1)
    
    
outfile = open("reverse_complement_dna.fsa", "w")

accessions_header = collections.deque([])
dna_sequences = collections.deque([])

line = infile.readline()

while line != "":

        if line.startswith(">"):
            accessions_header.append(line.strip() + bright_green+" ** REVERSE COMPLEMENT STRAND **"+reset)
            dna_sequences.append('')
            
        else:
            sequence = re.sub("\s", "", line)
            dna_sequences[-1] += sequence 
            
        line = infile.readline()
    
# print(sequence)
# print(dna_sequences)
    
translation_table = str.maketrans('AGTC', 'TCAG')

rev_comp_dna = list(map(lambda dna_sequences : dna_sequences[::-1].translate(translation_table), dna_sequences))

for acc, deena in zip(accessions_header, rev_comp_dna):
    print(acc, end="", file = outfile)
    print(acc, end="")
    for i in range(0,len(deena),60):
        print(deena[i:i + 60], file = outfile)
        print(deena[i:i + 60])
        
infile.close()
outfile.close()

print("# --------------------------------------------------------------------")
print("Q4-5:")

# (?<=...) # Positive Lookbehind Assertion and  .+ match all characters 1 or  more times

re_list = [
    # DEFINITION
    r'(?<=NITION\s{2})(.+)', 
    
    # ACCESSION
    r'(?<=[A-Z]{9}\s{3})(.+)',
     
    # ORGANISM 
    r'(?<=NISM\s{2})(.+)'
]

wanted_information = []

try: 
    infile = open(sys.argv[1], "r")

except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
    
    
line = infile.readline()

while line != "":
    
    for regular_expression in re_list:
        wanted_information += re.findall(regular_expression, line)
    
    line = infile.readline()
    
infile.close()

print("Definition:", wanted_information[0])
print("Accession:", wanted_information[1])
print("Organism:", wanted_information[2])

print("# --------------------------------------------------------------------")
print("Q6:")

print("MEDLINE ARTICLE NUMBER:")

re_list = [ 
    
    r'(\s{2}MEDLINE\s+)(?P<article_number>\d+)'
]

try: 
    infile = open(sys.argv[1], "r")
    
except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
    
line = infile.readline()

while line != "":
    
    for regular_expression in re_list:
        result = re.search(regular_expression, line)
        
        if result is not None:
            print(result["article_number"])
        
    line = infile.readline()
    
infile.close()

print("# --------------------------------------------------------------------")
print("Q7:")

print("TRANSLATED STRAND:")

data = ''
flag = False

try:
    with open("data2.gb", "r") as infile:
        for line in infile:
            
            second_result = re.search(r'(?<=\s{5})exon', line)
            if second_result is not None: 
                flag = False
                
                
            result = re.search(r'(?<=/translation=\")(.+)', line)
            if result is not None:
                
                flag = True
                
            if flag is True:
                data += line.strip()[:-1]
                
                
                
except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
    
    
print(data)

print("# --------------------------------------------------------------------")
print("Q8:")

print("DNA SEQUENCE:")

deena_seq = ''
flag = False


try:
    
    with open(sys.argv[1], "r") as infile:
        for line in infile:
            
            second_result = re.search(r'//', line)
            if second_result is not None: 
                flag = False
                
            if flag is True:
                deena_seq += line 
                
            result = re.search(r'ORIGIN' , line)
            if result is not None:
                flag = True
            
except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
                    
        	
uppercase_DNA = deena_seq.upper()

# remove digits from DNA
nodigits_DNA = re.sub(r'[0-9]+', '', uppercase_DNA)
#print(nodigits_DNA)

# remove spaces from DNA
nospaces_DNA = re.sub(r' ', '', nodigits_DNA)
print(nospaces_DNA)
''' 
print("# --------------------------------------------------------------------")
print("Q9")

re_list = [ 
    
    r"^\s+CDS\s+join\((.+)"
]
# --------------------------------------------------------------------
try: 
    infile = open(sys.argv[1], "r")
    
except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
# --------------------------------------------------------------------
line = infile.readline()

exonsflag = False
exons = ""

while line != "":
    
    coding = re.search(r"^\s+CDS\s+join\((.+)",line)
    
    if coding is not None:
        exons += coding.group(1).strip()
        
        if line[-2] != ")":
            exonsflag = True
            
    elif exonsflag:
        exons += line.strip()[:-1]
        
        if line[-2] == ")":
            exonsflag = False
            
            
    line = infile.readline()
    
# Make it into a list. 
EXONS = exons[:-1].split(",")

infile.close()

# --------------------------------------------------------------------
flag = False
deena_seq = []

with open(sys.argv[1], "r") as infile:
    
    for line in infile:
        second_result = re.search(r'//', line)
        
        if second_result is not None: 
            flag = False
            
        deena_seq.append('')
        
        if flag is True:
            # Read in the entire string without digits, newlines or spaces.  
            deena_seq[-1] = re.sub(r'\s+', '',line.upper(), re.MULTILINE| re.DOTALL)
            deena_sequence = re.sub(r'\d+', '',''.join(deena_seq))
            
        result = re.search(r'ORIGIN' , line)
        if result is not None:
            flag = True

# --------------------------------------------------------------------
# Extract the string from one index to the next using this for loop and string addition. 
coding_sequence = ""

for val in EXONS:
    
    positions = val.split(r"..")
    
    the_start = int(positions[0]) - 1
    the_end = int(positions[1])
    
    coding_sequence += deena_sequence[the_start:the_end]
    print("Coding DNA sequence:")
for i in range(0, len(coding_sequence), 60):
    print(coding_sequence[i:i+60])    
# --------------------------------------------------------------------
def str_list_to_int_list(str_list):
    # Convert the strings in a list into integers in a list.
    n = 0
    while n < len(str_list):
        str_list[n] = int(str_list[n])
        
        n += 1
        
    return(str_list)
# --------------------------------------------------------------------