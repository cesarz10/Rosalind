'''
Month 2: you still have one pair of rabits (because your rabbits were immature in the first Month) = 1
Month 3: you have the initial pair of mature rabbits (from month 2) + 3 immature pairs of rabbits (from that pair) = 4
Month 4: you have 1 Mature pair of rabbits (the initial) its new litter (3 pairs of immature) plus 3 newly mature rabbits (from month 3) = 7
Month 5: you have [ 1 Mature + 3 Immature ] + 3 Mature + [ 3 Matture + 3 x 3 Immature pairs ] = 19

You generally drag everything from the immediately previous generation + the litter from all the rabbits from the generation right before that (because they are all mature in the immediately previous generation).
I hope it helps'''


with open('Rabbits_and_Recurrence_Relations/rosalind_fib.txt') as f:
    n, k = f.read().split(' ')

print(n, k)

def fibonacci(n, k):
    
    arr = [1]
    old  = 0
    temp = 1
    for i in range(n-1):    
        new  = temp + (old * k)
        arr.append(new)
        old = temp
        temp = new
    return arr

print(fibonacci(int(n), int(k)))