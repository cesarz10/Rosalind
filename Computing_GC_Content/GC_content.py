from Bio import SeqIO
from Bio.SeqUtils import GC

input_file = 'Computing_GC_Content/rosalind_gc.txt'
seq_dict = {}

for seq_record in SeqIO.parse(input_file, "fasta"): # file doesn't need to be .fas to be read as fasta (fasta is just txt with formatting)
    seq_dict[f'{seq_record.id}'] = round(GC(seq_record.seq), 6) # store data in dictionary (seq_dict)

max_gc = max(seq_dict, key=seq_dict.get) # find key of the dicionary's max value
print(f'\n{max_gc}\n{seq_dict[max_gc]}\n')