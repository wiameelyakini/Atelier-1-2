LIST = [47, 64, 69, 37, 76, 83, 95, 97]
dict = {'yassine': 47, 'imane': 69, 'mohamed': 76, 'abir': 97}
# on va creer une liste vide pour qu'on place les elements de la liste
# et qui se trouvent aussi dans le dictionnaire en tant que valeur, dans cette liste vide
LISTV = []
for val in LIST:
    if val in dict.values():
        LISTV.append(val)
# affichage du resultat
print(LISTV)
