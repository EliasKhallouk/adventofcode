# LECTURE DU FICHIER
with open('Day03/input.txt', 'r') as file:
    data = file.read()

# CALCULE DU RESULTAT DE LA MULTIPLICATION
data = data.split('mul(')
compteur=0
flague = True
for i in range(len(data)):
    sauv=data[i]
    try:
        data[i] = data[i].split(',')
        data[i][1] = data[i][1].split(')')
        if(0<int(data[i][0])<1000 and 0<int(data[i][1][0])<1000 and ' ' not in data[i][0] and ' ' not in data[i][1][0] and len(data[i][1])>1 and flague==True):
            compteur+=int(data[i][0])*int(data[i][1][0])
    except:
        pass

    if ("don't()" in sauv):
        flague = False
    if ("do()" in sauv):
        flague = True

# AFFICHAGE DU RESULTAT DE LA MULTIPLICATION
print(compteur) # --> 74361272