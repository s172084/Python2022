#!/usr/bin/env python3
bright_green = "\033[0;32m"
brightish = "\033[0;36m"
bright_purple ="\033[0;35m" 
reset = "\033[0m\n"
bright_cyan = "\033[0;96m"

import re
import statistics

print("#--------------------------------------------------------------------")
print("Q1.")
print("#--------------------------------------------------------------------")

# a) Describe which keywords/patterns you will be looking for when parsing the file searching for the variants/mutations and the sequence.
print("ID   CIQ3_HUMAN     STANDARD;      PRT;   872 AA.")
print("FT   VARIANT     309    309       W -> R (IN BFNC2).")
print("FT   VARIANT     310    310       G -> V (IN BFNC2")
print("FT   MUTAGEN     310    310       G->V")
print("FT   MUTAGEN     318    318       G->S:")
print("SQ   SEQUENCE")
print("//")
print("RP   VARIANT BFNC2 ARG-309.")
print("\n")

# b) Describe a method, perhaps using pseudocode, to extract the sequence 
#    and variations/mutants and print all the different full sequences in fasta.

print(bright_purple+'''PSEUDOCODE:
Search for the name of the SwissProt entry (CIQ3_HUMAN) in appendix 1 using regular expressions
Extract the original amino acid sequence using stateful parsing. 
Turn the sequence into a byte array as mentioned in the lecture. 
Find the index number in the variant or mutagen line using regular expressions. 
Create the variant by substituting a letter in the byte array at a particular index with the new letter. 
In (FT), note several variants and mutations of the gene exist. 
Print all variations of the full sequence, with the appropriate amino acid changed.
Write the result to a FASTA file, with names for each entry. 
I may do this on a lot of SwissProt entries so take note of the name. '''+reset)

#--------------------------------------------------------------------
# c) Implement your method in python.

flag = False
aa_seq = ""

infile = open("appendix1.txt", "r")

for line in infile:
    
    if line[:2] == "//":
        flag = False 
        
    if flag is True:
        aa_seq += re.sub(" ", "", line.strip())
        
    if line[:2] == "SQ":
        flag = True 
        
infile.close()
#--------------------------------------------------------------------

amino_acid_sequence = bytearray(aa_seq.encode('ASCII'))

#--------------------------------------------------------------------
def process_index(s):
    '''Take a string in the swissprot file and return the "zero-indexed" index number and new amino acid'''
    search_terms = re.search(r'(?P<index_number>\d{3})\s+\d{3}\s+(\w{1})?\s?\->?\s?(?P<change_to>\w{1})', s)
    
    return int(search_terms["index_number"])-1

def process_variant(s):
    ''' Take a string in the swissprot file and return the new amino acid as an ASCII number'''
    search_terms = re.search(r'(?P<index_number>\d{3})\s+\d{3}\s+(\w{1})?\s?\->?\s?(?P<change_to>\w{1})', s)
    
    return ord(search_terms["change_to"])

def process_comp(s, bite_array):
    ''' Take in the variant line and bytearray and substitute a letter at a particular index'''
    bite_array[process_index(s)] = process_variant(s)
    
    return bite_array.decode('ASCII')

#--------------------------------------------------------------------
class mutation:
    '''A mutation class'''
    
    # class attributes are the same for every instance of a class. 
    type = "mutation"
    
    # instance attributes are different for every instance of a class.
    def __init__(self, name, sequence):
        
        self.name = name
        self.sequence = sequence
        
        # instance method 1
        def __len__(self):
            return len(self.sequence)
#--------------------------------------------------------------------
v1 = "FT   VARIANT     309    309       W -> R (IN BFNC2)."
v2 = "FT   VARIANT     310    310       G -> V (IN BFNC2"
m1 = "FT   MUTAGEN     310    310       G->V"
m2 = "FT   MUTAGEN     318    318       G->S:"

# process the the sequence completely
variant1 = process_comp(v1, amino_acid_sequence)
variant2 = process_comp(v2, amino_acid_sequence)
mutagen_1 = process_comp(m2, amino_acid_sequence)
mutagen_2 = process_comp(m1, amino_acid_sequence)

# instantiate the class. 
vee1 = mutation(name = "VARIANT1", sequence = variant1)
vee2 = mutation(name = "VARIANT2", sequence = variant2)
mu_1 = mutation(name = "MUTAGEN1", sequence = mutagen_1)
mu_2 = mutation(name = "MUTAGEN2", sequence = mutagen_2)

