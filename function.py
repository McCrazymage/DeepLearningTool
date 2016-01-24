#coding=utf8


import numpy as np
from OPTree import *
from Tensor import *
from ops import *


class function():
    def __init__(self,inputs,outputs):
        assert isinstance(inputs,list)
        assert isinstance(outputs,list) or isinstance(outputs,Tensor)
        
        self.inputs = inputs
        self.outputs = outputs

    def gradient(self, inputs):
        assert len(inputs) == len(self.inputs)
        for x1,x2 in zip(inputs,self.inputs):
            if isinstance(x1,np.ndarray):
                x2.grad = np.zeros(x1.shape)
            else:
                x2.grad = 0
        
        self.calc(inputs)
        for output in self.outputs:
            if isinstance(output,np.ndarray):
                output.grad = np.ones(output.shape)
            else:
                output.grad = 1
            self._gradient(output)
            
        return [x.grad for x in self.inputs]

    def _gradient(self,output):
        g1,g2= globals()[output.op].gradient(output.grad, output.a.value,output.b.value)
        output.a.grad += g1
        output.b.grad += g2
        if isinstance(output.a,OpTree):
            self._gradient(output.a)
        if isinstance(output.b,OpTree):
            self._gradient(output.b)
        
    def calc(self, inputs):
        assert len(inputs) == len(self.inputs)
        for in1,in2 in zip(inputs,self.inputs):
            in2.value = in1
        
        if isinstance(self.outputs,list):
            for output in self.outputs:
                self._calc(output)
            return [out.value for out in self.outputs]
        else:
            self._calc(self.outputs)
            return self.outputs.value
            
    def _calc(self,output):
        if isinstance(output.a,OpTree) and output.a.value is None:
            self._calc(output.a)
        if isinstance(output.b,OpTree) and output.b.value is None:
            self._calc(output.b)
            
        output.value = globals()[output.op].calc(output.a.value,output.b.value)  
        if isinstance(output.value, np.ndarray):
            output.grad = np.zeros(output.value.shape)
        else:
            output.grad = 0
         
        #=======================================================================
        # if output.op == 'mul' or output.op == 'rmul':
        #     output.value = output.a.value*output.b.value
        # if output.op == 'add' or output.op == 'radd':
        #     output.value = output.a.value+output.b.value
        #=======================================================================
            
            