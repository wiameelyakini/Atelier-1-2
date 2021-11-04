LIST=[11,45,8,23,14,12,78,45,89]
n=3
RAN=[LIST[i * n:(i+1) * n]
for i in range ((len(LIST) + n - 1)//n)]
print(RAN)