#--------------------------------------------------------------------
# write to a FASTA file. 

outfile = open("FASTA.fa", "w")
print("> |ORIGINAL|", file = outfile)

for e in range(0, len(aa_seq), 60):
    print(aa_seq[e:e+60], file = outfile)
    
print("\n", file = outfile)

mutation_list = [vee1, vee2, mu_1, mu_2]
for i in mutation_list:
    print(">", i.name, "|", file = outfile)
    
    for e in range(0, len(i.sequence), 60):
        print(i.sequence[e:e+60], file = outfile)
        
    print("\n", file = outfile)
    
outfile.close()
#--------------------------------------------------------------------

# d) What kind of error checking could/should you include in your program ? 
# name every check, which is relevant to the task, not every check possible.

print(bright_green+'''
Check that the right variant name was written to the FASTA file. 
Check the file is written to and not empty. 
Check that the byte array is turned into a string. 
Make the class subscriptable. 
Check there is a way to find the length of the object.''' +reset)


# e) In what way could you generalize or extend the program ? 
print(bright_cyan + "Extend the program by writing it for multiple swiss prot entries." +reset)

#--------------------------------------------------------------------
print("#--------------------------------------------------------------------")
print("Q2.")
print("#--------------------------------------------------------------------")

''' 
A program calculates scores based on amino acid sequence features.
The output is in appendix 3. 
There is an accession number followed by 6 numbers between 0 and 1 per line (tab separated). 
Find the accession numbers with the highest and lowest average scores (average of the 6 numbers). 
However, you want to exclude any genes on your negative list from your calculations. 
These genes are listed as SwissProt IDs in appendix 4.
Since GenBank accession numbers and SwissProt IDs are not identical, you need to translate between them in order to solve your problem.
appendix 5 does that. 
There is a SwissProt ID, second item is irrelevant, and third is the corresponding GenBank accession number.


a) Describe a method, perhaps using pseudo code, to find the data.
print('''
# read appendix 5 to get the swisspprot to genbank accession map. 
# Read in genes in appendix 4 to find out which ones are on the negative list. 
# convert swissprot ids in appendix 4 to genbank accession numbers
# Delete the negative list genes from the swissprot to genbank accession map using set or filter. 
# read appendix 3 to match accession map to accession. 
# Find the average scores for the accession numbers. 

''')

b) Implement your method in python.
c) Have you made any assumptions about the data in your algorithm? Which? Why? 
# I assumed that all of the names were in the dictionary, but they are not. 

Are they reasonable assumptions (explain) ? Could/should you do away with them (by changing the code) ?
d) Usually, when you have this kind of problem, you want the highest 10 and lowest 10 average scores,
not just the top and bottom average score. 
How would you solve this problem ? Will it change any assumptions in c) ? 

'''
class gene:
    '''A gene class'''
    
    # class attributes are the same for every instance of a class. 
    type = "gene"
    
    # instance attributes are different for every instance of a class.
    def __init__(self, swiss_prot_name, genbank_accession, average_score, sequence):
        
        self.swiss_prot_name = swiss_prot_name
        self.sequence = sequence
        self.genbank_accession = genbank_accession
        self.average_score=average_score
        
        # instance method 1
        def __len__(self):
            return len(self.sequence)
        
#--------------------------------------------------------------------
infile = open("appendix5.txt", "r")

sp = []
ac = []

for line in infile:
    line = line.rstrip("\n").split("\t")
    #swissprot
    sp.append(line[0])
    
    #accession
    ac.append(line[2])
infile.close()

# Turn two lists into a dictionary. 
mapped = dict(zip(sp, ac))

#--------------------------------------------------------------------
infile = open("appendix4.txt", "r")
nl = []

for line in infile:
    nl.append(line.strip("\n"))
    
infile.close()
#--------------------------------------------------------------------
infile = open("appendix3.txt", "r")

for line in infile:
    line = line.rstrip("\n").split("\t")
    
    num_line = line[1:] 
    # create a dictionary of this:
    print(line[0], ": ",round(statistics.mean(list(map(float,num_line))),2))
        
infile.close()
#--------------------------------------------------------------------
# Get the keys in mapped, if the key is not in the negative list. 
filtered_dict = {k:v for k,v in mapped.items() if k not in nl}
print(filtered_dict)
#--------------------------------------------------------------------
infile.close()