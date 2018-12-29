import pygame, sys, time, mixer, mylib2234
from pygame.locals import *
from mylib2234 import *

pygame.init()



# -- MAIN ------------------------
my_clock = pygame.time.Clock()

# (2) ΕΝΑΡΞΗ - SETUP
# Ανάλυση
HORIZ=800
VERT=600

# Οθόνη
my_screen = pygame.display.set_mode((HORIZ, VERT), 0, 32)
pygame.display.set_caption('PING PONG')

# Χρώματα
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

my_screen.fill(BLACK)

# Μουσική
my_music= pygame.mixer.music.load('Doom.mp3')
pygame.mixer.music.play(-1)


# Δημιουργία αντικειμένου my_ball --> Ball type 
my_ball = Ball(500, 50)

# Δημιουργία αντικειμένων για τις 2 ρακέτες --> Raketa1 και Raketa2 type  
racket1 = Raketa1(720, 250)
racket2 = Raketa2(15, 250)

# Δημιουργία αντικειμένου my_game --> Game type 
my_game = Game()



pygame.display.update()


#=========================================================
# (3) ΒΡΟΧΟΣ ΠΑΙΧΝΙΔΙΟΥ
case=True
while case:
    for ev in pygame.event.get():    
        if ev.type == QUIT:
            pygame.quit()                
            sys.exit()

        #Κινήσεις παίκτη_1
        if ev.type == KEYDOWN:
            if ev.key == K_UP:
                racket1.moveUp = True
            if ev.key == K_DOWN:
                racket1.moveDown = True
            if ev.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if ev.type == KEYUP:
            if ev.key == K_UP:
                racket1.moveUp = False
            if ev.key == K_DOWN:
                racket1.moveDown = False

        #Κινήσεις παίκτη_2
        if ev.type == KEYDOWN:
            if ev.key == K_w:
                racket2.moveUp = True
            if ev.key == K_s:
                racket2.moveDown = True
            if ev.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

        if ev.type == KEYUP:
            if ev.key == K_w:
                racket2.moveUp = False
            if ev.key == K_s:
                racket2.moveDown = False

    # ΛΟΓΙΚΗ ΠΑΙΧΝΙΔΙΟΥ
    my_screen.fill(BLACK)  
    
    my_game.changeScore(my_ball.move(my_screen))
    racket1.move(my_screen)
    racket2.move(my_screen)


    #Έλεγχος πρόσκρουσης της μπάλας στη ρακέτα
    if my_ball.rect.colliderect(racket1.rect):
        my_ball.speedX= -my_ball.speedX
        my_ball.move(my_screen)

    if my_ball.rect.colliderect(racket2.rect):
        my_ball.speedX= -my_ball.speedX
        my_ball.move(my_screen)
      
    

    #Έλεγχος λήξης παιχνιδιού
    if my_game.score1==20 or my_game.score2==20:
        my_game.printwinner(my_screen)
        case=False

    my_game.printscore1(my_screen)
    my_game.printscore2(my_screen)

    pygame.display.update()   
    

    my_clock.tick(120)
  


    
