import ajedrez.ajedrez
#import ajedrez.tablero as tablero
#import ajedrez.ficha as ficha
import sys

if len(sys.argv) > 1 :
    if sys.argv[1] == "-n" and len(sys.argv) > 1:
        n_damas=sys.argv[2]
        ajedrez.ajedrez.damas(n_damas)

else :
    print("el parametro -n debe estar seguido del número de reinas a colocar")
#ajedrez.ajedrez.help()
#ajedrez.ajedrez.damas()
