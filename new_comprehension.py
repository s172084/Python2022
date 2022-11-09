#!/usr/bin/env python3
import re  
import sys
import itertools

#--------------------------------------------------------------------
bright_cyan = "\033[0;96m"
bright_yellow = "\033[0;33m"
bright_green = "\033[0;32m"
brightish = "\033[0;36m"
bright_purple ="\033[0;35m" 
reset = "\033[0m\n"
#--------------------------------------------------------------------
print("#--------------------------------------------------------------------")
print("\U0001F338 Q1. \U0001F338")
print("#--------------------------------------------------------------------")
#--------------------------------------------------------------------"

def read_matrix(file):
    # Read a lists of lists (matrix) from an input file
    M = []
    
    infile = open(file, "r")
    for line in infile:
        line_values = line.strip().split("\t") 
        M.append(list(map(lambda line_values : int(line_values), line_values)))
    return M
    infile.close()
#--------------------------------------------------------------------"
def multiply_matrices(matA, matB):
    # Multiply Two Square 4x4 matrices. Each matrix is a list of list object.
    
    def __transpose(matB):
        #Transpose a (list of list) matrix using list comprehension
        
        return [[row[i] for row in matB] for i in range(4)]
        #return [[row[i] for row in matB] for i in range(0, len(matB))]
        
        
    def __perform_matrix_muliplication(n, m):
        # Perform matrix multiplication on two normal (flattened) lists
        
        return list(map(lambda n,m : n*m , n,m))
            
    Bt = __transpose(matB)
    
    # flatten the lists
    getA = [no for row in matA for no in row]
    getB_transposed = [no for row in Bt for no in row]
        
    final_matrix = __perform_matrix_muliplication(getA, getB_transposed)
    return (final_matrix)

#--------------------------------------------------------------------"
def display_dot_product(normal_list):
    # Show me the money
    
    def __divide_chunks(normal_list):
        ''''Take a normal list and convert to n equal sublists. The output is a list of lists of strings.'''
        # How many columns should matrix each have?
        n = 4
        
        # Convert integers to strings. 
        K = list(map(str, normal_list))
        
        for i in range(0, len(K), n):
            yield K[i:i + n]
            
            
    def __display_matrix(K):
        '''Concatenate a list of list (matrix) to a string with the appropriate matrix lookie-likie format.'''
        '''The input is a list of list of strings. The output is a single formatted string.'''
        
        MX = ""
        
        for i in K:
            MX += "{}".format("\t".join(i))
            # Add newlines \n or spaces " "  
            MX += "\n"
            
        return(MX)
    
    #--------------------------------------------------------------------"
    # call the internal functions
    numbers_in_rows = list(__divide_chunks(normal_list))
    the_dot_product = __display_matrix(numbers_in_rows)
    return(the_dot_product)

#--------------------------------------------------------------------"
# Read a matrix from a file

help_message = '''This program calculates the dot product of two matrices.
The files containing the matrices are called mat1.dat and mat2.dat. 
In order to run the program, enter the first two filenames for matrix A and matrix B.
A guideline of how to do this is shown below in the usage instructions. \n
The Usage: python3 program_name.py [-filename] [-filename] '''

# STEP 1
if len(sys.argv) < 3 or sys.argv[1] == '-h' or sys.argv[-1] == '--help':
    sys.exit(bright_green + help_message + reset)
else:
    try:
        A = read_matrix(sys.argv[1])
    except FileNotFoundError:
        print(bright_purple+ "There is a typo in the first filename." + reset)
        sys.exit()
    else:
        try:
            B = read_matrix(sys.argv[2])
        except FileNotFoundError:
            print(bright_purple+ "There is a typo in the second filename." + reset)
            sys.exit()
    finally:
        print(brightish+"Both files were read by the program."+reset)
    
# STEP 2
mm = multiply_matrices(A, B)

# STEP 3: Write to the screen. 
sys.stdout.write("THE DOT PRODUCT:\n")
sys.stdout.write((display_dot_product(mm)))

print("#--------------------------------------------------------------------")
print("\U0001F338 Q2.\U0001F338")
print("#--------------------------------------------------------------------")

log_intensities = ""
control = list()
cancer = list()

