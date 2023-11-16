ch=str(input('Donner une phrase : '))
voyelles = ["a","e","o","i","u","y"]

# 1er methode :
s=0
for i in range(0,len(ch)):
    if(ch[i] in voyelles):
        s+=1
print(f'Le nombre des voyelles dans {ch} est {s} ')
# 2eme methodek

v = list(filter(lambda x: x.lower() in ["a","e","o","i","u","y"],ch))
print(v)
print(len(v))
print(f'Le nombre des voyelles dans {ch} est {len(v)} ')


