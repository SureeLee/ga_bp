'''
Created on 2017年11月21日

@author: ljs
'''
import random


def sum(fit_value):
    total = 0
    for i in range(len(fit_value)):
        total += fit_value[i]
    return total


def cumsum(fit_value):
    t = 0
    for i in range(len(fit_value)):
        t = t + fit_value[i]
        fit_value[i] = t
    return fit_value


def ga_selection(pop, fit_value):
    newfit_value = []
    # 适应度总和
    total_fit = sum(fit_value)
    for i in range(len(fit_value)):
        #计算每个适应度占适应度总和的比例
        newfit_value.append(fit_value[i] / total_fit)
    # 计算累计概率
    cumsum(newfit_value)
    ms = []
    pop_len = len(pop)
    for i in range(pop_len):
        ms.append(random.random())
    ms.sort()
    fitin = 0
    newin = 0
    newpop = pop
    # 转轮盘选择法
    while newin < pop_len:
        if(ms[newin] < newfit_value[fitin]):
            newpop[newin] = pop[fitin]
            newin = newin + 1
        else:
            fitin = fitin + 1
    pop = newpop

if __name__ == '__main__':
    pass
# 轮盘赌模型例子，可以看出在轮盘中所占区域最大的pop[4]会在新种群newpop中拥有更多一样的个体
# pop = [1 ,3, 0, 2, 4]
# newfit_value = [0.1 , 0.4 , 0.4 , 0.6 , 1.0]
# ms = [0.05 , 0.2 , 0.7 , 0.8 ,0.9]
# if ms[newin] < newfit_value[fitin]
#         0          <          0     newpop[0] = pop[0]
#         1          >          0
#         1          <          1     newpop[1] = pop[1]
#         2          >          1
#         2          >          2
#         2          >          3     
#         2          <          4     newpop[2] = pop[4]
#         3          <          4     newpop[3] = pop[4]
#         4          <          4     newpop[4] = pop[4]