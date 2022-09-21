
''' Defining a vector '''
from random import randint
import numpy as np

class Vector_Col():
    def __init__(self, dim):
        self.dim = dim
        self.vector = [0] * self.dim
    
    def set_vector(self, values: list):
        if len(values) != self.dim:
            print("Wrong input data!")
        else:    
            for i in range(0, self.dim):
                self.vector[i] = values[i]
    
    def get_vector(self):
        print(self.vector)

''' Transpose a vector '''
# Let vector_2 be a row-vector
class Vector():
    
    def __init__(self, dim, vector_type):
        self.dim = dim
        self.vector_type = vector_type
        self.vector = []
        
        
        
    def set_vector(self, values: list):
        if self.vector_type == 'column':
            self.vector = []
            for i in range(0, self.dim):    
                self.vector.append([values[i]])
                
        elif self.vector_type == 'row':
            self.vector = [[]]
            for i in range(0, self.dim):
                self.vector[0].append(values[i])
            
                
            
    def get_values(self):
        
        vector_values = []
        
        if self.vector_type == 'column':
            for i in range(0, self.dim):
                vector_values.append(self.vector[i][0])
        
        elif self.vector_type == 'row':
            for i in range(0, self.dim):
                vector_values.append(self.vector[0][i])
        
        return vector_values
             
    
    
    def transpose(self):
        
        vector_values = self.get_values(self.vector)
        
        if self.vector_type == 'column':
            self.vector_type = 'row'
        
        elif self.vector_type == 'row':
            self.vector_type = 'column'        
        
        self.set_vector(vector_values)
                
    def get_vector(self):
        print(self.vector)


''' Summary, multiplication by scalar, dot-product, vector-product '''
class VectorOper(Vector):
    
    
    
    ''' Returns a vector with 'return', not by setting self.vector '''
    def create_vector(self, values):
        if self.vector_type == 'column':
            result_vector = []
            for i in range(0, self.dim):    
                result_vector.append([values[i]])
                
        elif self.vector_type == 'row':
            result_vector = [[]]
            for i in range(0, self.dim):
                result_vector[0].append(values[i])
        
        return result_vector
    
    
    
    ''' Norm L1 '''
    def L_1(self):
        
        result = 0
        if self.vector_type == 'column':
            for i in range(0, self.dim):
                result += abs(self.vector[i][0])
                
        elif self.vector_type == 'row':
            for i in range(0, self.dim):
                result += abs(self.vector[0][i])
                
        return result
    
    
    
    ''' Norm L2 '''
    def L_2(self):
                
        result = 0
        if self.vector_type == 'column':
            for i in range(0, self.dim):
                result += self.vector[i][0] * self.vector[i][0]
        elif self.vector_type == 'row':
            for i in range(0, self.dim):
                result += self.vector[0][i] * self.vector[0][i]
                
        return np.sqrt(result)
    
    
    
    '''Norm LInf '''
    def L_Inf(self):
        
        if self.vector_type == 'column':
            max_value = self.vector[0][0]
            for i in range(1, self.dim):
                if max_value < self.vector[i][0]:
                    max_value = self.vector[i][0]
            
        elif self.vector_type == 'row':
            max_value = self.vector[0][0]
            for i in range(1, self.dim):
                if max_value < self.vector[0][i]:
                    max_value = self.vector[0][i]
                    
        return max_value
    
    
    
    ''' Sum of two vectors '''
    def v_sum(self, vector, sign='+'):
        if (self.dim == vector.dim) and (self.vector_type == vector.vector_type):
            self_values = self.get_values()
            values = vector.get_values()
            
            if sign == '+':
                for i in range(0, self.dim):
                    self_values[i] += values[i]
            elif sign == '-':
                for i in range(0, self.dim):
                    self_values[i] -= values[i]
                
            return self.create_vector(self_values)
            
        else:
            print("Wrong vector sizes or orientation!")
            
            
            
    ''' Vector times scalar '''
    def sc_mult(self, scalar):
        self_values = self.get_values()
        
        for i in range(0, self.dim):
            self_values[i] *= scalar
    
        return self.create_vector(self_values)
    
    
    
    ''' Dot-product calculation '''
    def dot_product(self, vector):
        if (self.dim == vector.dim) and (self.vector_type != vector.vector_type):
            result = 0
            
            if self.vector_type == 'column':
                for i in range(0, self.dim):
                    result += self.vector[i][0] * vector.vector[0][i]
            
            elif self.vector_type == 'row':
                for i in range(0, self.dim):
                    result += self.vector[0][i] * vector.vector[i][0]
            return result
        else:
            print("Cannot compute dot-product for the chosen vectors!")
    
    
    
    ''' Find angle between two vectors using dot-product '''
    def find_angle(self, vector):
        angle = (self.dot_product(vector)) / (self.L_2() * vector.L_2())
        
        return np.arccos(angle) / 3.1415 * 180
    
    
    
    