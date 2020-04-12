# FILE: k-mer.py
# AUTHOR: Hanie Samimi
# CREATE DATE: 9 April 2020

import sys
import math
import os
import collections
import time


# GLOBAL: KMER DICTIONARY
kmer_dict = collections.defaultdict(int)


# KMER COUNTER
def kmer(sequence, k_size):
    start_index = 0
    end_index = len(sequence) - k_size + 1
    # itterate over the sequence with a K size window
    while start_index < end_index:
        key = sequence[start_index:start_index + k_size]
        kmer_dict[key] += 1
        start_index += 1


# READ FASTA FILE AND ANALYZE
def read_fasta(inputFile, k_size):
    fasta_file = open(inputFile, "r")
    counter = 1
    sequence = ""
    for line in fasta_file:
        if line[0] is ">": # header line
            # Call the kmer if sequence is not empty
            if sequence is not "":
                print('Analyzing chunk {} of data'.format(counter))
                kmer(sequence, k_size)
                sequence = sequence[-k_size + 1:] #add the last k-1 character to the new sequence
                counter += 1
        else:
            if line[-1] is '\n': # Omit EOL character
                line = line[:-1]
            sequence = sequence + line
    print('Analyzing chunk {} of data'.format(counter))
    kmer(sequence, k_size)
    print("Kmer counting is finished!")
    fasta_file.close()


### Main ###
# SET WORKING DIRECTORY
# START TIME
start_time = time.clock()
print(time.strftime('%X %x %S %Z'))

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# GET K VALUE AND Input FILE NAME FROM USER
print("Enter K value:")
k_size = int(input())
while k_size>250: # Max of k value
    print("K value should be less than 250! Try again:")
    k_size = int(input())
inputFile: str = "../data/SRR1748776.FASTA"
print("Enter input file or skip [S] to use the default:")
response: str = input()
if response != "S":
    inputFile = response

# CHECK IF INPUT FILE IS VALID
if not os.path.isfile(inputFile):
    print("Input file does not exist!")
    exit()

# READ THE INPUT FILE
print("Reading fasta file ... ")
read_fasta(inputFile, k_size)

# ANALYZE THE DICTIONARY
print("Data analysis:")
# max_val = [keys for keys,values in kmer_dict.items() if values == max(kmer_dict.values())]
counter = 0
for item in kmer_dict.values():
    counter += item

#max_kmer = max(kmer_dict.items())
key_max = max(kmer_dict.items(), key=lambda a: a[1])
print("There are {} k-mers in the file".format(counter))
print("{} has the maximum frequency".format(key_max[0]))
print("maximum frequency is {}".format(key_max[1]))

#END TIME
print(time.strftime('%X %x %S %Z'))
