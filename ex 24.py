SET1={23,42,65,57,78,83,29}
SET2={57,83,29,67,73,43,48}
SET3=SET1.intersection(SET2)
for val in SET3:
    SET1.remove(val)

print('intersection commune des deux sets est:',SET3)
print('le 1er set devient :',SET1)