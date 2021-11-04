# on commence par definir la fonction de la serie fibonacci en utilisant la recursivite
def fibonacci(n):
    if(n == 0):
        return 0
    if(n == 1):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


X = int(input("Veuillez entrer le nombre de termes:"))
# boucle for pour utiliser la fonction de fibonacci
for i in range(X+1):
    print(fibonacci(i))
