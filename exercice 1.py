# on  definit une fonction factoriel en utilisant la recursivite
def factoriel(n):
    if n == 0 or n == 1:
        return 1
    return n * factoriel(n-1)


# on utilise la fonction pour calculer de la somme de la serie debutant de 1 a 5
U1 = 0
somme = 0
for i in range(1, 7):
    somme = somme + U1
    U1 = factoriel(i) / i
print("la somme de la serie est :", somme)
