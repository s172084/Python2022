#!/bin/bash
date
printf "19\n\n"
paste ex1.acc ex1.dat > ex1.tot
echo "The ex1.tot file looks similar to this : " 
head -n 5 ex1.tot
printf "\n\n"
printf "#--------------------------------------------------------------------\n"

#--------------------------------------------------------------------
printf "20\n\n"
cat ex1.tot | cut -f1,5 > ex1.res
echo "Therefore columns 1 and 5 look like this : "
head -n5 ex1.res
printf "\n\n"
printf "#--------------------------------------------------------------------\n"

#--------------------------------------------------------------------
printf "21\n\n"
echo "The SwissProt IDs which have the largest values are these ... : "
sort -n -r -k 2 ex1.res |head -n 3 | cut -f1
printf "\n\n"
printf "#--------------------------------------------------------------------\n"

#--------------------------------------------------------------------
printf "22\n\n"
echo "There are 85 lines in orphans.sp with a GenBank accession number."
grep -n ".CDS.1" orphans.sp |wc -l 
printf "\n\n"
printf "#--------------------------------------------------------------------\n"
#--------------------------------------------------------------------
printf "23\n\n"
grep "_HUMAN" orphans.sp | wc -l
grep "_HUMAN" orphans.sp | grep "HYPOTHETICAL" |wc -l
echo "There are 207 human genes with SwissProt IDs in orphans.sp file. Of those, 11 are hypothetical."
printf "\n\n"
printf "#--------------------------------------------------------------------\n"
#---------------------------------------------------------------------
printf "24\n\n"
grep "_RAT" orphans.sp |wc -l 
grep "_RAT" orphans.sp | grep "PRECURSOR" |wc -l
echo "There are 51 genes which are from RAT. Of those, 9 are precursor genes."
printf "\n\n"
printf "#--------------------------------------------------------------------\n"
echo "by Miss Oriade Latifah Simpson s172084@dtu.dk"
#--------------------------------------------------------------------