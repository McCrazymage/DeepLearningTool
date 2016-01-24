#coding=utf8

import numpy as np


class OpTree(object):
    def __init__(self,op,a,b):
        self.op=op
        self.a=a
        self.b=b
        self.value = None
    
    def __add__(self, other):
        return OpTree.build("add",self,other)
    def __mul__(self, other):
        return OpTree.build("mul",self,other)
    def __radd__(self, other):
        return OpTree.build("radd",other,self)
    def __rmul__(self, other):
        return OpTree.build("rmul",other,self)
    
    def _assign(self, value):
        return OpTree.build("assign",self,other)
    
    
    def __str__(self):
        return str((self.op,str(self.a),str(self.b)))
    @staticmethod
    def build(op, a, b, out=None, **kwargs):
        #=======================================================================
        # print op
        # print a
        # print b
        #=======================================================================
        
        return OpTree(op,a,b)
        
    