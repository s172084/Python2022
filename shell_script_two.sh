#!/bin/bash
date 
#--------------------------------------------------------------------
cut -f1 ex1.dat | grep -v - > temp_file1
cut -f2 ex1.dat | grep -v - > temp_file2
cut -f3 ex1.dat | grep -v - > temp_file3
paste temp_file1 temp_file2 temp_file3  > ex1.pos2
echo "The positive numbers are here:"
head ex1.pos2

cut -f1 ex1.dat | grep -e - > ntemp_file1
cut -f2 ex1.dat | grep -e - > ntemp_file2
cut -f3 ex1.dat | grep -e - > ntemp_file3
paste ntemp_file1 ntemp_file2 ntemp_file3  > ex1.neg2

printf "\n\n"
echo "The negative numbers are here :"
head ex1.neg2

rm ntemp* temp*

printf "\n\n"
echo "by Miss Oriade Latifah Simpson s172084@dtu.dk "
#--------------------------------------------------------------------