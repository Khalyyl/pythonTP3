import statistics

# Saisir une liste de mots depuis l'utilisateur
user_input = input("Entrez une liste de mots séparés par des espaces : ")


# Diviser la chaîne de caractères en une liste de mots
words = user_input.split()


# Afficher la liste des mots saisis
print("Mots saisis :", words)


total_words=len(words)
print('Nombre total des mots saisie :',total_words)


total_word_length = sum(len(i) for i in words)
print("Longueur moyenne des mots de la liste",total_word_length / total_words)



#Mot le plus long dans la liste 
longest_word = max(words, key=len)
print("Mot le plus long :", longest_word)


mot_a_rechercher = input('Donner le mot a rechercher ')
if ( mot_a_rechercher in words):
    print(mot_a_rechercher,'est dans la liste',total_words)
else:
    print('La liste ne contienne pas le mot que vous allez de rechercher')

