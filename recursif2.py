from turtle import *
from random import randint
from math import sqrt
choix = randint(1,2)
if choix == 1:
  couleur = []
  for i in range(100):
    couleur.append(randint(0,255))
  pencolor("white")
  def carre(cote,n):
    fillcolor(couleur[3*n],couleur[3*n+1],couleur[3*n+2])
    begin_fill()
    for i in range(4):
      forward(cote)
      right(90)
    end_fill()  
  
  def arbre_pythagore(cote,n):
    if n > 0:
      n = n - 1
      carre(cote,n)
      forward(cote)
      cote2 = cote/sqrt(2)
      left(45)
      arbre_pythagore(cote2,n)
      right(90)
      up()
      forward(cote2)
      down()
      arbre_pythagore(cote2,n)
      left(180)
      up()
      forward(cote2)
      down()
      left(45)
      forward(cote)
      left(180)
      
  speed(0)
  setheading(90)
  up()
  goto(-40,-150)
  down()
  arbre_pythagore(80,6)
else:
  speed(0)
  angle = 30
  color('#3f1905')
  def arbre(n,longueur):
      if n==0:
          color('green')
          forward(longueur) # avance
          backward(longueur) # recule
          color('#3f1905')
      else:
          forward(longueur/3) #avance
          left(angle) # tourne vers la gauche de angle degrés
          arbre(n-1,longueur*2/3)
          right(2*angle) # tourne vers la droite de angle degrés
          arbre(n-1,longueur*2/3)
          left(angle) # tourne vers la gauche de angle degrés
          backward(longueur/3) # recule
  hideturtle() # cache la tortue
  up() # lève le stylo
  right(90) # tourne de 90 degrés vers la droite 
  forward(100) # avance de 300 pixels
  left(180) # fait un demi-tour
  down() # pose le stylo
  arbre(8,300) # exécute la macro
  showturtle() # affiche la tortue
  
