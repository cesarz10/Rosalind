with open('Calculating_expected_offspring/rosalind_iev.txt') as f:
    parents = [int(x) for x in f.read().split()] # Reading and converting str to int

probabilities = [1, 1, 1, 0.75, 0.5, 0] # Probabilities for the different genotypes to produce a dominant offspring
                                         # AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa

act_prob = list(map(lambda x,y: x*y, parents, probabilities)) # multiplying the parents array with the respective probability
Offspring = 2 * sum(act_prob)

print(f'\nParents: {parents}\nProbabilities: {probabilities}\nOffspring: {Offspring}\n')