import pygame, sys, time, mixer
from pygame.locals import *
from pygame.sprite import *


# Κλάση Game. Η κλάση αυτή περιέχει τον constructor και δύο μεθούδους για την εμφάνιση του σκορ.
class Game():
    score1 = 0
    score2 = 0

    def __init__(self):
        pass

# Κάθε φορά που η μπάλα ακουμπάει σε ένα όριο από δεξιά ή αριστερά, αυξάνεται η βαθμολογία του αντιστοιχου παικτη από την άλλη.
    def changeScore(self,side):
        if side == 2:
            Game.score1 += 1
        elif side == 3:
            Game.score2 += 1
        

        
    def printscore1(self, surf):
        my_font1 = pygame.font.SysFont(None, 70)    
        my_text1 = my_font1.render\
                  (str(Game.score1), True, (50,255,255), (0,0,0))  
        surf.blit(my_text1, (720, 20))

    def printscore2(self, surf):
        my_font2 = pygame.font.SysFont(None, 70)    
        my_text2 = my_font2.render\
                  (str(Game.score2), True, (50,255,255), (0,0,0))  
        surf.blit(my_text2, (20, 20))


    def printwinner(self, surf):
        surf.fill((0,0,0))
        surfcX=surf.get_rect().centerx
                
        my_font = pygame.font.SysFont(None, 64)
        if Game.score1==20:
            my_text = my_font.render\
                  ('PLAYER 1 WINS!', True, (255,255,255))
            my_textRect=my_text.get_rect()
            my_textRect.centerx=surfcX
            my_textRect.centery=100
            surf.blit(my_text, my_textRect)
            
        elif Game.score2==20:
            my_text = my_font.render\
                  ('PLAYER 2 WINS!', True, (255,255,255))
            my_textRect=my_text.get_rect()
            my_textRect.centerx=surfcX
            my_textRect.centery=100
            surf.blit(my_text, my_textRect)
     


        
class Object(Sprite):
    def __init__(self, createX, createY,\
                 dimX, dimY, speedX, speedY, name):
        Sprite.__init__(self)
        self.rect= pygame.Rect(createX, createY, dimX, dimY)
        self.image= pygame.image.load(name)
        self.speedX=speedX
        self.speedY=speedY
    def move(self, surf):
        
        pass
                   
# ΚΛάση Ball- υποκλάση της Object που δημιουργεί ένα rect, με ένα image και διαμορφώνει την ταχύτητα του.

class Ball(Object):
    def __init__(self, createX, createY):
        Object.__init__(self, createX, createY,\
                 dimX=32, dimY=32, speedX=-7, speedY=4, name='pingpong.jpg')        
        
    def move(self, surf):
        self.rect.move_ip(self.speedX, self.speedY)
        surf.blit(self.image, self.rect) 
        return self.check_bounce()

    def check_bounce(self, horiz=800, vert=600):  #Γίνονται οι έλεγχοι πρόσκρουσης της μπάλας στις πλευρές της οθόνης
        side=0
        if self.rect.top<0:
            self.speedY = -self.speedY
            side = 1
        elif self.rect.bottom>vert:
            self.speedY = -self.speedY
            side = 4
        elif self.rect.left<0:
            self.speedX = -self.speedX
            side = 2
        elif self.rect.left<0 or self.rect.right>horiz:
            self.speedX = -self.speedX
            side = 3
        return side                               # Η μπάλα προσκρούει σε κάθε πλευρά συνεχίζοντας την κίνησης της και μην διακόπτοντας την ροή που θα είχε
                                                  # αν παιζοταν ανάμεσα σε 2 αληθινούς τοίχους. Επίσης η ταχύτητα είναι αυξημένη για να είναι πιο ενδιαφέρον
                                                  # το παιχνίδι.


# Κλάσεις (υποκλάσεις Object) για την δημιουργία των ρακετών και των κινήσεων τους.
# Η εικόνα που φορτώνει ειναι μια ζωγραφισμένη ρακέτα με τις ρεαλιστικές διαστάσεις της και όχι τετραγωνοποιημένο
# image έτσι ώστε η πρόσκρουση σε μια ρακέτα να γίνεται πιο αληθοφανής. Δηλαδή ο παίκτης θα πρέπει να προσέξει να 
# να χτυπήσει την μπάλα με την επιφάνεια της ρακέτας και όχι με την βάση όπου η μπάλα θα έχει απροσδιόριστη τροχιά.

class Raketa1(Object):
    def __init__(self, createX, createY):
        Object.__init__(self, createX, createY,\
                 dimX=80, dimY=150, speedX=0, speedY=5, name='racket.jpg')   
        self.transimage = pygame.transform.scale(self.image, (80, 120))
        self.moveUp=False
        self.moveDown=False

    def move(self, surf):
        if self.moveUp and self.rect.top>0:
            self.rect.move_ip(0, -self.speedY)
        if self.moveDown and self.rect.bottom<600:
            self.rect.move_ip(0, self.speedY)
        surf.blit(self.transimage, self.rect)


class Raketa2(Object):
    def __init__(self, createX, createY):
        Object.__init__(self, createX, createY,\
                 dimX=80, dimY=150, speedX=0, speedY=5, name='racket.jpg')   
        self.transimage = pygame.transform.scale(self.image, (80, 120))
        self.moveUp=False
        self.moveDown=False
        
    def move(self, surf):
        if self.moveUp and self.rect.top>0:
            self.rect.move_ip(0, -self.speedY)
        if self.moveDown and self.rect.bottom<600:
            self.rect.move_ip(0, self.speedY)
        surf.blit(self.transimage, self.rect)



#Έχουμε επέκταση μεθόδου στην περιπτωση της move, η οποία στις κλάσεις Ball, Raketa1, Raketa2 κληρονομεί από την Object
#και πολυμορφισμό με την διαφορετική συμπεριφορα της σε αυτές.

