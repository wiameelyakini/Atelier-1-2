# on definit une fonction somme en utilisant la recursivite
def somme(n):
    if n >= 1:
        return n + somme(n - 1)
    return n


# on demande au utilisateur d'entrer un nombre
n = int(input("veuillez saisir un nombre :"))
print("la somme est :", somme(n))
