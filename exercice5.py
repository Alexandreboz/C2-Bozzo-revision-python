n = int(input("Tappez un nombre "))
def factorielle(n):
    if n ==0:
        return 1
    else :
        F = 1
        for k in range(2,n+1):
            F = F*k
        return F
    
resultat = factorielle(n)

print(resultat)