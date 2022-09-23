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
            
    def set_matrix_zeros(self):
        self.matrix = []
        for m in range(0, self.dim_m):
            self.matrix.append([])
            for n in range(0, self.dim_n):
                self.matrix[m].append(0)
    
    def set_matrix_one(self):
        self.matrix = []
        for m in range(0, self.dim_m):
            self.matrix.append([])
            for n in range(0, self.dim_n):
                if m == n:
                    self.matrix[m].append(1)
                else:
                    self.matrix[m].append(0)
                    
    def swap_rows(self, m_1: int, m_2: int):
        temp_row = self.matrix[m_1]
        self.matrix[m_1] = self.matrix[m_2]
        self.matrix[m_2] = temp_row
    
    def swap_cols(self, n_1: int, n_2: int):
        for m in range(0, self.dim_m):
            temp_value = self.matrix[m][n_1]
            self.matrix[m][n_1] = self.matrix[m][n_2]
            self.matrix[m][n_2] = temp_value
        
    def print_matrix(self):
        print("Matrix:")
        for m in range(0, self.dim_m):
            print(self.matrix[m])
            
    def round_values(self, dec: int):
        for m in range(0, self.dim_m):
            for n in range(0, self.dim_n):
                self.matrix[m][n] = round(self.matrix[m][n], dec)
            
    def transpose_matrix(self):
        result = Matrix(self.dim_n, self.dim_m)
        result.set_matrix_zeros()
        for m in range(0, self.dim_n):
            for n in range(0, self.dim_m):
                result.matrix[m][n] = self.matrix[n][m]
        self.matrix = result.matrix
    
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
            
    
    
    ''' Returns matrix without chosen row and column '''
    def reduced_matrix(self, row_ind: int, col_ind: int):
        result = Matrix(self.dim_m - 1, self.dim_n - 1)
        result.set_matrix_zeros()
        row_shift, col_shift = 0, 0
        for m in range(0, self.dim_m - 1):
            col_shift = 0
            if m == row_ind:
                row_shift = 1
            for n in range(0, self.dim_n - 1):
                if n == col_ind:
                    col_shift = 1
                result.matrix[m][n] = self.matrix[m + row_shift][n + col_shift]
        
        return result
    
    
    
    
    ''' This function adds b vector as the last column to the matrix A '''
    def compose_linear_system_matrix(self, b_vect):
        for m in range(0, self.dim_m):
            self.matrix[m].append(b_vect.vector[m][0])
        self.dim_n += 1
        
            
            
    ''' Sorting a matrix into echelon form '''
    def sort_matrix_to_echelon(self):
        rows = []
        new_rows = []
        for m in range(0, self.dim_m):
            rows.append(self.matrix[m])
        
            
        for n in range(0, self.dim_n):
            
            is_zero_row = True
            nonzero_rows = []
            
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
            
            
            
    ''' Support function to find out if a row consists only of zeros '''
    def is_zero_row(self, row: list, stop_index: int) -> bool:
        is_zero_row = True
        if row != []:
            for n in range(0, stop_index):
                if row[n] == 0:
                    is_zero_row *= True
                else:
                    is_zero_row *= False
                    
        return is_zero_row
        
        
        
    ''' Sorts a matrix to the triangle form with 1 on the diagonal positions'''
    def sort_matrix_to_triangle(self):
        
        rows = []
        new_rows = []
        for m in range(0, self.dim_m):
            rows.append(self.matrix[m])
        
          
        for n in range(0, self.dim_n):
            nonzero_rows = []
            
            for m in range(0, len(rows)):
                if rows[m][n] != 0:
                    nonzero_rows.append(rows[m])
                    
            if nonzero_rows != []:
                for col_index in range(0, self.dim_n): # first row converted to [1, ..., ...]
                    nonzero_rows[0][col_index] = nonzero_rows[0][col_index] / nonzero_rows[0][n]
                
                new_rows.append(nonzero_rows[0])
                rows.remove(nonzero_rows[0])
                
                for row_index in range(1, len(nonzero_rows)):
                    multiplier = nonzero_rows[row_index][n] / nonzero_rows[0][n] 
                    for col_index in range(0, self.dim_n):
                        nonzero_rows[row_index][col_index] -= nonzero_rows[0][col_index] * multiplier
                    
            else: # process fully zero rows
                if rows != []:
                    if self.is_zero_row(rows[0], len(rows[0])):
                        new_rows.append(rows[0])
                        rows.pop(0)
                    
        for m in range(0, self.dim_m):
            self.matrix[m] = new_rows[m]
    
    
    
    ''' Solves a system of linear equations if solutions without slider parameters exist'''
    def solve_system(self):
        solutions = []
        if (self.dim_m < self.dim_n - 1):
            print("Can't solve this system (too many variables)!")
        else:
            
            ''' This part of code is working when there is overinformation.
            In this case I delete useless rows by correcting self.matrix.
            Later I change self.dim_m in order not to have 'list out of range' '''
            number_deleted = 0 # number of deleted rows
            if (self.dim_m >= self.dim_n):
                for m in range(0, self.dim_m):
                    if self.is_zero_row(self.matrix[m], self.dim_n - 1):
                        self.matrix.pop(m)
                        number_deleted += 1
            print(f"Number deleted: {number_deleted}")
            self.dim_m -= number_deleted # I deleted one row -> I redefine size of matrix
            
            for m in range(0, self.dim_m):
                if self.matrix[self.dim_m - 1 - m][self.dim_n - 2 - m] == 0: # refer to the last coeff at x_m
                    solutions.insert(0, float('Inf'))  
                else:
                    temp_value = self.matrix[self.dim_m - 1 - m][self.dim_n - 1] # refer to the b_m (Ax = b)
                    for n in range(0, m):
                        temp_value -= self.matrix[self.dim_m - 1 - m][self.dim_n - 2 - n] * solutions[-n - 1] # we take solutions from the end
                    solutions.insert(0, temp_value)
                    
        return solutions
    
    
    
    ''' Performs LU-decomposition '''
    def LU_dec(self) -> list:
        if self.dim_m != self.dim_n:
            print("Dimensions are wrong for this method!")
        else:
            D = self.dim_m
            L = Matrix(D, D)
            L.set_matrix_zeros()
            
            U = Matrix(D, D)
            U.set_matrix_one()
            
            L.matrix[0][0] = self.matrix[0][0]
            
            for iter_number in range(1, D):
                
                for n in range(0, iter_number + 1):
                    L.matrix[iter_number][n] = self.matrix[iter_number][n]
                    U.matrix[n][iter_number] = self.matrix[n][iter_number]
                    
                    for sum_ind in range(0, n):
                        L.matrix[iter_number][n] -= L.matrix[iter_number][sum_ind] * U.matrix[sum_ind][n]
                        U.matrix[n][iter_number] -= L.matrix[n][sum_ind] * U.matrix[sum_ind][iter_number]
                    
                    if L.matrix[n][n] == 0:
                        U.matrix[n][iter_number] = float('nan')
                    else:
                        U.matrix[n][iter_number] = U.matrix[n][iter_number] / L.matrix[n][n]
                    
            result = [L, U]
            return result
        
    
    
    ''' Performs LU-decomposition for calculating determinant'''
    def LU_dec_swap(self) -> list:
        if self.dim_m != self.dim_n:
            print("Dimensions are wrong for this method!")
        else:
            temp = Matrix(self.dim_m, self.dim_m)
            temp.matrix = []
            for m in range(0, self.dim_m):
                temp.matrix.append([])
                for n in range(0, self.dim_m):
                    temp.matrix[m].append(self.matrix[m][n])
            for swap_index in range(0, self.dim_m):
                temp.swap_rows(0, swap_index)
                temp.swap_cols(0, swap_index)
                D = temp.dim_m
                L = Matrix(D, D)
                L.set_matrix_zeros()
                
                U = Matrix(D, D)
                U.set_matrix_one()
                
                L.matrix[0][0] = temp.matrix[0][0]
                
                for iter_number in range(1, D):
                    
                    for n in range(0, iter_number + 1):
                        L.matrix[iter_number][n] = temp.matrix[iter_number][n]
                        U.matrix[n][iter_number] = temp.matrix[n][iter_number]
                        
                        for sum_ind in range(0, n):
                            L.matrix[iter_number][n] -= L.matrix[iter_number][sum_ind] * U.matrix[sum_ind][n]
                            U.matrix[n][iter_number] -= L.matrix[n][sum_ind] * U.matrix[sum_ind][iter_number]
                        
                        if L.matrix[n][n] == 0:
                            L.set_matrix_zeros()
                            break
                        
                        U.matrix[n][iter_number] = U.matrix[n][iter_number] / L.matrix[n][n]
                        # if n == iter_number:
                        #     U.matrix[n][iter_number] = 1
                            
                    
                nonzero = True
                for m in range(0, D):
                    if L.matrix[m][m] == 0:
                        nonzero *= False
                        break
                    
                if nonzero:
                    result = [L, U]
                    return result
                            
                if swap_index == (D - 1):
                    result = [L, U]
                    return result
        
        
        
    ''' Computes Det() of a matrix on the basis of LU decomposition'''    
    def det_LU(self):
        if self.dim_m != self.dim_n:
            print("Dimensions are wrong for this method!")
        else:
            result = 1
            D = self.dim_m
            LU = self.LU_dec_swap()
            for m in range(0, D):
                result *= LU[0].matrix[m][m]
                
        return result
    
    
    ''' Recursively calculates determinant '''
    def det(self):
        if self.dim_m != self.dim_n:
            print("Dimensions are wrong for this method!")
        else:
            if self.dim_m == 1:
                return self.matrix[0][0]
            else:
                row_sum = 0
                for n in range(0, self.dim_n):
                    row_sum += (-1)**(n) * self.matrix[0][n] * self.reduced_matrix(0, n).det()
                return row_sum
    
    
    
    ''' Inverses matrix '''
    def matrix_inverse(self):
        if self.dim_m != self.dim_n:
            print("Dimensions are wrong for this method!")
        else:
            D = self.dim_m
            # Det = round(self.det(), 2)
            Det = self.det()
            print(f"Det = {Det}")
            temp = Matrix(D, D)
            temp.set_matrix_in(self.matrix)
            self.transpose_matrix()
            print("Transposed:")
            self.print_matrix()
            
            if Det == 0:
                print("Matrix has Det = 0!")
                temp.set_matrix_zeros()
                
            else:
                for m in range(0, D):
                    for n in range(0, D):
                        # temp.matrix[m][n] = (-1)**(m+n) * round(self.reduced_matrix(m, n).det(), 2)
                        temp.matrix[m][n] = (-1)**(m+n) * self.reduced_matrix(m, n).det()
                        print(f"Reduced Det[m = {m}][n = {n}] = {(-1)**(m+n) * round(self.reduced_matrix(m, n).det(), 2)}")
                        print(f"Reduced matrix [m = {m}][n = {n}] = {self.reduced_matrix(m, n).print_matrix()}")
                
                for m in range(0, D):
                    for n in range(0, D):
                        self.matrix[m][n] = temp.matrix[m][n] / Det
            
              
            
            
            
            
            
            
            
            