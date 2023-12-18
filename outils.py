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