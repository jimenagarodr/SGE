from PIL import Image

class Tablero:  
    
    def __init__(self, lista_fichas):
        self.lista = lista_fichas
    
    def pintar_tablero(self):
        tablero_img= Image.open('images/tablero.png').convert("RGBA")
        for ficha in self.lista:
            if ficha.visible: 
                aux_img= Image.open(ficha.image_location).convert("RGBA")
                tablero_img.alpha_composite(aux_img, (ficha.X,ficha.Y))
            tablero_img.save("prueba2.png")
#             tablero_img.show()
        
    def cambiar_posicion_ficha(self, inicio, dest):
        for i in self.lista:
            if i.posi == inicio[1:]:
                i.posi= dest[1:]
                i.set_coord(i.posi)
        self.pintar_tablero()
    
    def comer_ficha(self, inicio, dest):
        for i in self.lista:
            if i.posi == dest[1:]:
                i.visible= False
            if i.posi == inicio[1:]:
                i.posi= dest[1:]
                i.set_coord(i.posi)
        self.pintar_tablero()