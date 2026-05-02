from itertools import filterfalse
import pygame
import random
import sys

pygame.init()

largeur, hauteur = 800, 600
taille = 20 
vitesse = 10 

noir = (0, 0, 0)
blanc = (255, 255, 255)
vert  = (0, 255,0)
rouge = (255, 0, 0)
bleu = (50, 150, 255)

nbr_largeur = largeur // taille 
nbr_hauteur = hauteur // taille 

fenetre = pygame.display.set_mode((largeur, hauteur))
pygame.display.set_caption("Snake")
horloge = pygame.time.Clock()

def affichage(texte, couleur, x,y, taille = 30) : 
    police = pygame.font.SysFont("Poppins", taille)
    surface = police.render(texte, True, couleur)
    fenetre.blit(surface, (x, y))

def nourriture(snake):
    while True:
        x = random.randint(0, nbr_largeur - 1) 
        y = random.randint(0, nbr_hauteur - 1)
        if [x,y] not in snake: 
            return [x,y]
        
def jeu (): 
    snake = [[nbr_largeur // 2, nbr_hauteur // 2]]
    direction = [1, 0]
    point_rouge = nourriture(snake)
    score = 0
    jeu_en_cours = True
    
    while jeu_en_cours:
        for event in pygame.event.get():    
            if event.type == pygame.QUIT: 
                pygame.quit()  
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction !=[0, 1]:
                    direction =  [0, -1] 
                elif event.key == pygame.K_DOWN and direction !=[0, -1]:
                    direction = [0, 1]
                elif event.key == pygame.K_LEFT and direction !=[1, 0]:
                    direction = [-1, 0]
                elif event.key == pygame.K_RIGHT and direction !=[-1, 0]:
                    direction = [1, 0]  
            
        tete = snake[0].copy()
        tete[0] +=  direction[0]
        tete[1] += direction[1]
    
        if (tete[0] < 0 or tete[0] >= nbr_largeur or tete[1] < 0 or tete[1] >= nbr_hauteur ):
            jeu_en_cours = False
 
        snake.insert(0, tete)
    
        if tete == point_rouge:
            point_rouge = nourriture(snake)
            score +=1
        else:
            snake.pop()
  
        if tete in snake[1:]:
            jeu_en_cours = False
    
        fenetre.fill(noir)
        
        pygame.draw.circle(fenetre, rouge, 
                           (point_rouge[0] * taille + taille // 2, point_rouge[1] * taille + taille // 2),
                           taille // 2)   
        for segment in snake : 
            pygame.draw.rect(fenetre, vert, 
                            (segment [0] * taille, segment [1] * taille, 
                            taille, taille))
 
        affichage(f"Score: {score}", blanc, 10, 10)
        pygame.display.flip()
        horloge.tick(vitesse)
    
    fenetre.fill(noir)
    affichage(f"Game Over!", rouge, largeur // 2 - 80, hauteur // 2 - 40, 50)
    affichage(f"Score final: {score}", blanc, largeur // 2 - 90, hauteur // 2 + 10, 35)
    affichage("Appuyer sur une touche pour quitter", bleu, largeur // 2 - 220, hauteur // 2 + 80, 25)
    pygame.display.flip()
    
    attente = True 
    while attente: 
        for event in pygame.event.get():
          if event.type == pygame.QUIT: 
              attente = False
          if event.type == pygame.KEYDOWN:
              attente = False 
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    jeu()