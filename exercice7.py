fichier1 = open("fichier1.txt","r")
text = fichier1.readline()

nombre_mots = text.split()
longueur = len(nombre_mots)
longueurstr = str(longueur)

fichier2= open("fichier2.txt","a")
fichier2.write("Le nombre de mots du fichier 1 est : "+ longueurstr)

fichier1.close()
fichier2.close()