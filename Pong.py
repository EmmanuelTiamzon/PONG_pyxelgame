import pyxel
import random

class Balle:
    def __init__(self):
        self.x=pyxel.width/2
        self.y=pyxel.height/2
        self.width=6
        self.height=6
        self.angle=pyxel.rndi(-70,70)+180*pyxel.rndi(0,1) 
        self.vitesse=4
        #On initialise la balle pour sa taille sa vitesse et son angle
        self.game_over=False #ici on dit que le jeu ne s'arrete pas qu'il commence directement
        self.score_1 = 0
        self.score_2 = 0
    def update(self):
        if self.game_over==False:
            self.x = self.x + self.vitesse * pyxel.cos(self.angle)
            self.y = self.y - self.vitesse * pyxel.sin(self.angle)
            if self.y - self.width/2<=0 or pyxel.height <= self.y + self.width/2>=0 :
                """
                ici lorsqu'on dit que la balle est divisé par deux enfin un peu partout dans le code, alors ça veut dire qu'il sort de l'ecran, qu'il va etre coupé en deux en sortant de l'ecran en passant par le coté sans collision soit celui de droite ou de gauche
                """
                self.angle = -self.angle
            if self.x - self.width/2 < 0:
                self.score_2 +=1
                self.x=pyxel.width/2
                self.y=pyxel.height/2
                self.vitesse = 4 #cette ligne réeinitialise la vitesse meme après le power up
            if self.x + self.width/2 > pyxel.width:
                self.score_1 += 1
                self.x=pyxel.width/2
                self.y=pyxel.height/2
                self.vitesse = 4
            
            
    def draw(self):
        pyxel.circ(self.x,self.y,self.width/2,13) #cette ligne est la pour dessiner la balle
        pyxel.text(60,3,str(self.score_1),7) #ces lignes servent à écrire le score 
        pyxel.text(100,3,str(self.score_2),7)

class Joueur1:
    def __init__(self):
        self.x=20
        self.y=pyxel.height/2
        self.width=5
        self.height=25
        self.vitesse=6
    def update(self):
        if pyxel.btn(pyxel.KEY_Z) and self.y > 0:
            self.y=self.y-self.vitesse
        elif pyxel.btn(pyxel.KEY_S) and self.y < 90 :
            self.y=self.y+self.vitesse
    def draw(self):
        pyxel.rect(self.x,self.y,self.width,self.height,5)
    def colision(self,balle):
        if balle.x - balle.width/2 <= self.x + self.width \
        and balle.x + balle.width/2 >= self.x \
        and balle.y + balle.width/2 >= self.y \
        and balle.y - balle.width/2 <= self.y+self.height :
            #ça définit la collision 
            balle.angle = 180-balle.angle #ici comme je l'ai compris si l'angle de la balle part en colision avec une raquette le plafond ou le sol alors ça renvoie l'opposé de son angle pour qu'il aille ou il faut.

class Joueur2:
    def __init__(self):
        self.x=130
        self.y=pyxel.height/2
        self.width=5
        self.height=25
        self.vitesse=6
    def update(self):
        if pyxel.btn(pyxel.KEY_UP) and self.y > 0:
            self.y=self.y-self.vitesse
        elif pyxel.btn(pyxel.KEY_DOWN) and self.y < 90 :
            self.y=self.y+self.vitesse
    def draw(self):
        pyxel.rect(self.x,self.y,self.width,self.height,10)
    def colision(self,balle):
        if balle.x - balle.width/2 <= self.x + self.width \
        and balle.x + balle.width/2 >= self.x \
        and balle.y + balle.width/2 >= self.y \
        and balle.y - balle.width/2 <= self.y+self.height :
            balle.angle = 180-balle.angle

class Powerup:
    def __init__(self):
        self.x = random.randint(30,120)
        self.y = random.randint(20,90)
        self.x2 = 90
        self.y2 = 60
        self.width = 8
        self.height = 8
    
    def update(self):
        pass #ici je met un pass car je trouvais pas quoi mettre d'autre ici, sachant que j'ai pris du temp à comprendre que le jeu ne marcherais pas sans update dans cette class 
        
    def draw(self):
        pyxel.load("res.pyxres")
        pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8,random.randint(1,7))
        pyxel.blt(self.x2, self.y2, 0, 0, 0, 8, 8,random.randint(1,7))#ici j'ai mis random randint pour la couleur sans savoir qu'il allait juste clignoter mais ça me plait alors je l'ai gardé tel quel
        #ça m'a pris du tempmais j'ai réussi à comprendre comment mettre une image ou plutot un dessin fait moi meme 
    
    def colision(self,balle):
        if balle.x - balle.width/2 <= self.x + self.width \
        and balle.x + balle.width/2 >= self.x \
        and balle.y + balle.width/2 >= self.y \
        and balle.y - balle.width/2 <= self.y+self.height :
            #si il y a une colision entre la balle et ce power up alors tout d'abord la balle change d'emplacement et augmente en vitesse
            self.x= random.randint(30, 120)
            self.y= random.randint(20, 90)
            balle.vitesse *= 1.4
            
        if balle.x - balle.width/2 <= self.x2 + self.width \
        and balle.x + balle.width/2 >= self.x2 \
        and balle.y + balle.width/2 >= self.y2 \
        and balle.y - balle.width/2 <= self.y2+self.height :
            #si il y a une colision entre la balle et ce power up alors tout d'abord la balle change d'emplacement et diminue en vitesse
            self.x2= random.randint(30, 120)
            self.y2= random.randint(20, 90)
            balle.vitesse *= 0.7
            

class Game:
    def __init__(self):
        pyxel.init(160,119,fps=24)
        self.player1 = Joueur1()
        self.player2 = Joueur2()
        self.boule=Balle()
        self.powerawp = Powerup()
        #ici on donne des noms qu'on pourra utiliser en dessous
        pyxel.run(self.update, self.draw)

    def update(self):
        self.player1.update()
        self.player2.update()
        self.boule.update()
        self.powerawp.update()
        self.powerawp.colision(self.boule)
        self.player1.colision(self.boule)
        self.player2.colision(self.boule)
        #on "active" les update
    def draw(self):
        pyxel.cls(0) #pour un écran noir
        pyxel.line(pyxel.width // 2, 0, pyxel.width // 2, pyxel.height, 7) #ici pour la ligne, il calcule ou mettre la ligne pour le mettre parfaitement au milieu 
        self.player1.draw()
        self.player2.draw()
        self.boule.draw()
        self.powerawp.draw()
Game()
#Voila mon code j'espère qu'il vous aura plus, merci.
