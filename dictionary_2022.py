#!/usr/bin/env python3
import sys
import re
# -------------------------------------------------------------------
bright_green = "\033[0;32m"
brightish = "\033[0;36m"
bright_purple ="\033[0;35m" 
reset = "\033[0m\n"
bright_cyan = "\033[0;96m"
# -------------------------------------------------------------------
# NOTE: RUN EACH QUESTION INDIVIDUALLY. 
#print(bright_cyan+ "# NOTE: RUN EACH QUESTION INDIVIDUALLY." +reset)
'''
print("# --------------------------------------------------------------------")
print("Q1.")

codon = {"ATT" :"I", "ATC": "I", "ATA":"I", "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L", "TTA":"L", "TTG":"L", 
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V", "TTT":"F", "TTC":"F", "ATG":"M", "TGT":"C", "TGC":"C",
    "GCT":"A","GCC":"A", "GCA":"A", "GCG":"A", "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G", "CCT":"P", 
    "CCC":"P", "CCA":"P", "CCG":"P", "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T", "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S", "AGT":"S", "AGC":"S", "TAT":"Y", "TAC":"Y", "TGG":"W", "CAA":"Q", "CAG":"Q", 
    "AAT":"N", "AAC":"N", "CAT":"H", "CAC":"H", "GAA":"E", "GAG":"E", "GAT":"D", "GAC":"D", "AAA":"K", "AAG":"K", 
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AGA":"R", "AGG":"R", "TAA":"Stop", "TAG":"Stop", "TGA":"Stop"}

print("The dictionary is:\n", codon)

print("# --------------------------------------------------------------------")
print("Q2.")
# -------------------------------------------------------------------
# Ignore the last three codons in order not to include the stop codon. 
# translate each codon to a protein sequence. 
# -------------------------------------------------------------------

# Convert the codons in the string into amino acids using a dictionary
def perform_translation(s):
    
    aa_sequence = ""
    
    for i in range(0,len(s[:-3]),3):
        
        aa_sequence += codon[s[i:i+3]]
        
    return (aa_sequence)
# -------------------------------------------------------------------

# print("usage: python3 python_program.py [file ...]")
outfile = open("aa7.fsa", "w")
accessions_header = []
dna_sequences = []

try:
    infile = open(sys.argv[1], "r")
except IndexError as error:
    print(bright_purple + "Translation: Include the dna7.fsa file. " + reset)
    sys.exit(1)
    
line = infile.readline()

while line != "":
    
    if line.startswith(">"):
        accessions_header.append(line.strip() + bright_green +" ** Amino Acid Sequence **"+reset)
        dna_sequences.append('')
    else:
        sequence = re.sub("\s", "", line)
        dna_sequences[-1] += sequence 
    
    line = infile.readline()
    
infile.close()

# -------------------------------------------------------------------
#print(dna_sequences)

# Perform Translation of DNA sequences.
polypeptide_transformation = list(map(lambda dna_sequences : perform_translation(dna_sequences), dna_sequences))
#print(polypeptide_transformation)

for acc, pp in zip(accessions_header, polypeptide_transformation):
    print(acc, end="", file = outfile)
    print(acc, end="")
    for i in range(0,len(pp),30):
        print(pp[i:i + 30], file = outfile)
        print(pp[i:i + 30])
        
outfile.close()
''' 
'''
print("# --------------------------------------------------------------------")
print("Q3.")

# Access the accession numbers from start10.dat (done)
# Access the accesion numbers from res10.dat (done)
# Look at the difference between both using sets. (done)

# --------------------------------------------------------------------
try:
    infile = open(sys.argv[1], "r")
except FileNotFoundError as error:
    print(bright_purple +"Translation: Include the start10.dat file followed by the res10.dat file." + reset)
    sys.exit(1)
    
except IndexError as error:
    print(bright_purple +"usage: python3 python_program.py [file 1...] [file 2 ...] " +reset)
    sys.exit(1)

set_of_accessions = set()

line = infile.readline()
while line != "":
    
        set_of_accessions.add(line.strip())
    
        line = infile.readline()
    
infile.close()
# --------------------------------------------------------------------
article_accession_number = ""
try:
    infile_res = open(sys.argv[2], "r")
    
except FileNotFoundError as error:
    print(brightish +"Translation: Include the start10.dat file followed by the res10.dat file." + reset)
    sys.exit(1)
    
except IndexError as error:
    print(brightish +"usage: python3 python_program.py [file 1...] [file 2 ...] " +reset)
    sys.exit(1)
    
for line in infile_res:
    cds_value = re.search(r"(?<=\t)(?P<acc_number>\w+......)", line)
    
    # Add  the answer to a string. 
    if cds_value is not None:
        article_accession_number += cds_value["acc_number"]
        
        # Add commas  
        article_accession_number += ","
    
infile_res.close()

set_of_res_accessions = set()
set_of_res_accessions.update(article_accession_number)
# --------------------------------------------------------------------
# Which accession numbers are in the start that are not in the results?
the_difference = set_of_accessions - set_of_res_accessions
the_diff = "\n".join(sorted(list(the_difference)))

print(the_diff)
'''
# --------------------------------------------------------------------
'''
print("# --------------------------------------------------------------------")
print("Q4.") 
# PSEUDOCODE: Stay awake in class.
# Read the ex5.acc file. 
# Print a list of accession numbers.
# Count the duplicate accession numbers and add the count to a dictionary. 
# Print the dictionary with the accession name and number of occurrences in the file. 

list_of_accessions = list()

try:
    infile = open(sys.argv[1], "r")
    
    assert sys.argv[1] == "ex5.acc", "The requested file is ex5.acc"
    
except FileNotFoundError as error:
    print(bright_purple +"Translation: Include the ex5.acc file." + reset)
    sys.exit(1)
    
except IndexError as error:
    print(bright_purple +"usage: python3 python_program.py [file 1...] " +reset)
    sys.exit(1)
    
except AssertionError as err:
    print(bright_purple + str(err) + reset)
    sys.exit(1)
    
line = infile.readline()
while line != "":
    
        list_of_accessions.append(line.strip())
    
        line = infile.readline()
    
infile.close()

# --------------------------------------------------------------------
noted_occurrence = {}

for acc in sorted(list_of_accessions):
    if acc in noted_occurrence:
        noted_occurrence[acc] += 1
    else:
        noted_occurrence[acc] = 1
        
# print the accession name as a key and its corresponding count. 
for accession in sorted(noted_occurrence, key = noted_occurrence.get):
    print(f"{accession}, {(noted_occurrence[accession])}")

print("# --------------------------------------------------------------------")
print("Q5.") 
# In the genbank files data?.gb you should extract the coding DNA sequence
# Next you have to display a list of codons used in the coding sequence
# Display the number of times they are used
try: 
    infile = open(sys.argv[1], "r")
    
except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
# --------------------------------------------------------------------
line = infile.readline()

exons_flag = False
exons = ''

while line != "":
    
    coding = re.search(r"^\s+CDS\s+join\((.+)",line)
    
    if coding is not None:
        exons += coding.group(1).strip()
        
        if line[-2] == "(":
            exons_flag = True
            
        if line[-2] == ")":
            exons_flag = False
            
        if exons_flag is True:
            exons += line.strip()

    line = infile.readline()
    
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
# --------------------------------------------------------------------
# Display a list of codons used. 
list_of_codons = []

for i in range(0, len(coding_sequence), 3):
    list_of_codons.append(coding_sequence[i:i+3])

#print(list_of_codons)
# --------------------------------------------------------------------
codon_occurrence = {}

for cdn in sorted(list_of_codons):
    if cdn in codon_occurrence:
        codon_occurrence[cdn] += 1
    else:
        codon_occurrence[cdn] = 1
        
print("CODON OCCURRENCE:")

for codon in sorted(codon_occurrence, key = codon_occurrence.get):
    print(f"{codon}{(codon_occurrence[codon])}")
    
# print the codon name as a key and its corresponding count as a string)
'''
print("# --------------------------------------------------------------------") 
print("Q6.") 

