#lista=[43, 'hola', False, 234]
#for i in range(1,2):
#    print(lista[i])
#lista.append(5)
#lista.pop(2)
#l = [34, 543, 54, 2, 6]
#l.reverse
#l.sort

#print(l)


lis = [10,5,7,11,2,1]
n = len(lis)


for i in range(n, -1):
    for j in range(i+1,n):
        if n[i]<n[j]:
            aux=n[i]
            n[i]=n[j]
            n[j]=n
        else:
            print()
print()