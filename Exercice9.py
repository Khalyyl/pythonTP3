ch=input('Donner une chaine')
list_chaine = list("".join(ch.split(" ")))
print(list_chaine)
Nb_char = len(list_chaine)
print(f"Le nombre des caractère : {Nb_char}")

dict={}
for char in list_chaine:
    if char not in dict:
        dict[char]=1
    else:
        dict[char]+=1

for key,val in dict.items():
     print(f"{key} : {(val/Nb_char)*100}%")