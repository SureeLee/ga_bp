'''
Created on 2017年11月21日

@author: ljs
'''
import random

def ga_mutation(pop, pm):
    px = len(pop)
    py = len(pop[0])
    for i in range(px):
        if(random.random() < pm):
            index = random.randint(0, py-1)
            pop[i][index] = round(random.uniform(-0.5,0.5),8)
            
if __name__ == '__main__':
    pass