'''
Created on 2017年11月21日

@author: ljs
'''
import random

def ga_encoding(pop_size,chrom,num):
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(chrom*num):
            temp.append(random.randint(0,1))
        pop.append(temp)
    return pop[1:]    
    
if __name__ == '__main__':
    #pass
    pop = ga_encoding(30,9,131)
    for p in pop:
        print(p)        
    print(len(pop))