try: 
    infile = open(sys.argv[1], "r")
    
except IndexError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_purple + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
    
except FileNotFoundError as error:
    print("usage: python3 python_program.py [file ...]")
    print(bright_green + "Translation: Include a single data1.gb , data2.gb, data3.gb or data4.gb file. ", reset)
    sys.exit(1)
    
flag = False 
Authors = ''

re_list = [ 
    
    # Extract the author lines. 
    r'(?<=\sAUTHORS\s)(.+)'
]

line = infile.readline()

while line != "":
    
    for regular_expression in re_list:
        result = re.search(regular_expression, line)
        
        if result is not None:            Authors += result.group(1)
            
    line = infile.readline()
    
infile.close()
# --------------------------------------------------------------------
# replace the spaces with a newline, remove and & III, Add the authors to the set. 

authors_1 = re.sub(r'\s', '\n', Authors)
authors_2 = re.sub(r'and', '', authors_1)
authors_3 = re.sub(r'III\.', '', authors_2)
authors_4 = re.sub(r'De', '', authors_3, re.IGNORECASE)

authors_list = re.split(r'\n', authors_4)

authors_set = set()

for aut in sorted(authors_list):
    if aut in authors_list:
          authors_set.add(aut)
    
print("AUTHORS:")
for author in sorted(authors_set):
    print(author)
    
print("\U0001F33B","by Miss Oriade Latifah Simpson, Friday 14 October 2022" ,"\U0001F4BB")