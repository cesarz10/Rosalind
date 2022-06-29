from Bio import SeqIO

input_file = 'Overlap_Graphs/rosalind_grph.txt'
seq_dict = {} # dictionary of names and sequences

for i, seq_record in enumerate(SeqIO.parse(input_file, "fasta")): 
    seq_dict[f'{i+1}'] = [f'{seq_record.id}', seq_record.seq] # store data in dictionary (seq_dict)


# function that takes the dict of sequences and a value of k (length) and returns the adjacency list
def graph(dict, k):
    seq_dict = dict
    adj_list = []

    for s, val_s in seq_dict.items():        
        suffix = val_s[1][-k:] # last k nucleotides
        
        for t, val_t in seq_dict.items():
            prefix = val_t[1][:k] # first k nucleotides

            if( t != s ): # Directed loops are not valid
                if(suffix == prefix): # if they overlap
                    adj_list.append([s, t])
                    
    return adj_list

adjacency_list = graph(seq_dict, 3)

# Printing expected result with the specified formatting
print('\n')
for vect in adjacency_list:
    print(f'{seq_dict[vect[0]][0]} {seq_dict[vect[1]][0]}')
print('\n')