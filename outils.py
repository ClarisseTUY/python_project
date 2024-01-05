
def moyenne(tableau):
    """
    Calcule la moyenne d'un tableau de valeurs numériques.

    Arguments :
    tableau : list : Liste des valeurs numériques pour calculer la moyenne.

    Returns :
    float : La moyenne des valeurs du tableau.
    """
    if not tableau:
        return None  # Retourne None si le tableau est vide pour éviter une division par zéro
    somme = sum(tableau)
    moyenne = somme / len(tableau)
    return moyenne

def maximum(tableau):
    """
    Trouve la valeur maximale dans un tableau de nombres.

    Arguments :
    tableau : list : Liste des valeurs numériques.

    Returns :
    int : La valeur maximale dans le tableau.
    """
    tableau_entiers = [int(valeur) if valeur.isdigit() else 0 for valeur in tableau]
    return max(tableau_entiers)

def nom_url(url, limite, debut):
    """
    Génère une URL avec une limite et un point de départ donnés.

    Arguments :
    url : string : URL de base.
    limite : int : Limite pour la requête.
    debut : int : Point de départ pour la requête.

    Returns :
    string : URL complète avec les paramètres fournis.
    """
    return f"{url}limit={limite}&start={debut}"

def tab_carburants(prix_carburant, nom_carburant):
    """
    Crée un dictionnaire de tableaux de prix de carburants associés à leur nom.

    Arguments :
    prix_carburant : list : Liste des prix des carburants.
    nom_carburant : list : Liste des noms des carburants.

    Returns :
    dictionnaire : Dictionnaire avec les noms des carburants comme clés et les tableaux de prix comme valeurs.
    """
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
    """
    Calcule les moyennes des prix des carburants.

    Arguments :
    prix_carburant : list : Liste des prix des carburants.
    nom_carburant : list : Liste des noms des carburants.

    Returns :
    dictionnaire : Dictionnaire des moyennes des prix pour chaque carburant.
    """
    tableaux_carburants=tab_carburants(prix_carburant, nom_carburant)
    moyennes_carburants = {}
    for carburant, tableau in tableaux_carburants.items():
        # Utiliser la fonction moyenne de outils pour calculer la moyenne du tableau
        moyennes_carburants[carburant] = moyenne(tableau)

    return moyennes_carburants