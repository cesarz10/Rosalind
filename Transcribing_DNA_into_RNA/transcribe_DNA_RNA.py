with open('Transcribing_DNA_into_RNA/rosalind_rna.txt') as f:
    txt = f.read()

trans = txt.replace('T', 'U')

print(trans)