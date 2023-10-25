note = {
    "Alex" : 20,
    "Yassine" : 19,
    "Marine" : 1
}

meilleur = max(note, key=lambda eleve : note[eleve])

print("Le meilleur élève est : ", meilleur)