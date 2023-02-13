#Ajout de "0" lorsque le nombre passé en paramètre n'est pas assez long
#pour remplir 8 caractères
def dectobin(n):
	n,y = bin(n)[2:],8
	sep,j,x = " ",y,len(n)
	if x%y != 0:
		n = "0"*(y-x%y) + n
	L = [(n[i:i+j]) for i in range(0, len(n), j)]
	return sep.join(L) if (int(n,2) <= 255) else None
print(dectobin(5))