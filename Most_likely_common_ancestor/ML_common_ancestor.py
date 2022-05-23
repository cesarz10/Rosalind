import numpy as np
from Bio import SeqIO

input_file = 'Most_likely_common_ancestor/rosalind_cons.txt'
seq_arr = []
nucl_arr = ['A', 'C', 'G', 'T'] # list of DNA nucleotides

for seq_record in SeqIO.parse(input_file, "fasta"): # appending sequences into array
    seq_arr.append(seq_record.seq)

cols = len(seq_arr[0]) # number of bases of sequences
nucl_dict = {'A': [0]*cols, 'C': [0]*cols, 'G': [0]*cols, 'T': [0]*cols}

for seq in seq_arr:
    for j in range(cols):
        nucl_dict[f'{seq[j]}'][j] += 1 # counting the appearances of every base in the position

vals_list = list(nucl_dict.values()) # values of dict to list
cons_arr = np.argmax(vals_list, axis=0) # get indexes of max values
f_nuc = [nucl_arr[val] for val in cons_arr] # translate to nucleotides

# print in an organized way
print('\n', ''.join(f_nuc))
for k, v in nucl_dict.items(): # print pairs of keys and values
    print(f'{k}:', ' '.join(str(x) for x in v)) # int array to string