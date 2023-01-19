import ajedrez.tablero as tablero
import ajedrez.ficha as ficha
from PIL import Image

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






def damas(n_damas):
        # Inicialización del tablero
    if int(n_damas) > 8:
        n_damas = 8

    tablero = [[0 for _ in range(int(n_damas))] for _ in range(int(n_damas))]

    # Llamada a la función para resolver las 8 reinas
    if resolverReinas(tablero, 0):
        tablero_img= Image.open('images/tablero.png').convert("RGBA")
        for y in range (len(tablero)):
            fila_entera = tablero[y]
            for x in range(len(fila_entera)):
                if (fila_entera[x] == 1):
                    aux_img= Image.open('images/db.png').convert("RGBA")
                    tablero_img.alpha_composite(aux_img, (45*x,45*y))
                    tablero_img.save("images/tablero_damas.png")
        Image.open('images/tablero_damas.png').convert("RGBA").show()

    else:
        print("No se ha encontrado ninguna solución.")

def esValida(tablero, fila, columna):
  # fila
    for j in range(columna):
        if tablero[fila][j] == 1:
            return False

  # columna
    for i in range(fila):
        if tablero[i][columna] == 1:
            return False

  # diagonal 1
    i, j = fila, columna
    while i >= 0 and j >= 0:
        if tablero[i][j] == 1:
            return False
        i -= 1
        j -= 1

      # diagonal 2
    i, j = fila, columna
    while i >= 0 and j < len(tablero):
        if tablero[i][j] == 1:
              return False
        i -= 1
        j += 1

    return True


def resolverReinas(tablero, columna):

  if columna >= len(tablero):
    return True


  for fila in range(len(tablero)):

    if esValida(tablero, fila, columna):
        tablero[fila][columna] = 1
        if resolverReinas(tablero, columna + 1):
            return True
        if tablero[fila][columna] == 1:
            tablero[fila][columna] = 0


  return False
