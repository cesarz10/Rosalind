with open('Counting_Point_Mutations/rosalind_hamm.txt') as f:
    seq = f.read()

seq_arr = seq.splitlines()
err = 0

for i in range(len(seq_arr[0])):
    if(seq_arr[0][i] != seq_arr[1][i]):
        err += 1

print(f'\nPoint mutations:{err}\n')