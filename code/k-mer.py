# FILE: q2.py
# AUTHOR: Hanie Samimi
# CREATE DATE: 9 April 2020

import sys
import math
import os
import collections

kmer_dict = collections.defaultdict(int)

def kmer(sequence, k_size):
    start_index = 0
    end_index = len(sequence) - k_size +1
    while start_index < end_index:
        key = sequence[start_index:start_index+k_size]
        kmer_dict[key] += 1
        start_index += 1


def read_fasta(inputFile , k_size):
    fasta_file = open(inputFile, "r")
    counter = 1
    sequence = ""
    for line in fasta_file:
        if line[0] is ">":
            # call the kmer if sequence is not empty
            if sequence is not "":
                print('Analyzing chunk {} of data'.format(counter))
                kmer(sequence, k_size )
                sequence = sequence[-k_size+1:]
                counter += 1
        else:
            if line[-1] is '\n':
                line = line[:-1]
            sequence = sequence + line
    print("Kmer counting is finished!")
    fasta_file.close()


## Main ##
# SET WORKING DIRECTORY
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# GET THE FILE NAME FROM USER

print("Enter K value:")
k_size = int(input())

inputFile: str = "../data/sampleData.FASTA"
print("Enter input file or skip [S] to use the default:")
response: str = input()
if response != "S":
    inputFile = response

# CHECK IF INPUT IS VALID

# READ THE INPUT FILE
read_fasta(inputFile, k_size)
## analyzing the dictionary

