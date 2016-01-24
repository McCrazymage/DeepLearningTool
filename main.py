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
    print fun.calc([2,3,4,5])
