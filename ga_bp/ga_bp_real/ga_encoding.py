'''
Created on 2017年11月21日

@author: ljs
'''
import random

def ga_encoding(pop_size,num):
    pop = [[]]
    for i in range(pop_size):
        temp = []
        for j in range(num):
            temp.append(round(random.uniform(-0.5,0.5),8))
        pop.append(temp)
    return pop[1:]    
    
if __name__ == '__main__':
    #pass
    pop = ga_encoding(30,131)
    for p in pop:
        print(p)        
    print(len(pop))