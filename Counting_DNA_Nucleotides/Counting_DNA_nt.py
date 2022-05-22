with open('rosalind_dna.txt') as f:
    txt = f.read()

print(f"{txt.count('A')} {txt.count('C')} {txt.count('G')} {txt.count('T')}")