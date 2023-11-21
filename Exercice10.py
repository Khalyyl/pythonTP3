X= {"a","b","c","d"}
Y= {"s","b","d"}

## Les ensembles initiaux ;
print(f"X = {X}")
print(f"Y = {Y}")

## Le test d’appartenance de l’élément‘c’ à X ;
print(f"c in X : {'c' in X}")
## Le test d’appartenance de l’élément‘A’ à Y ;
print(f"a in X : {'a' in Y}")

## Les ensembles X-Y et Y-X ;
print(f"X-Y : { X-Y}")

## L’ensemble Z=X union Y;
print(f"Z = X union Y : {X.union(Y)}")
print(f"W= W inter Y : {X.intersection(Y)}")