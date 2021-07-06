#Le nombre que vous voulez faire deviner
#         |
#         v        
number = 356

running = True

while running:

    user_number = int(input("Entrer un nombre :"))

    if user_number == number:
     print("Bravo c'est gagné !")
     print("Fin du jeu vous avez remporté........Rien")
     running = False
    

    elif user_number > number:
     print("C'est moins l'amis !")
    elif user_number < number:
     print("C'est plus mon amis")
    




