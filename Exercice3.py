## Insertion d'une liste par utilisateur : 
while True:
    taille_liste=int(input('Donner la taille de la liste'))
    if(taille_liste>0):
        break;

liste=[]
for i in range(0,taille_liste):
    x=int(input(f'Donner liste[{i}]'))
    liste.append(x)
print(liste)
print("La somme de la liste :",sum(liste[::]))
print("Min liste",min(liste))
print("Max liste",max(liste))

## 