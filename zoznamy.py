import random
# max = teploty[0]
# for i in teploty:
#     if max < i :
#         max = i
#     print(max)

# count, index, append, pop, insert(index, hodnota), remove(hodnota), sort

# def generuj(x=20,m=0,n=100):
#     zoznam = []
#     for i in range(x):
#         cislo = random.randint(m,n)
#         zoznam.append(cislo)
#     return zoznam
#
# def vypis():
#     a = str(generuj())
#     for i in a:
#         print(a[i] + "\n")
#
# vypis()

cisla = [5,7,8,6,4,1,2,9,3]
def bublinkovy(nz):
    z = list(nz)
    n = len(z)
    for i in range(n):
        for j in range(n-1):
            if z[j] > z[j+1]:
                z[j],z[j+1] = z[j+1],z[j]
    return z

def bublinkovy2(nz):
    z = list(nz)
    n = len(z)
    for j in range(n):
        for i in range(j,n):
            if z[i] < z[j]:
                z[i],z[j] = z[j],z[i]
    return z

print(cisla)
print(bublinkovy(cisla))
print(cisla)
print(bublinkovy2(cisla))
