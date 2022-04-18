from turtle import*
from random import*
#adrien le 28/03/2021
n = 10

############### 1 #################
if n == 1:
  clear()
  up()
  goto(-40, -40)
  setheading(0)
  down()
  for k in range(4):
      forward(80)
      left(90)
############### 2 #################
elif n == 2:
  clear()
  up()
  goto(-40, -40)
  setheading(0)
  down()
  for k in range(3):
      forward(70)
      left(120)
############### 3 #################
elif n == 3:
  def carre(cote):
      for k in range(4):
          forward(cote)
          left(90)
  goto (-40, -40)
  setheading(0)
  clear()
  cote = 120
  for i in range(4):
      carre(cote)
      cote = cote-20
############### 4 #################
elif n == 4:
  def carre(cote):
      for k in range(5):
          forward(cote)
          left(90)
  goto (-180, -40)
  setheading(0)
  clear()
  cote = 120
  for i in range(4):
      carre(cote)
      right(90)
      cote = cote-20
############### 5 #################
elif n == 5:
  shape('turtle')
  pencolor('red')
  pensize(4)
  speed(5)
  def triangle(cote):
      for k in range(4):
          forward(cote)
          left(120)
  goto (-180, -40)
  setheading(0)
  clear()
  cote = 120
  for i in range(4):
      triangle(cote)
      right(120)
      cote = cote-20
############### 6 #################
elif n == 6:
  def carre(x, y):
    up()
    goto(x, y)
    down()
    setheading(0)
    color("blue")
    begin_fill()
    for i in range(4):
      forward(40)
      left(90)
    end_fill()
    up()
  for k in range(-150, 200, 50):
    carre(k, 80)
############### 7 #################
elif n == 7:
  speed(0)
  couleur = ["red", "blue", "green", "black", "purple", "pink", "orange", "yellow", "grey", "brown", "cyan", "fuchsia" ]
  def carre(x, y):
    up()
    goto(x, y)
    down()
    setheading(0)
    color(choice(couleur))
    begin_fill()
    for i in range(4):
      forward(40)
      left(90)
    end_fill()
    up()
  for k in range(-180, 180, 45):
    for m in range(150, -210, -45):
      carre(k,m)
############### 8 #################
elif n == 8:
  speed(0)
  hideturtle()
  def carre(x, y):
    up()
    goto(x, y)
    down()
    setheading(0)
    color("blue")
    begin_fill()
    for i in range(4):
      forward(40)
      left(90)
    end_fill()
    up()
  for k in range(-180, 180, 45):
    for m in range(150, -210, -45):
      carre(k,m)
  def disque(x,y,couleur):
    up()
    goto(-160+(x-1)*45,-145+(y-1)*45)
    down()
    dot(38,couleur)
    up()
  for i in range(1,9):
    for j in range(1,9):
      disque(i,j,"white")
  disque(4,1,"red")
  goto(-163,192)
  write(1)
############### 9 #################
elif n == 9:
  speed(0)
  hideturtle()
  def carre(x, y):
    up()
    goto(x, y)
    down()
    setheading(0)
    color("blue")
    begin_fill()
    for i in range(4):
      forward(30)
      left(90)
    end_fill()
    up()
  for k in range(-175, 105, 35):
    for m in range(-100, 180, 35):
      carre(k,m)
  def disque(x,y,couleur):
    up()
    goto(-160+(x-1)*35,-85+(y-1)*35)
    down()
    dot(28,couleur)
    up()
  for i in range(1,9):
    for j in range(1,9):
      disque(i,j,"white")
  for i in range(8):
    goto(-163+35*i,180)
    write(i+1)
  grille = 8*[0]
  compteur = 1
  while compteur < 65:
    if compteur%2 == 0:
      jj = 2
      cc = "red"
    else:
      jj = 1
      cc = "yellow"
    print "joueur",jj
    choix = int(input("votre choix :"))
    if grille[choix-1] !=8:
      disque(choix,grille[choix-1]+1,cc)
      grille[choix-1] = grille[choix -1]+1
      compteur = compteur + 1
############### 10 #################
elif n == 10:
  prenom = [0,0]
  prenom[0] = input("joueur 1, votre prenom :")
  prenom[1] = input("joueur 2, votre prenom :")
  speed(0)
  hideturtle()
  def carre(x, y):
    up()
    goto(x, y)
    down()
    setheading(0)
    color("blue")
    begin_fill()
    for i in range(4):
      forward(30)
      left(90)
    end_fill()
    up()
  for k in range(-175, 70, 35):
    for m in range(-30, 180, 35):
      carre(k,m)
  def disque(x,y,couleur):
    up()
    goto(-160+(x-1)*35,-15+(y-1)*35)
    down()
    dot(26,couleur)
    up()
  for i in range(1,8):
    for j in range(1,7):
      disque(i,j,"white")
  for i in range(7):
    goto(-163+35*i,180)
    write(i+1)
  goto(-125, -60)
  color("yellow")
  write(prenom[0], font=("Arial", 18, "normal"), align="center")
  goto(-55, -60)
  color("black")
  write("-vs-", font=("Arial", 18, "normal"), align="center")  
  goto(15, -60)
  color("red")
  write(prenom[1], font=("Arial", 18, "normal"), align="center")
  goto(-55, -100)
  color("green")
  write("PUISSANCE 4", font=("Arial", 18, "normal"), align="center")
  grille = 8*[0]
  compteur = 1
  while compteur < 43:
    if compteur%2 == 0:
      print prenom[1]
      cc = "red"
    else:
      cc = "yellow"
      print prenom[0]
    rep = 0
    while rep == 0:
      choix = raw_input("votre choix :")
      try:
        int(choix)
        rep = 1
        break
      except ValueError:
        print("Entrez un entier entre 1 et 7")
    choix = int(choix)    
    if choix > 7 or choix < 1:
      print("Entrez un entier entre 1 et 7")
    elif grille[choix-1] !=6:
      disque(choix,6,cc)
      for i in range(6, grille[choix-1]+1,-1):
        disque(choix,i-1,cc)
        disque(choix,i,"white")
      grille[choix-1] = grille[choix -1]+1
      compteur = compteur + 1
