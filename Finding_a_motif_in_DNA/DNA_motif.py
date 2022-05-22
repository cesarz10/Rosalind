with open('Finding_a_motif_in_DNA/rosalind_subs.txt') as f:
    lines = f.readlines()
    txt = lines[0]
    s = lines[1][:-1] # ignoring the \n at the end of the line

arr = [i+1 for i, let in enumerate(txt) if(txt[i:(i+len(s))] == s)] # solo indexo el índice de donde inicia el substring
print(' '.join(str(i) for i in arr)) # printing in the asked format