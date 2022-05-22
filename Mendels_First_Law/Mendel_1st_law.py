import numpy as np

with open('Mendels_First_Law/rosalind_iprb.txt') as f:
    txt = f.read()

# k: homozygous dominant (AA) 
# m: heterozygous (Aa)
# n: homozygous recessive (aa)

txt_arr = np.array(txt.split(' ')).astype(np.int32)
popultaion = sum(txt_arr)
print(txt_arr)

k, m, n = map(float, txt_arr)

couples = [k*(k-1), # AA x AA
           k*m, # AA x Aa
           k*n, # AA * aa
           n*k, # aa * AA
           m*k, # Aa * AA
           m*(m-1)*0.75, # Aa * Aa
           m*n*0.5, # Aa * aa
           n*m*0.5, # aa * Aa
           n*(n-1)*0] # aa * aa 

print(sum(couples))

print(round(sum(couples) / (popultaion * (popultaion - 1)), 5))