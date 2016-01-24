#coding=utf8


import numpy as np
from OPTree import *
from Tensor import *
from function import *








if __name__ == '__main__':
    a = Tensor('a')
    b = Tensor('b')
    c = Tensor('c')
    d = Tensor('d')
    
    f = a*d+b*c
    print f,type(f)
    fun = function([a,b,c,d],[f])
    
    x1 = np.ones((3,5))
    x2 = 2*np.ones((3,5))
    x3 = 3*np.ones((3,5))
    x4 = 4*np.ones((3,5))
    
    print fun.calc([x2,x3,x4,x1])
