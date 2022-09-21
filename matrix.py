class Matrix():
    
    def __init__(self, dim_m, dim_n):
        self.dim_m = dim_m
        self.dim_n = dim_n
        self.matrix = []
        
    ''' Setting values for the matrix '''
    def set_matrix_out(self, rows):
        for m in range(0, self.dim_m):
            self.matrix.append([])
            splitted_str = rows[m].split()
            for n in range(0, self.dim_n):
                temp_value = splitted_str.pop(0)
                self.matrix[m].append(float(temp_value))
    
    def set_matrix_in(self, rows: list):
        self.matrix = []
        for m in range(0, self.dim_m):
            self.matrix.append(rows[m])
        
    def print_matrix(self):
        print("Matrix:")
        for m in range(0, self.dim_m):
            print(self.matrix[m])
    
    ''' Sum of two matrices '''
    def matrix_sum(self, matrix):
        if (self.dim_m == matrix.dim_m) and (self.dim_n == matrix.dim_n):
            for m in range(0, self.dim_m):
                for n in range(0, self.dim_n):
                    self.matrix[m][n] += matrix.matrix[m][n]
        else:
            print("Wrong dimension(s) of matrices!")
            
    ''' Multiplication of matrices '''
    def matrix_mult(self, matrix):
        if (self.dim_n == matrix.dim_m):
            result = []
            for m in range(0, self.dim_m):
                result.append([])
                for nn in range(0, matrix.dim_n):
                    temp_value = 0
                    
                    for n in range(0, self.dim_n):
                        temp_value += self.matrix[m][n] * matrix.matrix[n][nn]
                    
                    result[m].append(temp_value)
                    
            self.matrix = result
                    
        else:
            print("Wrong dimension(s) of matrices!")
    
    ''' Sorting a matrix into echelon form '''
    def sort_matrix_to_echelon(self):
        rows = []
        new_rows = []
        for m in range(0, self.dim_m):
            rows.append(self.matrix[m])
        
            
        for n in range(0, self.dim_n):
            
            is_zero_row = True
            nonzero_rows = []
            print(n)
            print(rows)
            
            for m in range(0, len(rows)):
                if rows[m][n] != 0:
                    nonzero_rows.append(rows[m])
                    
            if nonzero_rows != []:
                for m in range(0, len(nonzero_rows)):
                    new_rows.append(nonzero_rows[m])
                    rows.remove(nonzero_rows[m])
            else:
                if rows != []:
                    for n in range(0, self.dim_n):
                        if rows[0][n] == 0:
                            is_zero_row *= True
                        else:
                            is_zero_row *= False
                            
                    if is_zero_row:
                        new_rows.append(rows[0])
                        rows.pop(0)
                    
        for m in range(0, self.dim_m):
            self.matrix[m] = new_rows[m]
        
        ''' It sorts a matrix to the triangle form '''
    def sort_matrix_to_triangle(self):
        
        rows = []
        new_rows = []
        for m in range(0, self.dim_m):
            rows.append(self.matrix[m])
        
          
        for n in range(0, self.dim_n):
            
            nonzero_rows = []
            is_zero_row = True
            print(n)
            print(rows)
            
            for m in range(0, len(rows)):
                if rows[m][n] != 0:
                    nonzero_rows.append(rows[m])
                    
            if nonzero_rows != []:
                for col_index in range(0, self.dim_n):
                    nonzero_rows[0][col_index] = nonzero_rows[0][col_index] / nonzero_rows[0][n]
                
                new_rows.append(nonzero_rows[0])
                rows.remove(nonzero_rows[0])
                
                for row_index in range(1, len(nonzero_rows)):
                    multiplier = nonzero_rows[row_index][n] / nonzero_rows[0][n] 
                    for col_index in range(0, self.dim_n):
                        nonzero_rows[row_index][col_index] -= nonzero_rows[0][col_index] * multiplier
                    
            else: # process fully zero rows
                if rows != []:
                    for n in range(0, self.dim_n):
                        if rows[0][n] == 0:
                            is_zero_row *= True
                        else:
                            is_zero_row *= False
                            
                    if is_zero_row:
                        new_rows.append(rows[0])
                        rows.pop(0)
                    
        for m in range(0, self.dim_m):
            self.matrix[m] = new_rows[m]
                
            
            
            
            
            
            
            
            