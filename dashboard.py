import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import outils

import webbrowser
from threading import Timer

#html_content=open('carte.py', 'r').read(),

def creer_histogramme(prix_carburant, nom_carburant):
    tableaux_carburants = outils.moy_carburants(prix_carburant, nom_carburant)
    df = pd.DataFrame(list(tableaux_carburants.items()), columns=['Fuel Type', 'Price'])
    fig = px.bar(
        df,
        y='Price',
        color='Fuel Type',
        barmode='group',
        labels={'Price': 'Prix (€)', 'Type de carburants': 'Fuel Type'},
        title='Fuel Prices in Different Cities'
    )   
    fig.update_traces(marker=dict(line=dict(width=2)), width=0.5,) 
    return fig

def creer_dashboard(prix_carburant, nom_carburant):# Mise en page de l'application Dash
    fig = creer_histogramme(prix_carburant, nom_carburant)
    app = dash.Dash(__name__)
    app.layout = html.Div(
    style={'backgroundColor': '#000000'},  # Ajout de la couleur de fond
    children=[
        html.H1(
            children='Bonjourrrrrrrrrrrrrrr',
            style={
                'textAlign': 'center',
                'color': '#7FDBFF',
                'fontFamily': 'Arial, sans-serif',
                'fontSize': '36px',
                'fontWeight': 'bold',
                'textShadow': '2px 2px 4px #000000'
            }
        ),
        dcc.Graph(
            id='graph1',
            figure=fig
        ),
        html.Div(
            children='Bar chart displaying fuel prices for different fuel types in various cities.'
        ),
    ]
)   
    app.run_server(debug=True, port=8050,use_reloader=False)

