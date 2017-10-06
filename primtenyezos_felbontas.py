from math import sqrt
print("Prímtényezős felbontás\n-----------------------")
inp = int(input("Vizsgálandó: "))
nums = list(range(1,inp)) + [inp]
osztok = []; primek = []; tenyezok = []
def oszt(z):
    x = 1
    while x <= sqrt(z):
        if z % x == 0 and x != z/x :
            osztok.append(int(x))
            osztok.append(int(z/x))
        if z % x == 0 and x == z/x:
            osztok.append(x)
        x += 1
for i in nums :
    oszt(i)
    if len(osztok) == 2 : 
        primek.append(i)
        osztok = []
    else:
        osztok = []
y = 0
while y < len(primek) :
    if inp % primek[y] == 0 and inp != primek[y] :
        tenyezok.append(primek[y])
        inp /= primek[y]
        continue
    elif inp == primek[y] :
        tenyezok.append(primek[y])
        break
    else: 
        y += 1
if len(tenyezok) == 1 :
    print("Prímszám:",tenyezok,"\n-----------------------")
else:
    print("Prímtényezők:",tenyezok,"\n-----------------------")
wait = input()
