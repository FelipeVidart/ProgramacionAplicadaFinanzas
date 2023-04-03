# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 21:38:38 2023

@author: vidar
"""

class Myarray1:
    """MyArray1 es un objeto que permite operar con matrices. Desde crear matrices
    hasta modificarlas, multiplicarlas o ver columnas/filas específicas"""
    
    def __init__(self, rows, columns, elements, by_row = bool):
        #error checking
        if len(elements) != (rows * columns):
            return print('ERROR: La cantidad de elementos introducidos no coincide con la cantidad de elementos de la matriz')
        #almacenamiento de variables
        self.elems = list(elements)
        self.r = rows
        self.c = columns
        self.by_row = by_row
     
    def get_pos(self, j, k):
        """La funcion get_pos busca dentro de la lista que representa la matriz la posicion de la coordenada
        (j, k) en la matriz. Tiene como parametros j (numero de filas) y k (numero de columnas). Devuelve 
        la posicion de esa coordenada en la lista que representa la matriz"""
        #error checking
        if j > self.r:
            return print(f'La fila introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
        if k > self.c:
            return print(f'La columna introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
        #parte funcional
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
        #Error checking
        if m > len(self.elems) or m <= 0:
            return print('ERROR: El numero introducido no se encuentra dentro de la lista')
        #Parte funcional
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
        """La funcion switch cambia el modo de atravesar la matriz. Predeterminadamente la matriz
        se atraviesa por filas, pero cada vez que switch sea usada se cambiara a columna o fila,
        según corresponda, y se devolverá un objeto con las filas cambiadas y el booleano by_row
        cambiado"""
        #parte funcional
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
        por fila. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
        cuando convenga indexarla por filas. Devuelve la matriz leida por filas"""
        if self.by_row == True:
            matrix = self.elems
        elif self.by_row == False:
            matrix = self.switch().elems
        return matrix
        
    def to_by_column(self):
        """to_by_column sirve para que, sea cual sea la matriz que se introduzca, esta pueda ser leida
        por cp;i,ma. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
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
            #pongo not self.by_row para que quede en el que ya estaba, porque switch lo cambia.
            aux_object = Myarray1(self.r, self.c, new_matrix, not self.by_row)
            new_object = aux_object.switch()
        return new_object

    def get_row(self, j):
        """La funcion get_row recibe un numero, j, y devuelve la fila que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las filas introducidas"""
        #Error checking
        if type(j) == list:
            for i in j:
                if i > self.r:
                    return print('ERROR: Una de las filas introducidas no se encuentra en la matriz')
        if type(j) == int:
            if j > self.r:
                return print('ERROR: La fila introducida no se encuentra en la matriz')
        
        #convierto a por fila
        matrix = self.to_by_row()
        
        #Parte funcional
        if type(j) == int:
            end = list(matrix[(self.c*(j-1)): ((self.c*(j-1)) + self.c)])
        elif type (j) == list:
            submatrix = []
            for i in j:
                submatrix.extend(matrix[(self.c * (i-1)): (self.c * (i-1) + self.c)])
            end = submatrix
        else:
            print('j debe ser un entero o una lista')
        return end
    
    def get_col(self, k):
        """La funcion get_col recibe un numero, k, y devuelve la columna que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las columnas introducidas"""
        #Error checking
        if type(k) == list:
            for i in k:
                if i > self.c:
                    return print('ERROR: Una de las columnas introducidas no se encuentra en la matriz')
        if type(k) == int:
            if k > self.c:
                return print('ERROR: La columna introducida no se encuentra en la matriz')
        
        #convierto a por columna
        matrix = self.to_by_column()

        #Parte funcional
        if type(k) == int:
            end = list(matrix[(self.r*(k-1)): ((self.r*(k-1)) + self.r)])
        elif type (k) == list:
            submatrix = []
            for i in k:
                submatrix.extend(matrix[(self.r * (i-1)): (self.r * (i-1) + self.r)])
            end = submatrix
        else:
            print('j debe ser un entero o una lista')
        return end
    
    def get_elem(self, j: int, k: int):
        """La funcion get_elem recibe dos numeros, j y k, y devuelve el elemento que se encuentra en
        la fila y columna que esos numeros representan respectivamente"""
        #Error checking
        if j > self.r:
            return print(f'La fila introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
        if k > self.c:
            return print(f'La columna introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
       
        #parte funcional
        m = self.elems[(self.get_pos(j, k))-1] 
        return m

    def del_row(self, j: int):
        """La funcion del_row recibe un numero, j, que representa una fila de la matriz. La funcion elimina
        esa fila de la matriz y devuelve un objeto cuya matriz no tiene esa fila. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro"""
        #Error checking
        if j > self.r:
            return print(f"ERROR: La fila que quiere eliminar no está en la matriz, la fila solo tiene {self.r} filas")
        
        #convierto a por fila
        matrix = self.to_by_row()
        
        #Parte funcional
        new_matrix = matrix[0: (self.c * (j-1))] + matrix[(self.c * (j-1)) + self.c:]
        #le saco 1 a self.c momentaneamente para que el nuevo objeto se cree correctamente
        self.r -= 1
        new_object = self.return_byrow(new_matrix)
        self.r += 1
        return new_object
    
    def del_col(self, k:int, matrix_input = None):
        """La funcion del_col recibe un numero, k, que representa una columna de la matriz. La funcion elimina
        esa columna de la matriz y devuelve un objeto cuya matriz no tiene esa columna. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro"""
        #Error checking
        if k > self.c:
            return print(f"ERROR: La columna que quiere eliminar no está en la matriz, la fila solo tiene {self.c} filas")
       
        #convierto a por columna
        matrix = self.to_by_column()
        
        #Parte funcional
        new_matrix = matrix[0: (self.r * (k-1))] + matrix[(self.r * (k-1)) + self.r:]
        self.c -= 1
        new_object = self.return_bycolumn(new_matrix)
        self.c += 1
        return new_object
    
    def swap_rows(self, j:int, k:int):
        """La funcion swap_rows recibe como parametros dos numeros, j y k. Estos numeros representan dos 
        filas en la matriz. Su funcion es devolver un objeto con la misma matriz pero con las filas j y k intercambiadas
        La funcion puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro.
        Para que funcione correctamente, se debe introducir una j < k """
        
        #Error checking
        if j > self.r or k > self.r:
            return print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
        
        #convierto a por fila
        matrix = self.to_by_row()
        
        #Parte funcional
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
    
    def swap_cols(self, l:int, m:int):
        """La funcion swap_cols recibe como parametros dos numeros, l y m. Estos numeros representan dos columnas en 
        la matriz. Su funcion es devolver un objeto conla misma matriz pero con las columnas l y m intercambiadas"""
        #Error checking
        if l > self.c or m > self.c:
            return print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
        elif l > m:
            return print("Por favor, introduzca las filas en orden")
        
        #convierto a por columna
        matrix = self.to_by_column()
        
        #Parte funcional
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
    
    def scale_row(self, j: int, x: int, matrix_input = None):
        """ La funcion scale_row toma por argumentos dos numeros, j y x, j representando una fila de la
        matriz y x un factor. Devuelve la misma matriz pero con la fila j multiplicada por x. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. X debe
        ser un entero y j debe estar dentro de la matriz """
        
        #Error checking
        if type(x) != int:
            return print(f"ERROR: X debe ser un entero y se ha introducido: {type(x)}")
        if j > self.r:
            return print(f"ERROR: La fila introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
        
        #convierto a por fila
        matrix = self.to_by_row()
        
        #Parte funcional
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
        #Error checking
        if type(y) != int:
            return print(f"ERROR: K debe ser un entero y se ha introducido: {type(k)}")
        if k > self.c:
            return print(f"ERROR: La columna introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
        
        #convierto a por fila
        matrix = self.to_by_column()
        
        #Parte funcional
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
        
        #Parte funcional
        new_instance = Myarray1(self.r, self.c, self.elems.copy(), self.by_row)
        #este for es para iterar en los elementos que tengan que ser cambiados, si la matriz es impar el elemento del medio no se cambia
        for i in range(1, (new_instance.r//2) + 1):
            if 0 < i < new_instance.r:
                new_instance.elems = new_instance.swap_rows(i,new_instance.r-i+1).elems
        return new_instance.elems
    
    def flip_cols(self):
        """La funcion flip cols da vuelta especularmente las columnas de una funcion y devuelve
        una copia de la misma con las columnas dadas vuelta"""
        
        #Parte funcional
        new_instance = Myarray1(self.r, self.c, self.elems.copy(), self.by_row)
        #este for es para iterar en los elementos que tengan que ser cambiados, si la matriz es impar el elemento del medio no se cambia
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
        #Error checking
        if self.r != self.c:
            return print('ERROR: No se puede calcular el determinante de una matriz que no es cuadrada')
        
        if matrix_input == None:
            matrix, columns, rows = Myarray1(self.r, self.c, self.elems, self.by_row), self.r, self.c
        
        #convierto a por fila
        if matrix_input != None:
            instance = Myarray1(rows, columns, matrix_input, self.by_row)
            #cambiar a byrow
            matrix = instance.switch()
        
        #Parte funcional
        if rows == 2 and columns == 2:
            #caso base
            matrix_end = matrix.elems
            det = matrix_end[0]*matrix_end[3] - matrix_end[1]*matrix_end[2]
        else:
            first_row = matrix.get_row(1)
            #agarro la primer row
            det = 0
            col_counter = 0
            #para cada columna...
            for i in range(1,columns+1):
                element = first_row[i-1]
                #agarro el primer elemento de la primera fila para multiplicar por el determinante
                new_matrix = []
                for i in range(2, rows+1):
                    #para todas las filas menos la primera busco la fila
                    row = matrix.get_row(i)
                    if len(row) > 1:
                        #si la row mide mas de 1 le saco el elemento que no entra en el determinante de 2x2
                        row.pop(col_counter)
                        new_matrix.extend(row)
                        #agrego la lista a a new matrix, me queda la matriz de 2x2
                    elif len(row) <= 1:
                        break
                col_counter += 1
                #parte recursiva
                det += element * ((-1)**(1+col_counter)) * self.det(new_matrix, rows-1, columns-1)
        return det
    
#%%

class Myarray2:
    """MyArray1 es un objeto que permite operar con matrices. Desde crear matrices
    hasta modificarlas, multiplicarlas o ver columnas/filas específicas"""
    def __init__(self, rows, columns, elements, by_row = True):
        #error checking
        if len(elements) != (rows * columns):
            return print('ERROR: La cantidad de elementos introducidos no coincide con la cantidad de elementos de la matriz')
        #almacenamiento de variables
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
        #error checking
        if j > self.r:
            return print(f'La fila introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
        if k > self.c:
            return print(f'La columna introducida no está en la matriz, la matriz es de {self.r}x{self.c}')
        
        #parte funcional
        if self.by_row == True:
            indice = (self.c * (j-1)) + k
        elif self.by_row == False:
            indice = (self.r * (k-1)) + j
        return indice

    def get_coords(self, m):
        """
        La funcion get_coords busca y devuelve las coordenadas de un indice de la lista que 
        se introduce en los parametros. Al introducirse el numero debe introducirse teniendo
        en cuenta que el programa cuenta el primer elemento de la lista como 1 y no como 0, es 
        decir que si se quiere obtener el indice de la lista 4 en el sentido que lo lee python debe
        introducirse el numero 5. 
        """
        #Error checking
        if m > self.r*self.c:
            return print('ERROR: El numero introducido es mayor a la longitud de la lista')
        #Parte funcional
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
        """
        La funcion switch cambia el modo de atravesar la matriz. Predeterminadamente la matriz
        se atraviesa por filas, pero cada vez que switch sea usada se cambiara a columna o fila,
        según corresponda, y se devolverá un objeto con las filas cambiadas y el booleano by_row
        cambiado. 
        """
        plain_list = []
        if self.by_row == True:
            counter = 0
            for i in range(0, self.c):
                for i in self.elems:
                    plain_list.append(i[counter])
                counter += 1
        elif self.by_row == False:
            counter = 0
            for i in range(0, self.r):
                for i in self.elems:
                    plain_list.append(i[counter])
                counter += 1
        return Myarray2(self.r, self.c, plain_list, not self.by_row)
        
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
        por cp;i,ma. Necesita ser llamada desde otro metodo y sirve para facilitar el indexado de la matriz
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
            #pongo not self.by_row para que quede en el que ya estaba, porque switch lo cambia.
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
            #pongo not self.by_row para que quede en el que ya estaba, porque switch lo cambia.
            aux_object = Myarray2(self.r, self.c, new_matrix, not self.by_row)
            new_object = aux_object.switch()
        return new_object
    
    def get_row(self, j):
        """
        La funcion get_row recibe un numero, j, y devuelve la fila que ese numero representa
        en la matriz. Tambien puede recibir una lista, caso en el que va a devolver la submatriz
        formada por las filas introducidas. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro.
        """
        if type(j) == list:
            for i in j:
                if i > self.r:
                    return print('ERROR: Una de las filas introducidas no se encuentra en la matriz')
        if type(j) == int:
            if j > self.r:
                return print('ERROR: La fila introducida no se encuentra en la matriz')
        elems = self.to_by_row()
        if type(j) == int:
            j -= 1
            end = elems[j]
        elif type (j) == list:
            submatrix = []
            for i in j:
                submatrix.append(elems[i-1])
            end = submatrix
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
        if type(k) == list:
            for i in k:
                if i > self.c:
                    return print('ERROR: Una de las columnas introducidas no se encuentra en la matriz')
        if type(k) == int:
            if k > self.c:
                return print('ERROR: La columna introducida no se encuentra en la matriz')
        elems = self.to_by_column()
        if type(k) == int:
            k -= 1
            end = elems[k]
        elif type (k) == list:
            submatrix = []
            for i in k:
                submatrix.append(elems[i-1])
            end = submatrix
        else:
            print('k debe ser un entero o una lista')
        return end

    def get_elem(self, j, k):
        """ La funcion get_elem recibe dos numeros, j y k, y devuelve el elemento que se encuentra en
        la fila y columna que esos numeros representan respectivamente. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro """
        #Error checking
        if self.by_row == True:
            m = self.elems[j-1][k-1]
        elif self.by_row == False:
            m = self.elems[k-1][j-1]
        return m
        
    def del_row(self, j, matrix_input = None):
        """
        La funcion del_row recibe un numero, j, que representa una fila de la matriz. La funcion elimina
        esa fila de la matriz y devuelve una nueva matriz sin esa fila. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro.
        """
        #Error checking
        if j > self.r:
            return print(f"ERROR: La fila que quiere eliminar no está en la matriz, la fila solo tiene {self.r} filas")
        elems = self.to_by_row()
        elements = elems 
        elements.pop(j-1)
        self.r -= 1
        plain_list = []
        for lists in elements:
            for element in lists:
                plain_list.append(element)
        end = self.return_byrow(plain_list)
        self.r += 1
        return end
    
    #voy por aca, no anda 
    
    def del_col(self, k, matrix_input = None):
        """
        La funcion del_col recibe un numero, k, que representa una columna de la matriz. La funcion elimina
        esa columna de la matriz y devuelve una nueva matriz sin esa columna. La funcion puede usarse
        para matrices externas a la instancia introduciendolas en el tercer parametro.
        """
        #Error checking
        if k > self.c:
            return print(f"ERROR: La columna que quiere eliminar no está en la matriz, la fila solo tiene {self.c} filas")
        elems = self.to_by_column()
        elements = elems 
        elements.pop(k-1)
        self.c -= 1
        plain_list = []
        for lists in elements:
            for element in lists:
                plain_list.append(element)
        end = self.return_bycolumn(plain_list)
        self.c += 1
        return end
    
    def swap_rows(self, j, k, matrix_input = None):
        """
        La funcion swap_rows recibe como parametros dos numeros, j y k. Estos numeros representan dos 
        filas en la matriz. Su funcion es devolver la misma matriz pero con las filas j y k intercambiadas
        La funcion puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro.
        Para que funcione correctamente, se debe introducir una j < k. 
        """
        #Error checking
        if j > self.r or k > self.r:
            return print(f"ERROR: Una de las filas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
        elif j > k:
            return print("Por favor, introduzca las filas en orden")
        elems = self.to_by_row()
        copy = elems.copy()
        rowj, rowk = elems[j-1], elems[k-1]
        copy[j-1], copy[k-1] = rowk, rowj
        plain_list = []
        for lists in copy:
            plain_list.extend(lists)
        end = self.return_byrow(plain_list)
        return end
    
    def swap_cols(self, l, m, matrix_input = None):
        """
        La funcion swap_rows recibe como parametros dos numeros, j y k. Estos numeros representan dos 
        filas en la matriz. Su funcion es devolver la misma matriz pero con las filas j y k intercambiadas
        La funcion puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro.
        Para que funcione correctamente, se debe introducir una j < k. 
        """
        #Error checking
        if l > self.c or m > self.c:
            return print(f"ERROR: Una de las columnas introducidas no se está en la matriz, la matriz tiene {self.r} filas")
        elif l > m:
            return print("Por favor, introduzca las filas en orden")
        elems = self.to_by_column()
        copy = elems.copy()
        coll, colm = elems[l-1], elems[m-1]
        copy[l-1], copy[m-1] = colm, coll
        plain_list = []
        for lists in copy:
            plain_list.extend(lists)
        end = self.return_bycolumn(plain_list)
        return end
    
    def scale_row(self, j: int, x: int, matrix_input = None):
        """ La funcion scale_row toma por argumentos dos numeros, j y x, j representando una fila de la
        matriz y x un factor. Devuelve la misma matriz pero con la fila j multiplicada por x. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. X debe
        ser un entero y j debe estar dentro de la matriz """
        
        #Error checking
        if type(x) != int:
            return print(f"ERROR: X debe ser un entero y se ha introducido: {type(x)}")
        if j > self.r:
            return print(f"ERROR: La fila introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
        elems = self.to_by_row()
        copy = elems.copy()
        copy[j] = list(x*i for i in elems[j])
        plain_list = []
        for lists in copy:
            plain_list.extend(lists)
        end = self.return_byrow(plain_list)
        return end
    
    def scale_col(self, k: int, y: int, matrix_input = None):
        """La funcion scale_col toma como argumento dos enteros. k representa una columna e y un numero entero. La funcion
        multiplica esa columna especifica por y y devuelve la matriz completa con esa fila multiplicada por y. La funcion 
        puede usarse para matrices externas a la instancia introduciendolas en el tercer parametro. Y debe ser un entero 
        y k debe estar dentro de la matriz """
        #Error checking
        if type(y) != int:
            return print(f"ERROR: K debe ser un entero y se ha introducido: {type(k)}")
        if k > self.c:
            return print(f"ERROR: La columna introducida no se encuentra en la matriz, la matriz es de {self.r}x{self.c}")
        elems = self.to_by_column()
        copy = elems.copy()
        copy[k] = list(y*i for i in elems[k])
        plain_list = []
        for lists in copy:
            plain_list.extend(lists)
        end = self.return_bycolumn(plain_list)
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
        #hacer esto con zip, se lo paso con el asterisco
        #zip()
        elements = self.to_by_row()
        copy = elements.copy()
        for i in range(0, (self.r//2)):
            if 0 <= i < self.r:
                copy[i], copy[self.r-i-1] = elements[self.r-i-1], elements[i]
        plain_list = []
        for lists in copy:
            plain_list.extend(lists)
        end = self.return_byrow(plain_list)
        return end.elems
    
    def flip_cols(self):
        """La funcion flip cols da vuelta especularmente las columnas de una funcion y devuelve
        una copia de la misma con las columnas dadas vuelta"""
        elements = self.to_by_column()
        copy = elements.copy()
        for i in range(0, (self.c//2)):
            if 0 <= i < self.c:
                copy[i], copy[self.c-i-1] = elements[self.c-i-1], elements[i]
        plain_list = []
        for lists in copy:
            plain_list.extend(lists)
        end = self.return_bycolumn(plain_list)
        return end.elems

#%%

#bloque de testeo Myarray1

if __name__ == "__main__":
    matriz1 = Myarray1(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12], True)
    matriz2 = Myarray1(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], False)
    
    #print(matriz1.get_pos(2, 3))
    #print(matriz2.get_pos(4, 3))
    
    #print(matriz1.get_coords(3))
    #print(matriz2.get_coords(10))
    
    #test_matriz1 = matriz1.switch()
    #test_matriz2 = matriz2.switch()
    #print(test_matriz1.__dict__)
    #print(test_matriz2.__dict__)
    
    #print(matriz1.get_row(3))
    #print(matriz2.get_row(3))
    #print(matriz1.get_row([3, 4]))
    #print(matriz2.get_row([3, 4]))
    
    #print(matriz1.get_col(3))
    #print(matriz2.get_col(3))
    #print(matriz1.get_col([2, 3]))
    #print(matriz2.get_col([2, 3]))
    
    #print(matriz1.get_elem(3, 1))
    #print(matriz2.get_elem(3, 1))
    
    #test_matriz3 = matriz1.del_row(2)
    #test_matriz4 = matriz2.del_row(2)
    #print(test_matriz3.__dict__)
    #print(test_matriz4.__dict__)
    
    #test_matriz3 = matriz1.del_col(2)
    #test_matriz4 = matriz2.del_col(2)
    #print(test_matriz3.__dict__)
    #print(test_matriz4.__dict__)

    #test_matriz5 = matriz1.swap_rows(2, 3)
    #test_matriz6 = matriz2.swap_rows(2, 3)
    #print(test_matriz5.__dict__)
    #print(test_matriz6.__dict__)
    
    #test_matriz7 = matriz1.swap_cols(2, 3)
    #test_matriz8 = matriz2.swap_cols(2, 3)
    #print(test_matriz7.__dict__)
    #print(test_matriz8.__dict__)
    
    #test_matriz9 = matriz1.scale_row(2, 3)
    #test_matriz10 = matriz2.scale_row(2, 3)
    #print(test_matriz9.__dict__)
    #print(test_matriz10.__dict__)
    
    #test_matriz11 = matriz1.scale_col(2, 3)
    #test_matriz12 = matriz2.scale_col(2, 3)
    #print(test_matriz11.__dict__)
    #print(test_matriz12.__dict__)
    
    #matriz1.transpose()
    #matriz2.transpose()
    
    #print(matriz1.flip_rows())
    #print(matriz2.flip_rows())
    
    #print(matriz1.flip_cols())
    #print(matriz2.flip_cols())
    
    #matriz3 = Myarray1(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], True)
    #matriz4 = Myarray1(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], False)
    #print(matriz3.det())
    #print(matriz4.det())

#%%

#bloque de testeo Myarray2

if __name__ == "__main__":
    matriz1 = Myarray2(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ,12], True)
    matriz2 = Myarray2(4,3,[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], False)
    #print(matriz1.det())
    
    #print(matriz1.get_pos(2, 3))
    #print(matriz2.get_pos(4, 3))
    
    #print(matriz1.get_coords(3))
    #print(matriz2.get_coords(10))
    
    #test_matriz1 = matriz1.switch()
    #test_matriz2 = matriz2.switch()
    #print(test_matriz1.__dict__)
    #print(test_matriz2.__dict__)
    
    #print(matriz1.get_row(3))
    #print(matriz2.get_row(3))
    #print(matriz1.get_row([3, 4]))
    #print(matriz2.get_row([3, 4]))
    
    #print(matriz1.get_col(3))
    #print(matriz2.get_col(3))
    #print(matriz1.get_col([2, 3]))
    #print(matriz2.get_col([2, 3]))
    
    #print(matriz1.get_elem(3, 1))
    #print(matriz2.get_elem(3, 1))
    
    #test_matriz3 = matriz1.del_row(2)
    #test_matriz4 = matriz2.del_row(2)
    #print(test_matriz3.__dict__)
    #print(test_matriz4.__dict__)
    
    #test_matriz3 = matriz1.del_col(2)
    #test_matriz4 = matriz2.del_col(2)
    #print(test_matriz3.__dict__)
    #print(test_matriz4.__dict__)

    #test_matriz5 = matriz1.swap_rows(2, 3)
    #test_matriz6 = matriz2.swap_rows(2, 3)
    #print(test_matriz5.__dict__)
    #print(test_matriz6.__dict__)
    
    #test_matriz7 = matriz1.swap_cols(2, 3)
    #test_matriz8 = matriz2.swap_cols(2, 3)
    #print(test_matriz7.__dict__)
    #print(test_matriz8.__dict__)
    
    #test_matriz9 = matriz1.scale_row(2, 3)
    #test_matriz10 = matriz2.scale_row(2, 3)
    #print(test_matriz9.__dict__)
    #print(test_matriz10.__dict__)
    
    #test_matriz11 = matriz1.scale_col(2, 3)
    #test_matriz12 = matriz2.scale_col(2, 3)
    #print(test_matriz11.__dict__)
    #print(test_matriz12.__dict__)
    
    #matriz1.transpose()
    #matriz2.transpose()
    
    #print(matriz1.flip_rows())
    #print(matriz2.flip_rows())
    
    #print(matriz1.flip_cols())
    #print(matriz2.flip_cols())
    
    #matriz3 = Myarray2(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], True)
    #matriz4 = Myarray2(3,3,[1, 2, 3, 4, 5, 6, 7, 8, 9], False)
    
    #print(matriz3.det())
    #print(matriz4.det())

    #print(matriz3.shift(2, 'right'))
    #print(matriz3.shift(2, 'left'))
    #print(matriz3.shift(2, 'up'))
    #print(matriz3.shift(2, 'down'))
    
    #print(matriz4.shift(2, 'right'))
    #print(matriz4.shift(2, 'left'))
    #print(matriz4.shift(2, 'up'))
    #print(matriz4.shift(2, 'down'))
    
