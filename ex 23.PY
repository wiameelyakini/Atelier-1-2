LIST=[11,45,8,11,23,45,23,45,89]
dict={}
for val in LIST :
    if val not in dict.keys() :
        dict[val]=1
    else: 
            dict[val]=dict[val] + 1

print(dict)