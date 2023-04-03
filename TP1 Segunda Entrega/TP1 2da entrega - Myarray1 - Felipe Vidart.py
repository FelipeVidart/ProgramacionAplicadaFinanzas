# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 16:26:57 2023

@author: vidar
"""

class Myarray1:
    """MyArray1 es un objeto que permite operar con matrices. Desde crear matrices
    hasta modificarlas, multiplicarlas o ver columnas/filas específicas. Las matrices
    no se almacenan como lista de listas"""
    def __init__(self, rows, columns, elements, by_row = bool):
        if len(elements) != (rows * columns):
            return print('ERROR: La cantidad de elementos introducidos no coincide con la cantidad de elementos de la matriz')
        self.elems = list(elements)
        self.r = rows
        self.c = columns
        self.by_row = by_row
     
    def get_pos(self, j, k):
        """La funcion get_pos busca dentro de la lista que representa la matriz la posicion de la coordenada
        (j, k) en la matriz. Tiene como parametros j (numero de filas) y k (numero de columnas). Devuelve 
        la posicion de esa coordenada en la lista que representa la matriz"""
        if j > self.r:
            print(f'La fila introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
            indice = None
        if k > self.c:
            print(f'La columna introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
            indice = None
        if self.by_row == True:
            indice = (self.c * (j-1)) + k
        elif self.by_row == False:
            indice = (self.r * (k-1)) + j
        return indice

    def get_coords(self, m):
        """La funcion get_coords busca y devuelve las coordenadas de un indice de la lista que 
        se introduce en los parametros. Al introducirse el numero debe introducirse teniendo
        en cuenta que el programa cuenta el primer elemento de la lista como 1 y no como 0, es 
        decir que si se quiere obtener el indice de la lista 4 en el sentido que lo lee python debe
        introducirse el numero 5"""
        if m > len(self.elems) or m <= 0:
            print('ERROR: El numero introducido no se encuentra dentro de la lista')
            coord = None
        else:
            m -= 1
            if self.by_row == True:
                row = (m // self.c)
                col = (m - row*self.c)
                coord = (row + 1, col + 1)
            elif self.by_row == False:
                col = (m // self.r) 
                row = (m - col*self.r)  
                coord = (row + 1, col + 1)
        return coord
        
    def switch(self):
        """La funcion switch cambia el modo de atravesar la matriz. Cada vez que switch sea usada se 
        cambiará a columna o fila, según corresponda, y se devolverá un objeto con las filas cambiadas 
        y el booleano by_row cambiado"""
        new_matrix = []
        if self.by_row == True:
            for i in range(self.c):
                new_matrix.extend(self.elems[j*self.c+i] for j in range(self.r))
        elif self.by_row == False:
            for i in range(self.r):
                new_matrix.extend(self.elems[j*self.r+i] for j in range(self.c))
        return Myarray1(self.r, self.c, new_matrix, not self.by_row)
        
    def to_by_row(self):
        """to_by_row sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por fila. Dentro del programa la usa para llamarla desde otros metodos y sirve para facilitar 
        el indexado de la matriz cuando convenga indexarla por filas. Devuelve la matriz leida por filas"""
        if self.by_row == True:
            matrix = self.elems
        elif self.by_row == False:
            matrix = self.switch().elems
        return matrix
        
    def to_by_column(self):
        """to_by_column sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por cp;i,ma. Dentro del programa la usa para llamarla desde otros metodos y sirve para facilitar 
        el indexado de la matriz cuando convenga indexarla por columnas. Devuelve la matriz leida por columnas"""
        if self.by_row == False:
            matrix = self.elems
        elif self.by_row == True:
            matrix = self.switch().elems
        return matrix
    
    def return_byrow(self, new_matrix):
        """De manera similar a to_by_row, return_byrow convierte el return de un metodo que trabaja con la 
        matriz en by_row a by_column si es necesario o lo deja en by_row. Su uso es interno de la instancia, se 
        usa para no repetir el mismo codigo al final de todas las funciones"""
        if self.by_row == True:
            new_object = Myarray1(self.r, self.c, new_matrix, self.by_row)
        if self.by_row == False:
            #pongo not self.by_row para que quede en el que ya estaba, porque switch lo cambia.
            aux_object = Myarray1(self.r, self.c, new_matrix, not self.by_row)
            new_object = aux_object.switch()
        return new_object
        
    def return_bycolumn(self, new_matrix):
        """De manera similar a to_by_column, return_bycolumn convierte el return de un metodo que trabaja con la 
        matriz en by_column a by_row si es necesario o lo deja en by_column. Su uso es interno de la instancia, se 
        usa para no repetir el mismo codigo al final de todas las funciones"""
        if self.by_row == False:
            new_object = Myarray1(self.r, self.c, new_matrix, self.by_row)
        if self.by_row == True:
            aux_object = Myarray1(self.r, self.c, new_matrix, not self.by_row)
            new_object = aux_object.switch()
        return new_object
    
    def eye(self, n):
        """eye es una funcion usada para crear matrices idendidad de NxN. El unico parametro es N e indica el 
        numero de columnas y filas de la matriz identidad (ya que debe ser cuadrada). Devuelve una nueva instancia
        de la clase Myarray1 formada por la matriz identidad, sus columnas y filas y el booleano by_row (de todas 
        formas leer la matriz identidad por filas o columnas es igual)"""
        elems, flat = [[0] * i + [1] + [0] * (n - i - 1) for i in range(n)], []
        for i in elems:
            flat.extend(i)
        return Myarray1(n, n, flat, True)
        
    def get_row(self, j):
        """La funcion get_row recibe un numero, j, y devuelve la fila que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las filas introducidas"""
        matrix = self.to_by_row()
        if type(j) == list:
            submatrix = []
            for i in j:
                if i > self.r:
                    print('ERROR: Una de las filas introducidas no se encuentra en la matriz')
                    submatrix = None
                else:
                    submatrix.extend(matrix[(self.c * (i-1)): (self.c * (i-1) + self.c)])    
            end = submatrix
        elif type(j) == int:
            if j > self.r:
                print('ERROR: La fila introducida no se encuentra en la matriz')
                end = None
            else:
                end = list(matrix[(self.c*(j-1)): ((self.c*(j-1)) + self.c)])
        else:
            print('j debe ser un entero o una lista')
        return end
     
    def get_col(self, k):
        """La funcion get_col recibe un numero, k, y devuelve la columna que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las columnas introducidas"""
        matrix = self.to_by_column()
        if type(k) == list:
            submatrix = []
            for i in k:
                if i > self.c:
                    print('ERROR: Una de las columnas introducidas no se encuentra en la matriz')
                    submatrix = None
                else:
                    submatrix.extend(matrix[(self.r * (i-1)): (self.r * (i-1) + self.r)])
            end = submatrix
        elif type(k) == int:
            if k > self.c:
                print('ERROR: La columna introducida no se encuentra en la matriz')
                end = None
            else:
                end = list(matrix[(self.r*(k-1)): ((self.r*(k-1)) + self.r)])    
        else:
            print('j debe ser un entero o una lista')
        return end
    
    def get_elem(self, j, k):
        """La funcion get_elem recibe dos numeros, j y k, y devuelve el elemento que se encuentra en
        la fila y columna que esos numeros representan respectivamente"""
        if j > self.r:
            print(f'La fila introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
            m = None
        if k > self.c:
            print(f'La columna introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
            m = None
        else:
            m = self.elems[(self.get_pos(j, k))-1] 
        return m

    def del_row(self, j):
        """La funcion del_row recibe un numero, j, que representa una fila de la matriz. La funcion elimina
        esa fila de la matriz y devuelve un objeto cuya matriz no tiene esa fila"""
        if j > self.r:
            print(f"ERROR: La fila que quiere eliminar no está en la matriz, la fila solo tiene {self.r} filas")
            new_object = None
        else:
            matrix = self.to_by_row()
            new_matrix = matrix[0: (self.c * (j-1))] + matrix[(self.c * (j-1)) + self.c:]
            #le saco 1 a self.c momentaneamente para que el nuevo objeto se cree correctamente
            self.r -= 1
            new_object = self.return_byrow(new_matrix)
            self.r += 1
        return new_object
    
    def del_row_eye(self, j):
        """Al igual que del_row, del_row_eye elimina una fila j de la matriz. Lo que diferencia ambos métodos es que 
        en este caso la elimina premultiplicando la matriz original por una matriz identidad con una fila eliminada"""
        if j > self.r:
            print(f"ERROR: La fila que quiere eliminar no está en la matriz, la fila solo tiene {self.r} filas")
            end = None
        else:
            aux_instance = Myarray1(self.r, self.c, self.to_by_row(), True)
            identity = self.eye(self.r)
            updated_identity = identity.del_row(j)
            deleted =  updated_identity @ aux_instance
            #tengo que cambiar las rows antes de crear el return porque sino me tira error el init, despues las devuelvo a como estaban
            originalrows, newrows = self.r, self.r - 1
            self.r = newrows
            end = self.return_byrow(deleted).elems
            self.r = originalrows
        return end 
    
    def del_col(self, k:int, matrix_input = None):
        """La funcion del_col recibe un numero, k, que representa una columna de la matriz. La funcion elimina
        esa columna de la matriz y devuelve un objeto cuya matriz no tiene esa columna. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro"""
        if k > self.c:
            print(f"ERROR: La columna que quiere eliminar no está en la matriz, la fila solo tiene {self.c} columnas")
            new_object = None
        else:
            matrix = self.to_by_column()
            new_matrix = matrix[0: (self.r * (k-1))] + matrix[(self.r * (k-1)) + self.r:]
            self.c -= 1
            new_object = self.return_bycolumn(new_matrix)
            self.c += 1
        return new_object
    
    def del_col_eye(self, m):
        """Al igual que del_col, del_col_eye elimina una columna k de la matriz. Lo que diferencia ambos métodos es que 
        en este caso la elimina premultiplicando la matriz original por una matriz identidad con una columna eliminada"""
        if m > self.c:
            print(f"ERROR: La columna que quiere eliminar no está en la matriz, la fila solo tiene {self.c} columnas")
            end = None
        else:
            matrix = self.to_by_row()
            aux_instance = Myarray1(self.r, self.c, matrix, True)
            identity = self.eye(self.c)
            updated_identity = identity.del_col(m)
            deleted =  aux_instance @ updated_identity
            originalcols, newcols = self.c, self.c - 1
            self.c = newcols
            end = self.return_byrow(deleted).elems
            self.c = originalcols
        return end
    
    def swap_rows(self, j:int, k:int):
        """La funcion swap_rows recibe como parametros dos numeros, j y k. Estos numeros representan dos 
        filas en la matriz. Su funcion es devolver un objeto con la misma matriz pero con las filas j y k intercambiadas
        Para que funcione correctamente, se debe introducir una j < k"""
        if j > k:
            inputj, inputk = j, k
            k, j = inputj, inputk
        if j > self.r or k > self.r:
            print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            new_object = None
        matrix = self.to_by_row()
        row_j, row_k = self.get_row(j), self.get_row(k)
        new_matrix = []
        row_counter = 1
        for i in range(0, len(matrix), self.c):
            if row_counter == j:
                new_matrix.extend(row_k)
            elif row_counter == k:
                new_matrix.extend(row_j)
            else:
                new_matrix.extend(matrix[i: i+self.c])
            row_counter += 1
        new_object = self.return_byrow(new_matrix)
        return new_object
    
    def swap_rows_eye(self, j, k):
        """Al igual que swap_row, swap_rows_eye intercambia dos filas, j y k, de una matriz. Lo que diferencia ambos métodos 
        es que en este caso las intercambia premultiplicando la matriz original por una matriz identidad con las respectivas
        filas intercambiadas"""    
        if j > self.r or k > self.r:
            print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            end = None
        else:
            matrix = self.to_by_row()
            aux_instance = Myarray1(self.r, self.c, matrix, True)
            identity = self.eye(self.r)
            counter = 1
            rowj, rowk = identity.get_row(j), identity.get_row(k)
            for i in range(0, len(identity.elems), identity.r):
                if counter == j:
                    identity.elems[i: i+identity.r] = rowk
                elif counter == k:
                    identity.elems[i: i+identity.r] = rowj
                counter += 1
            swapped = identity @ aux_instance
            end = self.return_byrow(swapped).elems
        return end
    
    def swap_cols(self, l:int, m:int):
        """La funcion swap_cols recibe como parametros dos numeros, l y m. Estos numeros representan dos columnas en 
        la matriz. Su funcion es devolver un objeto conla misma matriz pero con las columnas l y m intercambiadas"""
        if l > m:
            inputl, inputm = l, m
            m, l = inputl, inputm
        if l > self.c or m > self.c:
            print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            new_object = None
        else:
            matrix = self.to_by_column()
            col_l = self.get_col(l)
            col_m = self.get_col(m)
            new_matrix = []
            col_counter = 1
            for i in range(0, len(matrix), self.r):
                if col_counter == l:
                    new_matrix.extend(col_m)
                elif col_counter == m:
                    new_matrix.extend(col_l)
                else:
                    new_matrix.extend(matrix[i: i+self.r])
                col_counter += 1
            new_object = self.return_bycolumn(new_matrix)
        return new_object
    
    def swap_cols_eye(self, l, m):
        """Al igual que swap_cols, swap_cols_eye intercambia dos columnas, l y m, de una matriz. Lo que diferencia ambos métodos 
        es que en este caso las intercambia premultiplicando la matriz original por una matriz identidad con las respectivas
        filas intercambiadas"""  
        if l > m:
            inputl, inputm = l, m
            m, l = inputl, inputm
        if l > self.c or m > self.c:
            print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            end = None
        else:
            matrix = self.to_by_row()
            aux_instance = Myarray1(self.r, self.c, matrix, True)
            identity = self.eye(self.c)
            counter = 1
            rowl, rowm = identity.get_row(l), identity.get_row(m)
            for i in range(0, len(identity.elems), identity.r):
                if counter == l:
                    identity.elems[i: i+identity.r] = rowm
                elif counter == m:
                    identity.elems[i: i+identity.r] = rowl
                counter += 1
            swapped = aux_instance @ identity
            end = self.return_byrow(swapped).elems
        return end
    
    def scale_row(self, j: int, x: int, matrix_input = None):
        """ La funcion scale_row toma por argumentos dos numeros, j y x, j representando una fila de la
        matriz y x un factor. Devuelve la misma matriz pero con la fila j multiplicada por x. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. X debe
        ser un entero y j debe estar dentro de la matriz """
        if type(x) != int:
            print(f"ERROR: X debe ser un entero y se ha introducido: {type(x)}")
            new_object = None
        if j > self.r:
            print(f"ERROR: La fila introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
            new_object = None
        else:
            matrix = self.to_by_row()
            scaled_row = []
            scaled_row.extend(i*x for i in self.get_row(j))
            new_matrix = matrix[:(self.c * (j-1))] + scaled_row + matrix[(self.c * (j-1)) + self.c:]
            new_object = self.return_byrow(new_matrix)
        return new_object 
    
    def scale_col(self, k: int, y: int, matrix_input = None):
        """La funcion scale_col toma como argumento dos enteros. k representa una columna e y un numero entero. La funcion
        multiplica esa columna especifica por y y devuelve la matriz completa con esa fila multiplicada por y. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. Y debe ser un entero 
        y k debe estar dentro de la matriz """
        if type(y) != int:
            print(f"ERROR: K debe ser un entero y se ha introducido: {type(k)}")
            new_object = None
        if k > self.c:
            print(f"ERROR: La columna introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
            new_object = None
        else:
            matrix = self.to_by_column()
            scaled_column = []
            scaled_column.extend(i*y for i in self.get_col(k))
            new_matrix = matrix[:(self.r * (k-1))] + scaled_column + matrix[(self.r * (k-1)) + self.r:]
            new_object = self.return_bycolumn(new_matrix)
        return new_object

    def transpose(self):
        """Esta funcion transpone la matriz. La funcion modifica la instancia de la matriz, cambiando la lista de 
        elementos e intercambiando el numero de filas y el número de columnas"""
        self.elems = self.switch().elems
        rows, columns = self.r, self.c
        self.r, self.c = columns, rows
        return print(f"Ahora la matriz es {self.elems}, de dimension {self.r}x{self.c}")
        
    def flip_rows(self):
        """La funcion flip rows da vuelta especularmente las filas de la matriz y devuelve una copia de ese
        objeto con las filas dadas vuelta"""
        new_instance = Myarray1(self.r, self.c, self.elems.copy(), self.by_row)
        #este for es para iterar en los elementos que tengan que ser cambiados, si la matriz es impar el elemento del medio no se cambia
        for i in range(1, (new_instance.r//2) + 1):
            if 0 < i < new_instance.r:
                new_instance.elems = new_instance.swap_rows(i,new_instance.r-i+1).elems
        return new_instance.elems
    
    def flip_cols(self):
        """La funcion flip cols da vuelta especularmente las columnas de una funcion y devuelve
        una copia de la misma con las columnas dadas vuelta"""
        new_instance = Myarray1(self.r, self.c, self.elems.copy(), self.by_row)
        for i in range(1, (new_instance.c//2)+1):
            if 0 < i < new_instance.c:
                new_instance.elems = new_instance.swap_cols(i, new_instance.c-i+1).elems
        new_object = self.return_bycolumn(new_instance.elems)
        return new_object.elems

    def det(self, matrix_input = None, rows = None, columns = None):
        """det es una funcion que calcula el determinante de una matriz recursivavmente.
        Se puede calcular el determinante de la matriz de una instancia o de una matriz
        cualquiera que se introduce como parámetro. Se debe indicar el numero de columnas
        y de filas de esta matriz, de lo contrario, el programa supondrá que es del mismo
        tamaño que la matriz de la instancia y podrá fallar. Sólo se puede calcular el
        determinante de una matriz cuadrada, si la matriz no es cuadrada la función dará
        error"""
        if self.r != self.c:
            print('ERROR: No se puede calcular el determinante de una matriz que no es cuadrada')
            det = None
        else:
            if matrix_input == None: #si no se incluyen parametros en la call
                matrix, rows, columns = Myarray1(self.r, self.c, self.elems, self.by_row), self.r, self.c
            if matrix_input != None: #si se incluyen parametros en la call (se llama recursivamente)
                matrix = Myarray1(rows, columns, matrix_input, self.by_row)
            if rows == 2 and columns == 2: #caso base
                matrix_end = matrix.elems
                det = matrix_end[0]*matrix_end[3] - matrix_end[1]*matrix_end[2]
            else:
                first_row = matrix.get_row(1)
                det = 0
                col_counter = 0
                for i in range(0,columns):
                    element = first_row[i] #agarro el primer elemento de la primera fila para multiplicar por el determinante
                    new_matrix = []
                    for a in range(2, rows+1):
                        row = matrix.get_row(a) #para todas las filas menos la primera busco la fila
                        if len(row) > 1:
                            row.pop(col_counter) #a la row le saco el elemento que no entra en el determinante de 2x2
                            new_matrix.extend(row) #agrego la lista a a new matrix, me queda la matriz de 2x2
                        elif len(row) <= 1:
                            break
                    col_counter += 1
                    #parte recursiva
                    det += element * ((-1)**(1+col_counter)) * self.det(new_matrix, rows-1, columns-1)
        return det
    
    def inverse(self):
        """inverse es un método de Myarray1 que busca la inversa de la matriz. Busca la inversa con la siguiente
        fórmula (siendo A la matriz y cof(A)T la matriz de cofactores de A traspuesta):
        Inversa = 1/det(A) * cof(A)T"""
        if self.r == self.c and self.det() != 0: #para poder calcular la inversa de una matriz debe ser cuadrada y el determinante debe ser distinto de 0
            matrix = self.to_by_row()
            cofactors_matrix = []
            for i in range(1, len(matrix)+1):
                aux_instance = Myarray1(self.r, self.c, matrix, True) #hago una instancia auxiliar
                coords = aux_instance.get_coords(i) #busco las cordenadas de cada elemento y le elimino esa fila y esa columna para obtener la primer submatriz
                deletedrow = aux_instance.del_row(coords[0])
                deletedcolandrow = deletedrow.del_col(coords[1]) 
                determinant = deletedcolandrow.det() * ((-1)**(coords[1]+coords[0])) #calculo el determinante de la submatriz que quedo sin esa columna y esa fila, multiplico por (-1) ** row*column para que queden bien los signos
                cofactors_matrix.append(determinant) #appendeo cada determinante (cofactor) a la matriz de cofactores
            main_instance = Myarray1(self.r, self.c, matrix, True) #creo la instancia a la que le voy a calcular el determinante
            cofactors_instance = Myarray1(self.r, self.c, cofactors_matrix, True) #creo una instancia cuyo elems es la matriz de cofactores y hago la traspuesta
            cofactors_instance.transpose()
            matrix_det = main_instance.det()
            inverse = (1/matrix_det)*cofactors_instance #busco la inversa y la paso a by_row o by_column según se necesite
            end = self.return_byrow(inverse).elems
        else:
            print('No se puede calcular la inversa de la matriz ya sea porque no es cuadrada o porque su determinante es igual a 0')
            end = None
        return end
    
    def __add__(self, other):
        """Redefinicion del special method __add__. Suma elemento a elemento una matriz o un entero en caso de ser necesario"""
        if isinstance(other, int) or isinstance(other, float):
            end = [element + other for element in self.elems]
        if isinstance(other, type(self)):
            matrix1, matrix2 = self.to_by_row(), other.to_by_row()
            paired = list(zip(matrix1, matrix2))
            aux_end = [sum(tupla) for tupla in paired]
            end = self.return_byrow(aux_end).elems
        return end
    
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self + other
    
    def __sub__(self, other):
        """Redefinicion del special method __add__. Resta elemento a elemento una matriz o un entero en caso de ser necesario"""
        if isinstance(other, int) or isinstance(other, float):
            end = [element - other for element in self.elems]
        if isinstance(other, type(self)):
            matrix1, matrix2 = self.to_by_row(), other.to_by_row()
            paired = list(zip(matrix1, matrix2))
            aux_end = [tupla[0] - tupla[1] for tupla in paired]
            end = self.return_byrow(aux_end).elems
        return end
    
    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self - other

    def __mul__(self, other):
        """Redefinicion del special method __mul__. Multiplica elemento a elemento una matriz o un escalar"""
        if isinstance(other, int) or isinstance(other, float):
            end = [element * other for element in self.elems]
        if isinstance(other, type(self)):
            matrix1, matrix2 = self.to_by_row(), other.to_by_row()
            paired = list(zip(matrix1, matrix2))
            aux_end = [tupla[0] * tupla[1] for tupla in paired]
            end = self.return_byrow(aux_end).elems
        return end
        
    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self * other
        
    def __matmul__(self, other):
        """Redefinicion del special method __matmul__. Lleva a cabo la multiplicacion entre matrices"""
        if isinstance(other, type(self)):
            if self.c == other.r:
                matrix1, matrix2 = self.to_by_row(), other.to_by_column()
                #voy a multiplicar la matriz1 y la matriz2 para tenerlas repetidas y poder zipear las filas y columnas segun corresponda
                mult_matrix1 = []
                for i in range(0, len(matrix1), self.c):
                    mult_row = matrix1[i:i+self.c] * other.c
                    mult_matrix1.append(mult_row)
                mult_matrix2 = [matrix2]*self.c
                counter = 0
                zippedmatrices = []
                for i in mult_matrix1:
                        ziprow = list(zip(i, mult_matrix2[counter]))
                        for a in range(0, len(matrix2), self.c):
                            zippedmatrices.append(ziprow[a: a+other.r])
                        counter += 1
                auxmatrix = []       
                for element in zippedmatrices:
                    auxmatrix.append(list(map(lambda x: x[0]*x[1],element)))
                aux_finalmatrix = list((sum(elements) for elements in auxmatrix))
                #tengo que cambiar el numero de columnas y filas sino me da error, despues lo pongo como estaba
                originalrows, originalcolumns, newrows, newcolumns = self.r, self.c, other.c, self.r
                self.r, self.c = newrows, newcolumns
                print(aux_finalmatrix, self.r, self.c)
                finalmatrix = self.return_byrow(aux_finalmatrix).elems
                self.r, self.c = originalrows, originalcolumns
            else:
                print('La cantidad de columnas de la primera matriz no coincide con la cantidad de filas de la segundo')
                finalmatrix = None
            return finalmatrix
    
    def __pow__(self, other):
        """Redefinicion del special method __pow__. Solo funciona con enteros, eleva la matriz a un entero"""
        if isinstance(other, int):
            matrix = self.to_by_row()
            aux_instance = Myarray1(self.r, self.c, matrix, True)
            changing_aux_instance = Myarray1(self.r, self.c, matrix, True)
            for i in range(other-1):
                matrix = changing_aux_instance @ aux_instance
                changing_aux_instance = Myarray1(self.r, self.c, matrix, True)
            aux_matrix = changing_aux_instance.elems
            matrix = self.return_byrow(aux_matrix).elems
        return matrix
    
#%%

if __name__ == "__main__":
    matriz1 = Myarray1(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12], True)
    matriz2 = Myarray1(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], False)
    
    print('Get pos con by_row True: ', matriz1.get_pos(2, 3))
    print('Get pos con by_row False: ', matriz2.get_pos(2, 3))
    
    print('Get coords con by_row True: ', matriz1.get_coords(3))
    print('Get coords con by_row False: ', matriz2.get_coords(3))
    
    test_matriz1 = matriz1.switch()
    test_matriz2 = matriz2.switch()
    print('Switch con byrow True: ', test_matriz1.__dict__)
    print('Switch con byrow False: ', test_matriz2.__dict__)
    
    print('Get row con byrow True: ', matriz1.get_row(3))
    print('Get row con byrow False: ', matriz2.get_row(3))
    print('Get row (version submatriz) con byrow True: ', matriz1.get_row([3, 4]))
    print('Get row (version submatriz) con byrow False: ', matriz2.get_row([3, 4]))
    
    print('Get col con byrow True: ',matriz1.get_col(3))
    print('Get col con byrow False: ',matriz2.get_col(3))
    print('Get col (version submatriz) con byrow True: ',matriz1.get_col([2, 3]))
    print('Get col (version submatriz) con byrow False: ',matriz2.get_col([2, 3]))
    
    print('Get elem con  byrow True: ', matriz1.get_elem(3, 1))
    print('Get elem con byrow False: ', matriz2.get_elem(3, 1))
    
    test_matriz3 = matriz1.del_row(2)
    test_matriz4 = matriz2.del_row(2)
    print('Del row con byrow True: ', test_matriz3.__dict__)
    print('Del row con byrow False: ', test_matriz4.__dict__)
    
    test_matriz3 = matriz1.del_col(2)
    test_matriz4 = matriz2.del_col(2)
    print('Del col con byrow True: ', test_matriz3.__dict__)
    print('Del col con byrow False: ',test_matriz4.__dict__)

    test_matriz5 = matriz1.swap_rows(2, 3)
    test_matriz6 = matriz2.swap_rows(2, 3)
    print('Swap rows con byrow True: ', test_matriz5.__dict__)
    print('Swap rows con byrow False: ', test_matriz6.__dict__)
    
    test_matriz7 = matriz1.swap_cols(2, 3)
    test_matriz8 = matriz2.swap_cols(2, 3)
    print('Swap cols con byrow True: ', test_matriz7.__dict__)
    print('Swap cols con byrow False: ', test_matriz8.__dict__)
    
    test_matriz9 = matriz1.scale_row(2, 3)
    test_matriz10 = matriz2.scale_row(2, 3)
    print('Scale row con byrow True: ', test_matriz9.__dict__)
    print('Scale row con byrow False: ', test_matriz10.__dict__)
    
    test_matriz11 = matriz1.scale_col(2, 3)
    test_matriz12 = matriz2.scale_col(2, 3)
    print('Scale col con byrow True: ', test_matriz11.__dict__)
    print('Scale row con byrow False: ', test_matriz12.__dict__)
    
    matriz1.transpose()
    matriz2.transpose()
    
    print('Flip rows con byrow True: ', matriz1.flip_rows())
    print('Flip rows con byrow False: ', matriz2.flip_rows())
    
    print('Flip cols con byrow True: ', matriz1.flip_cols())
    print('Flip cols con byrow False: ', matriz2.flip_cols())
    
    matriz3 = Myarray1(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], True)
    matriz4 = Myarray1(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], False)
    print('El determinante con byrow True da: ', matriz3.det())
    print('El determinante con byrow False da: ', matriz4.det())
    
    matrizdeprueba1 = Myarray1(3, 3, [1,2,3,4,5,6,7,8,9], True)
    matrizdeprueba2 = Myarray1(3, 3, [1,2,3,4,5,6,7,8,9], True)

    sumapruebamatriz = matrizdeprueba1 + matrizdeprueba2
    sumapruebanumero = matrizdeprueba1 + 10
    rsumapruebanumero = 10 + matrizdeprueba1
    print('Suma entre dos matrices', sumapruebamatriz) 
    print('Suma entre una matriz y un numero: ', sumapruebanumero) 
    print('Suma reversa entre una matriz y un numero: ', rsumapruebanumero)    

    restapruebamatriz = matrizdeprueba1 - matrizdeprueba2
    restapruebanumero = matrizdeprueba1 - 10
    rrestapruebanumero = 10 - matrizdeprueba1
    print('Resta entre dos matrices', restapruebamatriz) 
    print('Resta entre una matriz y un numero: ', restapruebanumero) 
    print('Resta reversa entre una matriz y un numero: ', rrestapruebanumero) 

    multpruebamatriz = matrizdeprueba1 * matrizdeprueba2
    multpruebanumero = matrizdeprueba1 * 10
    rmultpruebanumero = 10 * matrizdeprueba1
    print('Multiplicacion elemento por elemento entre dos matrices', multpruebamatriz) 
    print('Multiplicacion entre una matriz y un escalar: ', multpruebanumero) 
    print('Multiplicacion reversa entre una matriz y un escalar: ', rmultpruebanumero) 
    
    matmulprueba = matrizdeprueba1 @ matrizdeprueba2
    print('Multiplicacion de matrices: ', matmulprueba)

    powprueba = matrizdeprueba1 ** 3
    print('Potencia de matrices', powprueba)

    pruebarowsidentidad = matrizdeprueba1.swap_rows_eye(1, 3)
    pruebacolsidentidad = matrizdeprueba1.swap_cols_eye(1, 3)
    print('Swap rows multiplicando por una identidad modificada: ', pruebarowsidentidad)
    print('Swap cols multiplicando por una identidad modificada: ', pruebacolsidentidad)

    deleterowidentidad = matrizdeprueba1.del_row_eye(1)
    deletecolidentidad = matrizdeprueba1.del_col_eye(1)
    print('del row multiplicnado por una identidad modificada: ', deleterowidentidad)
    print('del col multiplicando por una identidad modificada: ', deletecolidentidad)
    
    inversadeprueba = Myarray1(3, 3, [10,2,3,8,5,4,7,8,9], True)
    print('Inversa de una matriz: ', inversadeprueba.inverse())
    