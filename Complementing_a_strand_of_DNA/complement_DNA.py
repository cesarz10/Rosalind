# complement and the reverse the sequence
# A <--> C, G <--> T

with open('Complementing_a_strand_of_DNA/rosalind_revc.txt') as f:
    strand = f.read()


# return complement of nucleotide
def complement(N):
    if N == 'A':
        return 'T'
    if N == 'C':
        return 'G'
    if N == 'T':
        return 'A'
    if N == 'G':
        return 'C'


final = ''

# add complement to final strand
for i in range(len(strand)-1):
    final += complement(strand[i])

final = final[::-1]
print(final)    