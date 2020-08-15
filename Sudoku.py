# A Utility Function to print the Grid 
def print_grid(arr): 
    for i in range(9): 
        for j in range(9): 
            print (arr[i][j], end =" ")
        print (' ') 
  
def remplazar_ubicacion_vacia(arr, l): 
    for fila in range(9): 
        for columna in range(9): 
            if(arr[fila][columna]==0): 
                l[0]= fila 
                l[1]= columna 
                return True
    return False

def utilizado_fila(arr, fila, num): 
    for i in range(9): 
        if(arr[fila][i] == num): 
            return True
    return False
 
def utilizado_columna(arr, columna, num): 
    for i in range(9): 
        if(arr[i][columna] == num): 
            return True
    return False

def utilizado_caja(arr, fila, columna, num): 
    for i in range(3): 
        for j in range(3): 
            if(arr[i + fila][j + columna] == num): 
                return True
    return False

def es_Segura(arr, fila, columna, num): 

    return not utilizado_fila(arr, fila, num) and not utilizado_columna(arr, columna, num) and not utilizado_caja(arr, fila - fila % 3, columna - columna % 3, num) 

def resuelveSudoku(arr): 
 
    l =[0, 0] 
      
    if(not remplazar_ubicacion_vacia(arr, l)): 
        return True

    fila = l[0] 
    columna = l[1] 

    for num in range(1, 10): 
          
        if(es_Segura(arr, fila, columna, num)): 
              
            arr[fila][columna]= num 

            if(resuelveSudoku(arr)):
                return True

            arr[fila][columna] = 0
              
    return False 
  
if __name__=="__main__": 
      
    grid =[[0 for x in range(9)]for y in range(9)] 
      
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0], 
          [5, 2, 0, 0, 0, 0, 0, 0, 0], 
          [0, 8, 7, 0, 0, 0, 0, 3, 1], 
          [0, 0, 3, 0, 1, 0, 0, 8, 0], 
          [9, 0, 0, 8, 6, 3, 0, 0, 5], 
          [0, 5, 0, 0, 9, 0, 6, 0, 0], 
          [1, 3, 0, 0, 0, 0, 2, 5, 0], 
          [0, 0, 0, 0, 0, 0, 0, 7, 4], 
          [0, 0, 5, 2, 0, 6, 3, 0, 0]] 

    if(resuelveSudoku(grid)): 
        print_grid(grid) 
    else:
        print("Sin Solución")