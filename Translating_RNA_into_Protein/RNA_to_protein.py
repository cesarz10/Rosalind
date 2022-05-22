import pandas as pd

with open('Translating_RNA_into_Protein/rosalind_prot.txt') as f:
    txt = f.read()

# extracting table of codons 
df = pd.read_fwf('Translating_RNA_into_Protein/RNA_codon_table.txt', header=None)
codons = {}


# indexing every codon to its respective protein 
for i in range(16):
    for j in range(0, 8, 2):
        codons[f'{df[j][i]}'] = df[j+1][i]


# translating RNA sequence into protein
prot = ''
for i in range(0, len(txt), 3):
    if(codons[f'{txt[i:i+3]}'] == 'Stop'): # break when a Stop codon is reached
        break
    prot += codons[f'{txt[i:i+3]}']

print(f'\n{prot}\n')