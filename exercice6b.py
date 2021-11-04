# Tri à bulle :
def tri_bulle(tab):
    echange = True
    while echange:
        echange = False
    for i in range(len(tab) - 1):
        if tab[i] > tab[i + 1]:
            tab[i], tab[i + 1] = tab[i+1], tab[i]
            echange = True
