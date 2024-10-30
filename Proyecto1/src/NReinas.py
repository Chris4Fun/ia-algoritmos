# Funciones comunes para resolver el problema de las N reinas

# Calcula el número de conflictos entre las reinas en el tablero
def conflictos(tablero):
    conflictos = 0
    n = len(tablero)
    for i in range(n):
        for j in range(i+1, n):
            # Si estan en la misma fila o en la misma diagonal
            if (tablero[i] == tablero[j]) or (abs(tablero[i]-tablero[j]) == abs(i-j)):
                conflictos += 1
    return conflictos

# Retorna una lista con los posibles movimientos (tableros que resultan de 
# intercambiar dos reinas)
def movimientos(tablero):
    movimientos = []
    n = len(tablero)
    for i in range(n):
        for j in range(i+1, n):
            vecino = tablero[:]
            vecino[i], vecino[j] = vecino[j], vecino[i]
            movimientos.append(vecino)
    return movimientos

# Imprimir el tablero 
def imprimir_tablero(tablero):
    print(f"Numero de conflictos: {conflictos(tablero)}")
    n = len(tablero)
    for i in range(n):
        fila = ['-'] * n
        fila[tablero[i]] = 'R'
        print(' '.join(fila))
