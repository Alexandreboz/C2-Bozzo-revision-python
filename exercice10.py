liste = {1, 5, 45, 5, 3, 10}

def tri_insertion(liste):
    n = len(liste)
    for n in range (1,n):
        key = liste(n)
        j = n-1
        while j>=0 and liste[j] > key:
            liste[j+1] = liste[j]
            j = j-1
        liste[j+1] = key
print(liste)