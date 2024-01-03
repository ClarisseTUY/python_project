import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html,Input, Output, State
import outils
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import plotly.graph_objects as go

def creer_histogramme(prix_carburant, nom_carburant):
    """
    Retourne l'histogramme des carburants

    Arguments : 
    prix_carburant : prix des carburants, valeur décimal
    nom_carburant : noms des carburants, chaîne de caractères
    """
    # Appel à une fonction externe pour obtenir des tableaux de prix de carburant
    tableaux_carburants = outils.moy_carburants(prix_carburant, nom_carburant)
    # Création d'un DataFrame à partir des données obtenues avec les colonnes 'Fuel Type' et 'Price'
    df = pd.DataFrame(list(tableaux_carburants.items()), columns=['Fuel Type', 'Price'])
    # Création d'une figure pour le graphique à barres
    fig = go.Figure()
    # Calcul du rang des prix de carburant dans l'ordre décroissant et assignation à une colonne 'Rank' dans le DataFrame
    df['Rank'] = df['Price'].rank(ascending=False)
    # Opacité minimale pour les barres du graphique
    min_opacity = 0.2 
    # Boucle sur chaque type de carburant pour créer une barre dans le graphique
    for i, fuel_type in enumerate(df['Fuel Type']):
        # Calcul du rang du carburant spécifique
        rank = int(df[df['Fuel Type'] == fuel_type]['Rank'].iloc[0])
        max_rank = len(df)
        # Calcul de l'opacité en fonction du rang du carburant
        opacity = min_opacity + (1 - min_opacity) * (1-rank / max_rank)
        # Ajout d'une barre au graphique avec les informations du carburant spécifique
        fig.add_trace(go.Bar(
            x=[fuel_type],
            y=[df['Price'][i]],
            hovertemplate=f'<b>Carburant : {fuel_type}</b><br>Prix moyen : {df["Price"][i].round(2)}€<extra></extra>',
            marker=dict(color=f"rgba(131, 148, 150, {opacity})"),  # Couleur de la barre basée sur l'opacité
            name=fuel_type,  # Nom du carburant pour la légende
        ))

    # Mise à jour de la mise en page du graphique (couleurs, titres, etc.)
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)', # Couleur de fond du graphique transparente
        paper_bgcolor='rgba(0, 0, 0, 0)', # Couleur de fond du papier du graphique transparente
        font=dict(color='#839496'), # Couleur de la police
        title_text='Histogramme de la moyenne des prix des carburants', # Titre du graphique
        title_x=0.5,  # Position horizontale du titre
    )

    return fig  # Renvoie l'histogramme créée

#génère une structure d'onglets
def createTabs(prix_carburant, nom_carburant):
    """
    Retourne la structure d'onglets

    Arguments : 
    prix_carburant : prix des carburants, valeur décimal
    nom_carburant : noms des carburants, chaîne de caractères
    """
    tabs_styles = {
        'height': '44px', # Hauteur des onglets
        'border': 'none', # Aucune bordure pour les onglets
        'background-color': 'rgba(0, 0, 0, 0)', # Couleur de fond transparente pour les onglets
        'color': '#045165', # Couleur du texte des onglets
    }
    # Styles pour les onglets sélectionnés
    tab_selected_style = {
        'background-color': 'rgba(0, 0, 0, 0)', # Couleur de fond transparente pour les onglets 
        'color': '#839496', # Couleur du texte pour les onglets 
        'border-right' :'none', # Aucune bordure à droite pour les onglets 
        'border-left' :'none', # Aucune bordure à gauche pour les onglets 
        'border-top': '3px solid #839496', # Bordure supérieure pour les onglets 
    }
    # Création de l'élément Dcc Tabs avec deux onglets
    tab=dcc.Tabs([
            dcc.Tab(
                label='Carte', # Texte de l'onglet 'Carte'
                children=[html.Iframe(id='map', srcDoc=open('map.html', 'r').read(), width='100%', height='450')], # Contenu de l'onglet 'Carte'
                style=tabs_styles, # Applique les styles définis pour les onglets normaux
                selected_style=tab_selected_style, 
            ),
            dcc.Tab(
                label='Histogramme', # Texte de l'onglet 'Histogramme'
                children=[dcc.Graph(id='graph1', figure=creer_histogramme(prix_carburant, nom_carburant))], #contenu
                style=tabs_styles,
                selected_style=tab_selected_style,
            ),
        ],style = {'width': '40%','float': 'left'}) #taille des onglets
    return tab

# Fonction pour créer un composant offcanvas
def createOffCanvas():
    """
    Retourne le canvas crée
    """
    # Création d'un élément canvas
    offcanvas = dbc.Offcanvas(
        id="offcanvas",
        title="Options", # Titre affiché en haut du canvas
        children=[ # Contenu du canvas
            dbc.Checklist(
                options=[ # Liste des options de la liste de contrôle
                    {"label": "Option 1", "value": 1},
                    {"label": "Option 2", "value": 2},
                    {"label": "Option 3", "value": 3},
                ],
                inline=True, # Aligne les checkboxes horizontalement
                style={'margin': '10px'} # Style pour espacer les éléments dans la liste de contrôle
            ),
        ],
    )
    return offcanvas # Renvoie l'élément canvas créé

def creer_dashboard(prix_carburant, nom_carburant):
    """
    Retourne is_open

    Arguments : 
    prix_carburant : correspond aux prix des carburants, valeur décimal
    nom_carburants : correspond aux noms des carburants, valeur chaine de caractères


    """

    # Création d'une instance Dash
    app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])

    # Création du panneau déroulant et des onglets
    offcanvas=(createOffCanvas())
    tabs=createTabs(prix_carburant,nom_carburant)

    app.layout = html.Div(children=[
        html.Button("Menu", id="open-offcanvas"),
        offcanvas,
        html.H1(
            children='Stations services en France',
            style={'text-align': 'center'},
        ),
        html.Br(),
        tabs,
    ])       
        
    @app.callback(
        Output("offcanvas", "is_open"),
        Input("open-offcanvas", "n_clicks"),
        [State("offcanvas", "is_open")],
    )
    def toggle_offcanvas(n1, is_open):
        if n1:
            return not is_open
        return is_open
    
    # Lancement du serveur Dash
    app.run_server(debug=True, port=8050, use_reloader=False)

