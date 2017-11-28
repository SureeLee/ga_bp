'''
Created on 2017年11月21日

@author: ljs
'''
import math

def reduce(pop):
    population = [[]]
    for po in pop:
        temp = []
        for p in po:
            p = -0.5 + p*(1/255)
            temp.append(round(p,8))
        population.append(temp)
    return population[1:]          
    
    
def ga_decoding(pop,chrom,num):
    population = [[]]
    for p in pop:
        temp = []
        for i in range(num):
            t = 0
            for j in range(chrom):
                t += p[j+chrom*i] * (math.pow(2, j))
            temp.append(t)
        population.append(temp)
    return reduce(population[1:])

def ga_decoding_individual(individual,chrom,num):
    temp = []
    for i in range(num):
        t = 0
        for j in range(chrom):
            t += individual[j+chrom*i] * (math.pow(2, j))
        temp.append(t)
    result = []
    for t in temp:
        t = -0.5 + t*(1/255)
        result.append(round(t,8))
    return result    
        
if __name__ == '__main__':
    pass