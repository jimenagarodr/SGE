from PIL import Image

def pintar_tablero():
    tablero_img= Image.open('images/tablero.png').convert("RGBA")
    tablero_img.show()
    
pintar_tablero()