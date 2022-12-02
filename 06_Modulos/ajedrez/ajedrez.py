import ajedrez.tablero as tablero
import ajedrez.ficha as ficha


inicio = ['Ta1', 'Cb1', 'Ac1', 'Rd1', 'De1', 'Af1', 'Cg1', 'Th1',
          'Pa2', 'Pb2', 'Pc2', 'Pd2', 'Pe2', 'Pf2', 'Pg2', 'Ph2',
          'pa7', 'pb7', 'pc7', 'pd7', 'pe7', 'pf7', 'pg7', 'ph7',
          'ta8', 'cb8', 'ac8', 'rd8', 'de8' ,'af8', 'cg8', 'th8'      
         ]



lista_fichas = []
for i in inicio:
    lista_fichas.append(ficha.Ficha(i))

tabl = tablero.Tablero(lista_fichas)
    
tabl.pintar_tablero()  

tabl.cambiar_posicion_ficha("Pd2","Pd4")
tabl.cambiar_posicion_ficha("cb8","cc6")
tabl.cambiar_posicion_ficha("Ac1","Ae3")

tabl.comer_ficha("cc6","cd4")