class Ficha:  
    
    def __init__(self, codigo):
        
        self.name = codigo
        self.caracter = codigo[0]
        
        
        self.posi = codigo[1:]
        
        
        self.visible = True
        
        self.set_coord(self.posi)
        self.image_location= ""
        if(self.caracter.isupper()):
            self.image_location= "images/" + self.caracter.lower() + "b.png"
        else:
            self.image_location = "images/" + self.caracter.lower() + "n.png"
    
    
    def set_coord(self, posi):
        horizontal='abcdefgh'
        self.X = horizontal.find(posi[0]) * 45
        self.Y = (int(posi[1]) -1) * 45
    
    def get_car(self):
        return str(self.caracter)
    
    def get_posi(self):
        return str(self.pos)