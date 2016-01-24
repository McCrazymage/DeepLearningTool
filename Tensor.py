#coding=utf8


import numpy as np
from OPTree import OpTree


class Tensor(object):
    def __init__(self,name):
        self.name = name
        self.value = None
    def __str__(self):
        return self.name
    def __add__(self, other):
        return OpTree.build("add",self,other)
    def __mul__(self, other):
        return OpTree.build("mul",self,other)
    def __radd__(self, other):
        return OpTree.build("radd",other,self)
    def __rmul__(self, other):
        return OpTree.build("rmul",other,self)