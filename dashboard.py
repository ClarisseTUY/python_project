import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html,Input, Output, State
import outils
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template

import plotly.graph_objects as go

def creer_histogramme(prix_carburant, nom_carburant):
    tableaux_carburants = outils.moy_carburants(prix_carburant, nom_carburant)
    df = pd.DataFrame(list(tableaux_carburants.items()), columns=['Fuel Type', 'Price'])

    fig = go.Figure()
    df['Rank'] = df['Price'].rank(ascending=False)
    min_opacity = 0.2 

    for i, fuel_type in enumerate(df['Fuel Type']):
        rank = int(df[df['Fuel Type'] == fuel_type]['Rank'].iloc[0])
        max_rank = len(df)
        opacity = min_opacity + (1 - min_opacity) * (1-rank / max_rank)

        fig.add_trace(go.Bar(
            x=[fuel_type],
            y=[df['Price'][i]],
            hovertemplate=f'<b>Carburant : {fuel_type}</b><br>Prix moyen : {df["Price"][i].round(2)}€<extra></extra>',
            marker=dict(color=f"rgba(131, 148, 150, {opacity})"), 
            name=fuel_type,
        ))

    # Set transparent background
    fig.update_layout(
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        font=dict(color='#839496'),
        title_text='Histogramme de la moyenne des prix des carburants',
        title_x=0.5,
    )

    return fig
def createTabs(prix_carburant, nom_carburant):
    tabs_styles = {
        'height': '44px',
        'border': 'none',
        'background-color': 'rgba(0, 0, 0, 0)',
        'color': '#045165',
    }

    tab_selected_style = {
        'background-color': 'rgba(0, 0, 0, 0)',
        'color': '#839496',
        'border-right' :'none',
        'border-left' :'none',
        'border-top': '3px solid #839496', 
    }
    tab=dcc.Tabs([
            dcc.Tab(
                label='Carte', 
                children=[html.Iframe(id='map', srcDoc=open('map.html', 'r').read(), width='100%', height='450')],
                style=tabs_styles,
                selected_style=tab_selected_style,
            ),
            dcc.Tab(
                label='Histogramme', 
                children=[dcc.Graph(id='graph1', figure=creer_histogramme(prix_carburant, nom_carburant))],
                style=tabs_styles,
                selected_style=tab_selected_style,
            ),
        ],style = {'width': '40%','float': 'left'})
    return tab

def createOffCanvas():
    offcanvas = dbc.Offcanvas(
        id="offcanvas",
        title="Options",
        children=[
            dbc.Checklist(
                options=[
                    {"label": "Option 1", "value": 1},
                    {"label": "Option 2", "value": 2},
                    {"label": "Option 3", "value": 3},
                ],
                inline=True,
                style={'margin': '10px'}
            ),
        ],
    )
    return offcanvas

def creer_dashboard(prix_carburant, nom_carburant):
    app = dash.Dash(external_stylesheets=[dbc.themes.SOLAR])
    offcanvas=(createOffCanvas())
    tabs=createTabs(prix_carburant,nom_carburant)

    app.layout = html.Div(children=[
        html.Button("Menu", id="open-offcanvas"),
        offcanvas,
        html.H1(
            children='Bonjourrrrrrrrrrrrrrr',
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
    
    app.run_server(debug=True, port=8050, use_reloader=False)

