'''
Created on 2017年11月21日

@author: ljs
'''
import random

def ga_crossover(pop,pc):
    pop_len = len(pop)
    for i in range(pop_len - 1):
        if(random.random() < pc):
            a1 = random.random()
            a2 = 1 - a1
            temp1 = []
            for index in range(len(pop[0])):
                a = pop[i][index]*a1 + pop[i+1][index]*a2
                temp1.append(a)
            temp2 = []
            for index in range(len(pop[0])):
                a = pop[i][index]*a1 + pop[i+1][index]*a2
                temp2.append(a)
            pop[i] = temp1
            pop[i+1] = temp2

if __name__ == '__main__':
    pass