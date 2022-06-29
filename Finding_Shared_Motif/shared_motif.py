from Bio import SeqIO

input_file = 'Finding_Shared_Motif/rosalind_lcsm.txt'
seq_dict = {} # dictionary of names and sequences

for i, seq_record in enumerate(SeqIO.parse(input_file, "fasta")): 
    # seq_dict[f'{i+1}'] = [f'{seq_record.id}', seq_record.seq] # store data in dictionary (seq_dict)
    seq_dict[f'{seq_record.id}'] = seq_record.seq # store data in dictionary (seq_dict)


print(seq_dict)

for i in range(len(seq_dict.values()), 0, -1): # reduce the number of characters every loop
    print(i) 
    for key, val in seq_dict.items(): # iterate through every pair of key/value
        print(val)