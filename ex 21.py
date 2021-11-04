LIST1 = [3, 6, 9, 12, 15, 18, 21]
LIST2 = [4, 8, 12, 16, 20, 24, 28]
LIST3 = []
for i in range(len(LIST1)):
    if(i % 2 == 0):
        LIST3.append(LIST1)
    for i in range(len(LIST2)):
        if(i % 2 != 0):
            LIST3.append(LIST2)

print("la liste finale est:", LIST3)
