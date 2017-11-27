'''
Created on 2017年11月23日

@author: ljs
'''
def ga_replace(result,pop,x):
    i = x.index(min(x))
    x[i] = result[0]
    pop[i] = result[2]
        
if __name__ == '__main__':
    pass