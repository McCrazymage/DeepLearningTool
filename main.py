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
    
    f = a.dot(b)+c
    g = a*b+d*c
    print f,type(f)
    fun = function([a,b,c,d],[f])
    
    x1 = np.ones((1,5))
    x2 = 2*np.ones((5,1))
    x3 = 3*np.ones((1,1))
    x4 = 4*np.ones((2,1))
    
    print fun.calc([x1,x2,x3,x4])
    print fun.gradient([x1,x2,x3,x4])
