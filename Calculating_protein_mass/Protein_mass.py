import pandas as pd

with open('Calculating_protein_mass/rosalind_prtm.txt') as f:
    amino_seq = f.read()

amino_df = pd.read_csv('Calculating_protein_mass/aminoacid_table.txt', sep='   ', header=None) # [column][row]


prot_mass = 0
for amino in amino_seq:
    for aminoacid, mass in amino_df[[0, 1]].itertuples(index=False): # iterate through the dataframe elements
        
        if (amino == aminoacid):
            prot_mass += mass
            
print(f"\nProtein mass: {round(prot_mass, 3)}\n")