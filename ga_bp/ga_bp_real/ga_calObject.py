'''
Created on 2017年11月21日

@author: ljs
'''
from ga_bp_real.bp_train import bp_train 

def ga_calObject(x):
    obj = []
    #x是整个种群，xi是每个个体
    for xi in x:    
        temp = bp_train(xi)
        obj.append(temp)
    return obj
  
if __name__ == '__main__':
    pass