the_input_accession = input("Enter an accession number: (e.g. H55933 , R39465, H80240 etc.) \n")

try:
    infile = open("dna-array.dat", "r")
except IOError as error_ag:
    print(bright_cyan + "There is a minor problem with opening the 'dna-array.dat' file.", reset)
    sys.exit(1)
    
for line in infile:
    
    #--------------------------------------------------------------------
    classes_column = re.search('(?<=COL_CLASSES\s{3})(?P<case_or_control>(.+))', line)
        
    if classes_column is not None:
        #print(classes_column["case_or_control"])
        
        # substitute all 0s with the word Cancer
        # substitute all 1s with the word Control
        case_or_control = re.sub(r'0', 'Cancer', classes_column["case_or_control"])
        case_or_cont = re.sub(r'1', 'Control', case_or_control)
        case_or_conrol_list = case_or_cont.split("\t")
        #--------------------------------------------------------------------"
        
    if line.startswith("Hsa"): # parse the file piece by piece
        #--------------------------------------------------------------------"
        start = 0
        
        while line[start] == " ":
            start = start + 1
            
        stop = start +5
        
        while line[stop] != "\t":
            stop = stop +  1
            
        HSA_number = line[start:stop]
        #print(HSA_number)
        #--------------------------------------------------------------------"
        start_again = stop + 1
        
        while line[start_again] == " ":
            start_again = start_again + 1
            
        stop_again = start_again + 1
        
        while line[stop_again] != "\t":
            stop_again = stop_again +  1
            
        gene_accession_number = line[start_again:stop_again]
        #print(gene_accession_number)
        #--------------------------------------------------------------------"
        the_beginning = stop_again + 1
        
        while line[the_beginning] == " ":
            the_beginning = the_beginning + 1
            
        the_end = the_beginning + 1
        
        while line[the_end] != "\t":
            the_end = the_end +  1
            
        the_description = line[the_beginning:the_end]
        #print(the_description)
        #--------------------------------------------------------------------"
        #print("{:<10} {:<8} {:<15}".format(HSA_number, gene_accession_number, the_description, ))
        #--------------------------------------------------------------------"
        # remove the \n and '' characters and convert to a list
        log_intensities = line[the_end+1: -1]
        log_intensities_list = log_intensities.split("\t")
        
        #--------------------------------------------------------------------"
        data_structure = {
            
        }
        # Add the accession numbers to the data structure.  
        data_structure["acc"] = dict()
        data_structure["acc"] = gene_accession_number
        
        # Add the HSA numbers. 
        data_structure["hsa"] = dict()
        data_structure["hsa"] = HSA_number
        
        # Add the description. 
        data_structure["desc"] = dict()
        data_structure["desc"] = the_description
        
        # Add the intensities
        data_structure["log_int"] = dict()
        data_structure["log_int"] = log_intensities_list
        
        # Add the classes
        data_structure["category"] = dict()
        data_structure["category"] = case_or_conrol_list
        
        #--------------------------------------------------------------------"
        # For a particular accession: 
        # Access the log intensity values baseed on whether the category is Cancer or Control. 
        # Append the log intensity values to a list called control or a list called cancer. 
        # Note: Where should the try except statement go if the accession is not present.
        if data_structure['acc'] == the_input_accession:
            for i in range(len(data_structure["category"])):
                
                if data_structure["category"][i] == 'Cancer':
                    cancer.append(data_structure["log_int"][i])
                    
                elif data_structure["category"][i] == 'Control':
                    control.append(data_structure["log_int"][i])

infile.close()
#--------------------------------------------------------------------"
#print(control)
#print(cancer)

# print the log intensity values side by side using zip longest from iterools. 
print("{} {} {}".format(bright_purple + f"cancer patients"+ reset.strip(), "\t", 
    bright_cyan+ f"control patients" + reset.strip(), end = ""))

for i, j in itertools.zip_longest(cancer, control, fillvalue='\'.\'\''):
    print("{:<10} {:<9} {:<15}".format(f"{i}", "\t",  f"{j}"))
print("\U0001F33B","by Miss Oriade Latifah Simpson, Wednesday 9th November 2022" ,"\U0001F4BB")