while True:
    taille_liste = int(input("Donner la taille de la liste : "))
    if(taille_liste>0):
        break;
t = []
for i in range(0, taille_liste):
    x = int(input(f"Donner le t[{i}] : "))
    t.append(x)

t2 = []

for i in range(0, len(t)):
    t2.append(sum(t[:i+1]))


x = float(input("Donner un entier decimal : "))
n = int(input("Donner le nombre des decimales : "))

print(list(str(x).split(".")[1][0:n]))