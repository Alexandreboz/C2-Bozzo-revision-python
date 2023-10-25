def addition (n1, n2):
    return n1 + n2
def soustraction (n1, n2):
    return n1 - n2
def multiplication (n1, n2):
    return n1 * n2
def division (n1, n2):
    if n2 != 0:
        return n1 / n2
    else :
        return "Erreur"
        
operation = {
    '+' : addition,
    '-' : soustraction,
    '*' : multiplication,
    '/' : division
}

n1 = int(input("taper le premier nombre "))
n2 = int(input("taper le deuxième nombre "))
choix = input ("choississez l'opérateur")

resultat = operation[choix](n1,n2)
print("Le résultat est : ",resultat)

