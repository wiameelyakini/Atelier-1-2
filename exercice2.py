# on definit la fonction binaire , qui fait convertir un nombre decimal a un nombre binaire
def binaire(n):
    # on crée une chaine vide
    binaire = ""
    while n != 0:
        binaire += str(n % 2)
        n = n // 2
        # on ajoute le dernier element a la chaine de caractere
    return binaire[::-1]


# on demande au utilisateur d'entrer un nombre
n = int(input("veuillez saisir un nombre :"))
print("le nombre en binaire est :", binaire(n))
