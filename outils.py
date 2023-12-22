
def moyenne(tableau):
    if not tableau:
        return None  # Retourne None si le tableau est vide pour éviter une division par zéro
    somme = sum(tableau)
    moyenne = somme / len(tableau)
    return moyenne

def maximum(tableau):
    tableau_entiers = [int(valeur) if valeur.isdigit() else 0 for valeur in tableau]
    return max(tableau_entiers)

def nom_url(url, limite, debut):
    return f"{url}limit={limite}&start={debut}"

def tab_carburants(prix_carburant, nom_carburant):
    tableaux_carburants = {}

    for i in range(len(nom_carburant)):
        carburant = nom_carburant[i]
        prix = prix_carburant[i]
        if carburant == '':
                    continue
        # Vérifier si le carburant a déjà un tableau associé
        if carburant not in tableaux_carburants:
            # S'il n'existe pas, créer un nouveau tableau avec la valeur du prix actuel
            tableaux_carburants[carburant] = [prix]
        else:
            # S'il existe, ajouter la valeur du prix actuel au tableau existant
            tableaux_carburants[carburant].append(prix)
    return tableaux_carburants

def moy_carburants(prix_carburant, nom_carburant):
    tableaux_carburants=tab_carburants(prix_carburant, nom_carburant)
    moyennes_carburants = {}
    for carburant, tableau in tableaux_carburants.items():
        # Utiliser la fonction moyenne de outils pour calculer la moyenne du tableau
        moyennes_carburants[carburant] = moyenne(tableau)

    return moyennes_carburants