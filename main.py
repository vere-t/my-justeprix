#bienvenue


start_game = input("Bienvenue ,entrez ok pour commencer la partie : ")

while start_game != "ok":
    start_game = input("Bienvenue ,entrez ok pour commencer la partie : ")
print("Let's play")



from random import randint
good_number = randint(1,100)
guess_number = input("choisir un nombre entre 1 et 100 :")

while guess_number != good_number:
    if guess_number.isdigit() == False:
        print ("error")
        guess_number = input("choisir un nombre entre 1 et 100 :")
    else:
        guess_number = int(guess_number)
        
        if guess_number > 100:
            print(" ce nombre trop grand !")
            guess_number = input("choisir un nombre entre 1 et 100 :")
        elif guess_number < good_number:
            print("trop petit try again noob")
            guess_number = input("choisir un nombre entre 1 et 100 :")
        elif guess_number > good_number:
            print("trop grand try again noob!")
            guess_number = input("entrez un nombre :")
        
        else:
            print("you good bruv ")


print(f"You win congratulations ,the answer was : {good_number}.")
