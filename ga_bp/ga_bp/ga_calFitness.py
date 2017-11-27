'''
Created on 2017年11月21日

@author: ljs
'''
def ga_calFitness(pop,x):
    best_pop = pop[0]
    best_fit = x[0]
    for i in range(1,len(pop)):
        if(x[i]>best_fit):
            best_fit = x[i]
            best_pop = pop[i]
    #best_pop最优个体[1,0,0,1,0...],best_fit最优适应度,
    return [best_pop,best_fit]

if __name__ == '__main__':
    pass
