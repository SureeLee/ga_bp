'''
Created on 2017年11月21日

@author: ljs
'''
from ga_bp_real.ga_encoding import ga_encoding
from ga_bp_real.ga_calObject import ga_calObject
from ga_bp_real.ga_calFitness import ga_calFitness
from ga_bp_real.ga_selection import ga_selection
from ga_bp_real.ga_crossover import ga_crossover
from ga_bp_real.ga_mutation import ga_mutation
from ga_bp_real.ga_replace import ga_replace
from ga_bp_real.ga_getBest import ga_getBest
from ga_bp_real.bp_object import bp_object

POP_SIZE = 20#种群个体数量
GEN = 20#遗传迭代代数
NUM = 131 #11*10+10+10*1+1待优化权值与偏重数量
PC = 0.7#交叉概率
PM = 0.05#变异概率
result = [[]]#存储最优解及其对应权值偏重
pop = ga_encoding(POP_SIZE,NUM)
for i in range(GEN):
    obj = ga_calObject(pop)
    best_pop,best_fit = ga_calFitness(pop,obj)
    #如果这一代最优值高于上一代，就用上一代最优值代替这一代最差的
    if len(result) != 1 and best_fit>result[-1][0]:
        ga_replace(result[-1],pop,obj)
    result.append([best_fit,best_pop])
    #python中list,dict是可变对象，参数传递相当于引用传递，所以会改变变量本身，string,tuple,number是不可变对象
    ga_selection(pop,obj)
    ga_crossover(pop,PC)
    ga_mutation(pop, PM)
    print('over..........one term')
for r in result:
    print(r)
best = ga_getBest(result)
print(best)
bp_object(best)
