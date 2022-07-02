from Bio import SeqIO

input_file = 'Finding_Shared_Motif/rosalind_lcsm.txt'
seq_dict = {} # dictionary of names and sequences

for i, seq_record in enumerate(SeqIO.parse(input_file, "fasta")): 
    seq_dict[f'{seq_record.id}'] = seq_record.seq # store data in dictionary (seq_dict)

sequences = [x for x in seq_dict.values()] # converting values into a list of sequences


# function that finds longest motif in list of sequences
def find_motif(seq_list):

    min_len = min(map(len, seq_list))
    print(f"\nMin len: {min_len}")

    min_idx = [seq_list.index(sub_s) for sub_s in seq_list if len(sub_s) == min_len ][0] # find index of min_len sequence 
    print(f"Index of min_len: {min_idx}") #                              if there are multiple possible elements choose the 1st one


    for n_chars in range(min_len, 0, -1): # reduce the number of characters every loop
        act_pos = 0

        while (act_pos + n_chars <= len(seq_list[min_idx])):
            motif = seq_list[min_idx][act_pos:(act_pos+n_chars)] # move position to try every sub_seq of that length in seq
            res = all(motif in seq for seq in seq_list) # all() returns True if every element is True

            if res:
                print(f"\nThe motif is: {motif}\n")
                return motif
            
            act_pos += 1

    print("There is no match ???") # not possible to not return anything (in theory)
    return

result = find_motif(sequences)