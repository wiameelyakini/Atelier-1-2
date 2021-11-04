# on commence par definir la fonction inverse
def inverse(CH):
    # on cree une chaine de caractere vide
    resultat = ""
    # on initiale une boucle for pour repeter l'operation
    for val in CH:
        resultat = val + resultat
        # resultat= une chaine inversé
    return resultat


mot = str(input("saisir une chaine de caractere:"))
print("la chaine de caratere inversé est :", inverse(mot))
