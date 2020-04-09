# FILE: q2.py
# AUTHOR: Hanie Samimi
# CREATE DATE: 9 April 2020

import sys
import math
import os

def kmer(sequence):
    print(sequence)

def read_fasta(inputFile , k_size):
    fasta_file = open(inputFile, "r")
    counter = 1
    sequence = ""
    for line in fasta_file:
        if line[0] is ">":
            # call the kmer if sequence is not empty
            if sequence is not "":
                print('Analyzing chunk {} of data'.format(counter))
                kmer(sequence)
                sequence = sequence[-k_size+1:]
                counter += 1
        else:
            if line[-1] is '\n':
                line = line[:-1]
            sequence = sequence + line


## Main ##
# SET WORKING DIRECTORY
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# GET THE FILE NAME FROM USER

print("Enter K value:")
k_size = int(input())

inputFile: str = "../data/SRR1748776.FASTA"
print("Enter input file or skip [S] to use the default:")
response: str = input()
if response != "S":
    inputFile = response

# CHECK IF INPUT IS VALID

# READ THE INPUT FILE
read_fasta(inputFile, k_size)
#read_fasta_sequence(inputFile)