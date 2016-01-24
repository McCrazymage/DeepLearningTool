#coding=utf8

import numpy as np







class op(object):
    def __init__(self):
        pass
    
class add(op):
    def __init__(self):
        pass
    
    
    @staticmethod
    def calc(a,b):
        return a+b
    
    
    @staticmethod
    def gradient(g,a,b):
        return g,g
    
    
class mul(op):
    
    def __init__(self):
        pass
    
    @staticmethod
    def calc(a,b):
        return a*b
    
    @staticmethod
    def gradient(g,a,b):
        return g*b,g*a
    
    
class dot(op):
    
    def __init__(self):
        pass
    
    @staticmethod
    def calc(a,b):
        return a.dot(b)
    
    @staticmethod
    def gradient(g,a,b):
        return g.dot(b.T),a.T.dot(g)