sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [0, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [0, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
]#Este es el tablero(No tengo idea de como acer para que coloque nuemros random en el tablero :V

def imprimir_tablero(tablero):
    for fila in tablero:
        print(" ".join(str(num) if num != 0 else "." for num in fila)) #Itercambia los numeros 0 por str con un espacio en medio y un punto(Es solo decoracion me gusta asi).

def movimiento_valido(tablero, fila, columna, numero):    # Verifica si el número ya está en la fila
    if numero in tablero[fila]:
        return False
    
    if numero in [tablero[i][columna] for i in range(9)]:# Verifica si el número ya está en la columna
        return False
    
    inicio_fila, inicio_columna = 3 * (fila // 3), 3 * (columna // 3)
    for i in range(inicio_fila, inicio_fila + 3):
        for j in range(inicio_columna, inicio_columna + 3):# Verifica si el número ya está en la subcuadrícula de 3x3
            if tablero[i][j] == numero:
                return False
                
    return True

def hacer_movimiento(tablero, fila, columna, numero):
    if movimiento_valido(tablero, fila, columna, numero):#Aqui estan creadas la variavles que definen las cordendas para que el jugador pueda moverse por el tablero de Sudoku
        tablero[fila][columna] = numero
        return True
    return False

def juego_sudoku():
    print("¡Bienvenido al juego de Sudoku!")#Solo es decorativo
    imprimir_tablero(sudoku)
    
    while True:#AQUI YA ES PARA JUGAR
        try:
            fila = int(input("Ingrese la fila (0-8): "))#Aqui defines la fila
            columna = int(input("Ingrese la columna (0-8): "))#Aqui defines la columna
            numero = int(input("Ingrese el número (1-9): "))#Aqui defines el numero
            
            if fila not in range(9) or columna not in range(9) or numero not in range(1, 10):#esto quei es solo una comprovacion para para que no puedas salirte de lo predefinido
                print("Entrada fuera de rango. Intente de nuevo.")
                continue
            
            if hacer_movimiento(sudoku, fila, columna, numero):
                print("¡Movimiento válido!")
            else:
                print("Movimiento inválido. Intente de nuevo.")
            
            imprimir_tablero(sudoku)
        except ValueError:
            print("Entrada inválida. Asegúrese de ingresar números. Intente de nuevo.")

juego_sudoku()

     




