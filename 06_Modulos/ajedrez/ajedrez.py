import ajedrez.tablero as tablero
import ajedrez.ficha as ficha

def help():
    print("hola")

inicio = ['Ta1', 'Cb1', 'Ac1', 'Rd1', 'De1', 'Af1', 'Cg1', 'Th1',
      'Pa2', 'Pb2', 'Pc2', 'Pd2', 'Pe2', 'Pf2', 'Pg2', 'Ph2',
      'pa7', 'pb7', 'pc7', 'pd7', 'pe7', 'pf7', 'pg7', 'ph7',
      'ta8', 'cb8', 'ac8', 'rd8', 'de8' ,'af8', 'cg8', 'th8'      
     ]

lista_fichas = []

for i in inicio:
    lista_fichas.append(ficha.Ficha(i))

tabl = tablero.Tablero(lista_fichas)



    
def inicio():
    tabl.pintar_tablero().show()
        
def mover(ficha1, ficha2):
    tabl.cambiar_posicion_ficha(ficha1, ficha2).show()

def comer(ficha1, ficha2):
    tabl.comer_ficha(ficha1, ficha2).show()
    
    
    
    
def es_seguro(tablero, fila, columna):
  # Comprueba si es seguro colocar una dama en la fila y columna dadas en el tablero

  # Comprueba las filas hacia arriba
    for i in range(fila):
        if (tablero[i] == columna) or (abs(tablero[i] - columna) == abs(i - fila)):
            return False

    return True

def ocho_damas(tabl_reinas, fila):
  # Encuentra una solución al problema de las 8 damas usando un algoritmo de búsqueda en profundidad
    tabl_reinas.pintar_tablero().show()
  # Si llegamos a la última fila, hemos encontrado una solución
    if fila == 8:
        tabl_reinas.pintar_tablero().show()
        return True

  # Prueba cada columna en la fila actual
    for columna in range(8):
        # Si es seguro colocar una dama en esta posición, intenta colocarla
        if es_seguro(tablero, fila, columna):
            print("es seguro: " + str(fila) + " <- fila  col -> " + str(columna))
          # Si se puede colocar una dama en la siguiente fila, devuelve verdadero
            if ocho_damas(tabl_reinas, fila + 1):
                return True

  # Si no se encontró ninguna solución, devuelve falso
    return False

def damas():
    # Inicializa el tablero como una lista de 8 elementos con valores iniciales de -1
    inicio_reinas=['Da1','Da2', 'Da3','Da4', 'Da5','Da6', 'Da7','Da8']
    lista_reinas = []
    for i in inicio_reinas:
        lista_reinas.append(ficha.Ficha(i))
    tabl_reinas = tablero.Tablero(lista_reinas)

    # Llama a la función para encontrar una solución
    ocho_damas(tabl_reinas, 0)