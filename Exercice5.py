from math import sin
## Construire la liste des carrés et celle des cubes de tous les nombres de 20 à 40
carre = [x**2 for x in range(20,41)]
print(carre)
cube = [x**3 for x in range(20,41)]
print(cube)
## Construire laliste despuissancesde5pourtouteslesvaleursd’exposantdansl’intervalle[6,14]
puissance_de_5 = [5**x for x in range(4,17) ]
print(puissance_de_5)
## Construire la liste des sinus des angles de 0à 90 degrés par pas de 5 degrés
sinus = [sin(x) for x in range (0,91,5)]
print(sinus)

