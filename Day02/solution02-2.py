# LECTURE ET STRUCTURATION DU FICHIER
with open('Day02/input.txt', 'r') as file:
    data = file.read()
data = data.split('\n')
data = [[int(num) for num in line.split()] for line in data if line]

# CALCUL DU NOMBRE DE RAPPORT SURS
def is_safe(report):
    variation = 0
    old_number = report[0]
    for j in range(1, len(report)):
        difference = abs(report[j] - old_number)
        if report[j] > old_number and (variation == 1 or variation == 0) and 1 <= difference <= 3:
            old_number = report[j]
            variation = 1
        elif report[j] < old_number and (variation == 2 or variation == 0) and 1 <= difference <= 3:
            old_number = report[j]
            variation = 2
        else:
            return False
    return True

compteur = 0
for report in data:
    if is_safe(report):
        compteur += 1
    else:
        for i in range(len(report)):
            if is_safe(report[:i] + report[i+1:]):
                compteur += 1
                break

# AFFICHAGE DU NOMBRE DE RAPPORT SURS
print(compteur) # --> 404
