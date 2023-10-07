n = int (input("Veuillez saisir la yaleur de n: "))
S = 0
for i in range( 0,n+1):
 S = S + (10 ** i)
print("La somme de la série est:",S)