from itertools import product

# LECTURE DU FICHIER
with open('Day07/input.txt', 'r') as file:
    equations = file.readlines()

# FONCTION POUR ÉVALUER UNE EXPRESSION GAUCHE-À-DROITE
def evaluate_left_to_right(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
    return result

# INITIALISATION DU RÉSULTAT TOTAL
total_calibration_result = 0

# PARCOURS DE CHAQUE ÉQUATION
for equation in equations:
    # EXTRACTION DE LA VALEUR CIBLE ET DES NOMBRES
    target, numbers = equation.split(':')
    target = int(target.strip())
    numbers = list(map(int, numbers.strip().split()))
    
    # GÉNÉRATION DE TOUTES LES COMBINAISONS POSSIBLES D'OPÉRATEURS
    num_operators = len(numbers) - 1
    operator_combinations = product('+*', repeat=num_operators)
    
    # TEST DE CHAQUE COMBINAISON D'OPÉRATEURS
    valid = False
    for operators in operator_combinations:
        if evaluate_left_to_right(numbers, operators) == target:
            valid = True
            listTest.append([target,numbers, operators])
            break
    
    # SI L'ÉQUATION EST VALIDE, AJOUTER LA VALEUR CIBLE AU RÉSULTAT TOTAL
    if valid:
        total_calibration_result += target

# AFFICHAGE DU RÉSULTAT TOTAL
print(total_calibration_result)  # --> 6231007345478