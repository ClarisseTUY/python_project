import matplotlib.pyplot as plt
import outils

"""def moyenne_carburants(prix_id,result_info,prix_moyens,carburant1_data, nom_carburant1):
    prix_moyens = []

    if result_info.get('prix_id', '') == 1:"""


def histogramme(prix_moyens):
    # Tableau de moyennes de prix de carburant
    moyenne_carburant = [2.5, 3.0, 2.8, 3.2, 3.5, 2.7, 3.8, 3.1, 2.9, 3.3]

    # Création de l'histogramme
    n, bins, patches = plt.hist(moyenne_carburant, bins=10)

    # Ajout de titres et d'étiquettes aux axes
    plt.title('Histogramme des moyennes de prix de carburant')
    plt.xlabel('Moyenne de prix')
    plt.ylabel('Fréquence')

    # Affichage de l'histogramme
    plt.savefig('histogramme.png')
    plt.show()