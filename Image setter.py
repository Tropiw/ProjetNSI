from PIL import Image   

class tile:
    SIZE = 16 # width and length

    def __init__(self, fichier):
        self.img = Image.open(fichier)


    def debug_afficher(self):
        self.img.show()

    def load(self,i, j):
        return self.img.crop(
            (
                i * tile.SIZE, #gauche
                j*tile.SIZE, #haut
                (i+1)*tile.SIZE, #droite
                (j+1)*tile.SIZE #bas
            )
        )



