# -*- coding: utf-8 -*-
"""
Created on Mon Apr  3 18:34:54 2023

@author: vidar
"""

class Myarray2:
    """MyArray1 es un objeto que permite operar con matrices. Desde crear matrices
    hasta modificarlas, multiplicarlas o ver columnas/filas específicas"""
    def __init__(self, rows, columns, elements, by_row = True):
        if len(elements) != (rows * columns):
            return print('ERROR: La cantidad de elementos introducidos no coincide con la cantidad de elementos de la matriz')
        self.elems = []
        if by_row == True:
            for i in range(0, len(elements), columns):
                row = elements[i:i + columns]
                self.elems.append(row)
        elif by_row == False:
            for i in range(0, len(elements), rows):
                column = elements[i:i + rows]
                self.elems.append(column)
        self.r = rows
        self.c = columns
        self.by_row = by_row
        
    def get_pos(self, j, k):
        """ La funcion get_pos busca dentro de la lista que representa la matriz la posicion de la coordenada
        (j, k) en la matriz. Tiene como parametros j (numero de filas) y k (numero de columnas). Devuelve la 
        posicion de esa coordenada en la lista que representa la matriz """
        if j > self.r:
            print(f'La fila introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
            indice = None
        if k > self.c:
            print(f'La columna introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
            indice = None
        else:
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
        if m > self.r*self.c:
            print('ERROR: El numero introducido es mayor a la longitud de la lista')
            coord = None
        else:
            m -= 1
            if self.by_row == True:
                row = (m // self.c)
                col = (m - row*self.c)
                coord = (row+1, col+1)
            elif self.by_row == False:
                col = (m // self.r)
                row = (m - col*self.r)
                coord = (row + 1, col + 1)
        return coord
        
    def switch(self):
        """La funcion switch cambia el modo de atravesar la matriz. Predeterminadamente la matriz
        se atraviesa por filas, pero cada vez que switch sea usada se cambiara a columna o fila,
        según corresponda, y se devolverá un objeto con las filas cambiadas y el booleano by_row
        cambiado"""
        zipped = list(zip(*self.elems))
        flat_list = self.flatten(zipped)
        return Myarray2(self.r, self.c, flat_list, not self.by_row)
        
    def to_by_row(self):
        """to_by_row sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por fila. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
        cuando convenga indexarla por filas. Devuelve la matriz leida por filas"""
        if self.by_row == True:
            matrix = self.elems
        elif self.by_row == False:
            matrix = self.switch().elems
        return matrix
        
    def to_by_column(self):
        """to_by_column sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por columma. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
        cuando convenga indexarla por columnas. Devuelve la matriz leida por columnas"""
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
            new_object = Myarray2(self.r, self.c, new_matrix, self.by_row)
        if self.by_row == False:
            aux_object = Myarray2(self.r, self.c, new_matrix, not self.by_row)
            new_object = aux_object.switch()
        return new_object
        
    def return_bycolumn(self, new_matrix):
        """De manera similar a to_by_column, return_bycolumn convierte el return de un metodo que trabaja con la 
        matriz en by_column a by_row si es necesario o lo deja en by_column. Su uso es interno de la instancia, se 
        usa para no repetir el mismo codigo al final de todas las funciones"""
        if self.by_row == False:
            new_object = Myarray2(self.r, self.c, new_matrix, self.by_row)
        if self.by_row == True:
            aux_object = Myarray2(self.r, self.c, new_matrix, not self.by_row)
            new_object = aux_object.switch()
        return new_object
    
    def eye(self, n):
        """eye es una funcion usada para crear matrices idendidad de NxN. El unico parametro es N e indica el 
        numero de columnas y filas de la matriz identidad (ya que debe ser cuadrada)"""
        elems = [[0] * i + [1] + [0] * (n - i - 1) for i in range(n)]
        identity = Myarray2(n,n,self.flatten(elems),True)
        return identity
        
    def flatten(self, lista):
        """Dada la forma en la que esta creada el init, necesito que la lista siempre se introduzca sin estar 
        separada por listas internamente. Creo esta funcion para crear una sola lista a partir de las listas de 
        listas que devuelven diferentes funciones"""
        return [elemento for sublista in lista for elemento in sublista]
    
    def get_row(self, j):
        """La funcion get_row recibe un numero, j, y devuelve la fila que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las filas introducidas. La funcion puede usarse para matrices externas a la 
        instancia introduciendolas en el tercer parametro"""
        elems = self.to_by_row()
        if type(j) == list:
            submatrix = []
            for i in j:
                if i > self.r:
                    print('ERROR: Una de las filas introducidas no se encuentra en la matriz')
                    submatrix = None
                else:
                    submatrix.append(elems[i-1])
            end = submatrix
        if type(j) == int:
            if j > self.r:
                return print('ERROR: La fila introducida no se encuentra en la matriz')
            else:
                j -= 1
                end = elems[j]        
        else:
            print('j debe ser un entero o una lista')
        return end
    
    def get_col(self, k):
        """
        La funcion get_col recibe un numero, k, y devuelve la columna que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las columnas introducidas. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro.
        """
        elems = self.to_by_column()
        if type(k) == list:
            submatrix = []
            for i in k:
                if i > self.c:
                    print('ERROR: Una de las columnas introducidas no se encuentra en la matriz')
                    submatrix = None
                else:
                    submatrix.append(elems[i-1])
            end = submatrix
        if type(k) == int:
            if k > self.c:
                print('ERROR: La columna introducida no se encuentra en la matriz')
                end = None
            else:
                k -= 1
                end = elems[k]
        else:
            print('k debe ser un entero o una lista')
        return end

    def get_elem(self, j, k):
        """ La funcion get_elem recibe dos numeros, j y k, y devuelve el elemento que se encuentra en
        la fila y columna que esos numeros representan respectivamente. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro """
        if self.by_row == True:
            m = self.elems[j-1][k-1]
        elif self.by_row == False:
            m = self.elems[k-1][j-1]
        return m
        
    def del_row(self, j, matrix_input = None):
        """La funcion del_row recibe un numero, j, que representa una fila de la matriz. La funcion elimina
        esa fila de la matriz y devuelve una nueva matriz sin esa fila. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro"""
        if j > self.r:
            print(f"ERROR: La fila que quiere eliminar no está en la matriz, la fila solo tiene {self.r} filas")
            end = None
        else:
            elems = self.to_by_row().copy()
            elements = list(elems)
            elements.pop(j-1)
            self.r -= 1
            flat_list = self.flatten(elements)
            end = self.return_byrow(flat_list)
            self.r += 1
        return end
    
    def del_row_eye(self, j):
        """Al igual que del_row, del_row_eye elimina una fila j de la matriz. Lo que diferencia ambos métodos es que 
        en este caso la elimina premultiplicando la matriz original por una matriz identidad con una fila eliminada"""
        if j > self.r:
            print(f"ERROR: La fila que quiere eliminar no está en la matriz, la fila solo tiene {self.r} filas")
            end = None
        else:   
            matrix = self.to_by_row()
            aux_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
            identity = self.eye(self.r)
            updated_identity = identity.del_row(j)
            deleted = updated_identity @ aux_instance
            #tengo que cambiar las rows antes de crear el return porque sino me tira error el init, despues las devuelvo a como estaban
            originalrows, newrows = self.r, updated_identity.r
            self.r = newrows
            end = self.return_byrow(self.flatten(deleted)).elems
            self.r = originalrows
        return end 
    
    def del_col(self, k, matrix_input = None):
        """
        La funcion del_col recibe un numero, k, que representa una columna de la matriz. La funcion elimina
        esa columna de la matriz y devuelve una nueva matriz sin esa columna. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro.
        """
        if k > self.c:
            print(f"ERROR: La columna que quiere eliminar no está en la matriz, la fila solo tiene {self.c} filas")
            end = None
        else:
            elems = self.to_by_column().copy()
            elements = list(elems) 
            elements.pop(k-1)
            self.c -= 1
            flat_list = self.flatten(elements)
            end = self.return_bycolumn(flat_list)
            self.c += 1
        return end
    
    def del_col_eye(self, m):
        """Al igual que del_col, del_col_eye elimina una columna k de la matriz. Lo que diferencia ambos métodos es que 
        en este caso la elimina premultiplicando la matriz original por una matriz identidad con una columna eliminada"""
        if m > self.c:
            print(f"ERROR: La columna que quiere eliminar no está en la matriz, la fila solo tiene {self.c} columnas")
            end = None
        else:
            matrix = self.to_by_row()
            aux_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
            identity = self.eye(self.c)
            updated_identity = identity.del_col(m)
            deleted = aux_instance @ updated_identity
            originalcolumns, newcolumns = self.c, updated_identity.c
            self.c = newcolumns
            end = self.return_byrow(self.flatten(deleted)).elems
            self.c = originalcolumns
        return end 
    
    def swap_rows(self, j, k, matrix_input = None):
        """
        La funcion swap_rows recibe como parametros dos numeros, j y k. Estos numeros representan dos 
        filas en la matriz. Su funcion es devolver la misma matriz pero con las filas j y k intercambiadas
        La funcion puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro.
        Para que funcione correctamente, se debe introducir una j < k. 
        """
        if j > k:
            inputj, inputk = j, k
            k, j = inputj, inputk
        if j > self.r or k > self.r:
            print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            end = None
        else:
            elems = self.to_by_row()
            copy = elems.copy()
            rowj, rowk = elems[j-1], elems[k-1]
            copy[j-1], copy[k-1] = rowk, rowj
            flat_list = self.flatten(copy)
            end = self.return_byrow(flat_list)
        return end
    
    def swap_rows_eye(self, j, k):
        """Al igual que swap_row, swap_rows_eye intercambia dos filas, j y k, de una matriz. Lo que diferencia ambos métodos 
        es que en este caso las intercambia premultiplicando la matriz original por una matriz identidad con las respectivas
        filas intercambiadas"""  
        if j > k:
            inputj, inputk = j, k
            k, j = inputj, inputk
        if j > self.r or k > self.r:
            print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            end = None
        else:
            matrix = self.to_by_row()
            aux_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
            identity = self.eye(self.r)
            counter = 1
            rowj, rowk = identity.get_row(j), identity.get_row(k)
            for row in identity.elems:
                if counter == j:
                    identity.elems[counter-1] = rowk
                elif counter == k:
                    identity.elems[counter-1] = rowj
                counter += 1
            swapped = identity @ aux_instance
            end = self.return_byrow(self.flatten(swapped)).elems 
        return end
    
    def swap_cols(self, l, m, matrix_input = None):
        """
        La funcion swap_rows recibe como parametros dos numeros, j y k. Estos numeros representan dos 
        filas en la matriz. Su funcion es devolver la misma matriz pero con las filas j y k intercambiadas
        La funcion puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro.
        Para que funcione correctamente, se debe introducir una j < k. 
        """
        if l > m:
            inputl, inputm = l, m
            m, l = inputl, inputm
        if l > self.c or m > self.c:
            print(f"ERROR: Una de las columnas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            end = None
        else:
            elems = self.to_by_column()
            copy = elems.copy()
            coll, colm = elems[l-1], elems[m-1]
            copy[l-1], copy[m-1] = colm, coll
            flat_list = self.flatten(copy)
            end = self.return_bycolumn(flat_list)
        return end
    
    def swap_cols_eye(self, l, m):
        """Al igual que swap_cols, swap_cols_eye intercambia dos columnas, l y m, de una matriz. Lo que diferencia ambos métodos 
        es que en este caso las intercambia premultiplicando la matriz original por una matriz identidad con las respectivas
        filas intercambiadas"""  
        if l > m:
            inputl, inputm = l, m
            m, l = inputl, inputm
        if l > self.c or m > self.c:
            print(f"ERROR: Una de las columnas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
            end = None
        else:
            matrix = self.to_by_row()
            aux_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
            identity = self.eye(self.c)
            counter = 1
            rowl, rowm = identity.get_row(l), identity.get_row(m)
            for i in identity.elems:
                if counter == l:
                    identity.elems[counter-1] = rowm
                elif counter == m:
                    identity.elems[counter-1] = rowl
                counter += 1
            swapped = aux_instance @ identity
            end = self.return_byrow(self.flatten(swapped)).elems
        return end

    def scale_row(self, j: int, x: int, matrix_input = None):
        """ La funcion scale_row toma por argumentos dos numeros, j y x, j representando una fila de la
        matriz y x un factor. Devuelve la misma matriz pero con la fila j multiplicada por x. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. X debe
        ser un entero y j debe estar dentro de la matriz """
        if type(x) != int:
            print(f"ERROR: X debe ser un entero y se ha introducido: {type(x)}")
            end = None
        if j > self.r:
            print(f"ERROR: La fila introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
            end = None
        else:
            elems = self.to_by_row()
            copy = elems.copy()
            copy[j] = list(x*i for i in elems[j])
            flat_list = self.flatten(copy)
            end = self.return_byrow(flat_list)
        return end
    
    def scale_col(self, k: int, y: int, matrix_input = None):
        """La funcion scale_col toma como argumento dos enteros. k representa una columna e y un numero entero. La funcion
        multiplica esa columna especifica por y y devuelve la matriz completa con esa fila multiplicada por y. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. Y debe ser un entero 
        y k debe estar dentro de la matriz """
        if type(y) != int:
            print(f"ERROR: K debe ser un entero y se ha introducido: {type(k)}")
            end = None
        if k > self.c:
            print(f"ERROR: La columna introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
            end = None
        else:
            elems = self.to_by_column()
            copy = elems.copy()
            copy[k] = list(y*i for i in elems[k])
            flat_list = self.flatten(copy)
            end = self.return_bycolumn(flat_list)
        return end
        
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
        elements = self.to_by_row()
        copy = elements.copy()
        for i in range(0, (self.r//2)):
            if 0 <= i < self.r:
                copy[i], copy[self.r-i-1] = elements[self.r-i-1], elements[i]
        flat_list = self.flatten(copy)
        end = self.return_byrow(flat_list)
        return end.elems
    
    def flip_cols(self):
        """La funcion flip cols da vuelta especularmente las columnas de una funcion y devuelve
        una copia de la misma con las columnas dadas vuelta"""
        elements = self.to_by_column()
        copy = elements.copy()
        for i in range(0, (self.c//2)):
            if 0 <= i < self.c:
                copy[i], copy[self.c-i-1] = elements[self.c-i-1], elements[i]
        flat_list = self.flatten(copy)
        end = self.return_bycolumn(flat_list)
        return end.elems
    
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
        if matrix_input == None:
            matrix, rows, columns = Myarray2(self.r, self.c, self.flatten(self.elems), self.by_row), self.r, self.c
        if matrix_input != None:
            matrix = Myarray2(rows, columns, matrix_input, self.by_row)
        if rows == 2 and columns == 2:
            #caso base
            matrix_end = self.flatten(matrix.elems)
            det = matrix_end[0]*matrix_end[3] - matrix_end[1]*matrix_end[2]
        else:
            first_row = matrix.get_row(1)
            det = 0
            col_counter = 0
            for i in range(0,columns):
                element = first_row[i]
                new_matrix = []
                for a in range(2, rows+1):
                    row = matrix.get_row(a).copy()
                    if len(row) > 1:
                        row.pop(col_counter)
                        new_matrix.extend(row)
                    elif len(row) <= 1:
                        break
                col_counter += 1
                det += element * ((-1)**(1+col_counter)) * self.det(new_matrix, rows-1, columns-1)
        return det
    
    def inverse(self):
        """inverse es un método de Myarray1 que busca la inversa de la matriz. Busca la inversa con la siguiente
        fórmula (siendo A la matriz y cof(A)T la matriz de cofactores de A traspuesta):
        Inversa = 1/det(A) * cof(A)T"""
        if self.r == self.c and self.det() != 0:
            matrix = self.to_by_row()
            cofactors_matrix = []
            for i in range(1, len(self.flatten(matrix))+1):
                aux_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
                coords = aux_instance.get_coords(i)
                deletedrow = aux_instance.del_row(coords[0])
                deletedcolandrow = deletedrow.del_col(coords[1])
                determinant = deletedcolandrow.det() * ((-1)**(coords[1]+coords[0]))
                cofactors_matrix.append(determinant)
            main_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
            cofactors_instance = Myarray2(self.r, self.c, cofactors_matrix, True)
            cofactors_instance.transpose()
            matrix_det = main_instance.det()
            inverse = (1/matrix_det)*cofactors_instance
            end = self.return_byrow(inverse).elems
        else:
            print('No se puede calcular la inversa de la matriz ya sea porque no es cuadrada o porque su determinante es igual a 0')
            end = None
        return end
    
    def __add__(self, other):
        """Redefinicion del special method __add__. Suma elemento a elemento una matriz o un entero en caso de ser necesario"""
        if isinstance(other, int) or isinstance(other, float):
            flattened = self.flatten(self.elems)
            end = [elemento + other for elemento in flattened]
        elif isinstance(other, type(self)):
            if len(other.elems) != len(self.elems):
                print('Las matrices deben ser del mismo tamaño')
                end = None
            else:
                matrix1, matrix2 = self.to_by_row(), other.to_by_row()
                paired = zip(matrix1, matrix2)
                clean = map(lambda x: list(zip(*x)),paired)
                summed = list(map(lambda x: [sum(tupla) for tupla in x], clean))
                flattened = self.flatten(summed)
                end = self.return_byrow(flattened).elems
        else:
            print(f'{type(other)} no se puede sumar con una matriz')
            end = None
        return end
    
    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self + other
        
    def __sub__(self, other):
        """Redefinicion del special method __add__. Resta elemento a elemento una matriz o un entero en caso de ser necesario"""
        if isinstance(other, int) or isinstance(other, float):
            flattened = self.flatten(self.elems)
            end = [elemento - other for elemento in flattened]
        elif isinstance(other, type(self)):
            if len(other.elems) != len(self.elems):
                print('Las matrices deben ser del mismo tamaño')
                end = None
            else:
                matrix1, matrix2 = self.to_by_row(), other.to_by_row()
                paired = zip(matrix1, matrix2)
                #la linea clean es para dejar una lista de tuplas
                clean = map(lambda x: list(zip(*x)),paired)
                substracted = list(map(lambda x: [tupla[0] - tupla[1] for tupla in x], clean))
                #devuelvo todo a byrow
                flattened = self.flatten(substracted)
                end = self.return_byrow(flattened).elems
        else:
            print(f'{type(other)} no se puede restar con una matriz')
            end = None
        return end
    
    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return self - other
    
    def __mul__(self, other):
        """Redefinicion del special method __mul__. Multiplica elemento a elemento una matriz o un escalar"""
        if isinstance(other, int) or isinstance(other, float):
            flattened = self.flatten(self.elems)
            end = [elemento * other for elemento in flattened]
        elif isinstance(other, type(self)):
            if len(other.elems) != len(self.elems):
                print('Las matrices deben ser del mismo tamaño')
                end = None
            else:
                matrix1, matrix2 = self.to_by_row(), other.to_by_row()
                paired = zip(matrix1, matrix2)
                #la linea clean es para dejar una lista de tuplas
                clean = map(lambda x: list(zip(*x)),paired)
                multiplied = list(map(lambda x: [tupla[0] * tupla[1] for tupla in x], clean))
                flattened = self.flatten(multiplied)
                aux = self.return_byrow(flattened).elems
                end = self.return_byrow(self.flatten(aux)).elems
        else:
            print(f'{type(other)} no se puede multiplicar con una matriz')
            end = None
        return end
                                            
    def __rmul__(self,other):
        if isinstance(other, int) or isinstance(other, float):
            return self * other

    def __matmul__(self, other):
        """Redefinicion del special method __matmul__. Lleva a cabo la multiplicacion entre matrices"""
        if isinstance(other, type(self)):
            if self.c == other.r:
                matrix1, matrix2 = self.to_by_row(), other.to_by_column()
                #voy a multiplicar la matriz1 y la matriz2 para tenerlas repetidas y poder zipear las filas y columnas segun corresponda
                mult_matrix1 = []
                #el indexado para list of lists es un poco distinto, pero la idea es la misma que en myarray1
                for i in range(0, self.r):
                    mult_row = [matrix1[i]] * other.c
                    mult_matrix1.extend(mult_row)
                mult_matrix2 = matrix2 * self.c
                counter = 0
                zippedmatrices = []
                for i in mult_matrix1:
                    ziprow = list(zip(i, mult_matrix2[counter]))
                    zippedmatrices.append(ziprow)
                    counter += 1
                auxmatrix = []       
                for element in zippedmatrices:
                    #si lo hago con list comprehension me dicec generator object y no suma, no se bien porque, preguntar
                    #intente hacer estas dos lineas en una sola pero no me salio no se porqueeeeeee
                    auxmatrix.append(list(map(lambda x: x[0]*x[1],element)))
                finalmatrix = list((sum(elements) for elements in auxmatrix))
                originalrows, originalcolumns, newrows, newcolumns = self.r, self.c, other.c, self.r
                self.r, self.c = newrows, newcolumns
                end = self.return_byrow(finalmatrix).elems
                self.r, self.c = originalrows, originalcolumns
            else:
                print('El numero de columnas de la primera matriz no coincide con el numero de filas de la segunda')
                end = None
            return end
        
    def __pow__(self, other):
        """Redefinicion del special method __pow__. Solo funciona con enteros, eleva la matriz a un entero"""
        if isinstance(other, int):
            matrix = self.to_by_row()
            flat_matrix = self.flatten(matrix)
            aux_instance = Myarray2(self.r, self.c, flat_matrix, True)
            changing_aux_instance = Myarray2(self.r, self.c, flat_matrix, True)
            for i in range(other-1):
                matrix = changing_aux_instance @ aux_instance
                changing_aux_instance = Myarray2(self.r, self.c, self.flatten(matrix), True)
            end = changing_aux_instance.elems
        return end

#%%

if __name__ == "__main__":
    matriz1 = Myarray2(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12], True)
    matriz2 = Myarray2(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], False)
    
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
    
    print('Get elem con byrow True: ', matriz1.get_elem(3, 1))
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
    
    matriz3 = Myarray2(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], True)
    matriz4 = Myarray2(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], False)
    print('El determinante con byrow True da: ', matriz3.det())
    print('El determinante con byrow False da: ', matriz4.det())
    
    matrizdeprueba1 = Myarray2(3, 3, [1,2,3,4,5,6,7,8,9], True)
    matrizdeprueba2 = Myarray2(3, 3, [1,2,3,4,5,6,7,8,9], True)

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
    
    inversadeprueba = Myarray2(3, 3, [10,2,3,8,5,4,7,8,9], True)
    print('Inversa de una matriz: ', inversadeprueba.inverse())
    
