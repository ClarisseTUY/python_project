import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Création de données factices pour les prix du carburant
data = {
    'Fuel Type': ['Gazole', 'Diesel', 'Gasoline', 'Diesel', 'Gasoline'],
    'Price': [2.5, 2.3, 2.6, 2.4, 2.7],
    'City': ['City A', 'City A', 'City B', 'City B', 'City C']
}

# Conversion des données en DataFrame pandas
df = pd.DataFrame(data)

# Initialisation de l'application Dash
app = dash.Dash(__name__)

# Création du graphique
fig = px.bar(
    df,
    x='Fuel Type',
    y='Price',
    color='Fuel Type',
    barmode='group',
    labels={'Price': 'Prix (€)', 'Type de carburants': 'Fuel Type'},
    title='Fuel Prices in Different Cities'
)

# Mise en page de l'application Dash
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


# Exécution de l'application Dash
if __name__ == '__main__':
    app.run_server(debug=True)
