from Bio import SeqIO
from natsort import natsorted

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

            if( t == s ): # order doesn't matter, and directed loops are prohibited
                continue
            else:
                if(suffix == prefix): # if they overlap
                    # adj_list.append([s, t])
                    if(int(s) > int(t)):
                        adj_list.append([t, s])
                    else:
                        adj_list.append([s, t])

    print(len(adj_list))
    adj_list = natsorted(adj_list)
    return adj_list




# adjacency_list = graph2(seq_dict, 3)
# print(adjacency_list)
adjacency_list = graph(seq_dict, 3)
# print(adjacency_list)

print('\n')
for vect in adjacency_list:
    print(f'{seq_dict[vect[0]][0]} {seq_dict[vect[1]][0]}')
print('\n')








# ------------------------------------------
# function that takes the dict of sequences and a value of k (length) and returns the adjacency list
def graph2(dict, k):
    seq_dict = dict
    adj_list = []

    for s, val_s in seq_dict.items():        
        suffix = val_s[1][-k:] # last k nucleotides
        
        for t in range(int(s), len(seq_dict.keys())):
            # print(f's: {s}\nt: {t}')
            prefix = seq_dict[f'{t}'][1][:k] # first k nucleotides

            if( [s, t] in adj_list or [t, s] in adj_list or t == s ): # order doesn't matter, and directed loops are prohibited
                continue
            else:
                if(suffix == prefix): # if they overlap    
                    adj_list.append([s, str(t)])
            
    # print(adj_list)
    return adj_list
