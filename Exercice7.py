ch="un bon étudiant est celui qui révise chaque jour son cours"
ch1 = ch.split(' ')[1]
print(ch1)

# un bon bonbon
ch2 = " ".join(ch.split(" ")[0:2]) +" "+ (ch.split(" ")[1]*2) 
print(ch2)

#cours
ch3 = ch.split(" ")[-1]
print(ch3)

## est celui qui révise 
ch4 = " ".join(ch.split(' ')[3:7])
print(ch4)