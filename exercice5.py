# on commence par la definition de la fonction qui calcule le nombre de chiffres d'un nombre saisi
def nbr(n):
    if n < 10:
        return 1
    else:
        return 1 + nbr(n / 10)


# on demande a l'utilisateur de entrer un nombre
N = int(input("saisir le nombre :"))
print("le nombre de chiffre de", N, "est", nbr(N))
