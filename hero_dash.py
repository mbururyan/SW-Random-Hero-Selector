# Import Dash Libraries
import dash
from dash import html
from dash import dcc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import researchpy as rp

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Some CSS

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "15rem",
    "padding": "2rem 1rem",
    "background-color": '#BFCDD9',
}

CONTENT_STYLE = {
    'margin-left' : '18rem',
    'margin-right' : '2rem',
    'padding' : '2rem 2 rem',
}

# Sidebar Bar that will ask the user whether he/she will use a hero or a villain
sidebar = html.Div(
    [
        html.H3('Choose your Faction : '),

        dbc.Nav(
            [
                dbc.NavLink('LightSide', href = '/', active = 'extact'),
                dbc.NavLink('DarkSide', href = '/page-1', active = 'extact'),
            ],
            pills = True,
            vertical = True
        )
    ], style = SIDEBAR_STYLE,
)

# Website layout

content = html.Div(
    id = 'LightSide',
    children = [],
    style = CONTENT_STYLE
)


app.layout = html.Div(
    [
        dcc.Location(id = 'url'),
        sidebar,
        content
    ]

)

# Callbacks

# Sidebar Callback

@app.callback(
    Output('LightSide', 'children'),
    [
        Input('url', 'pathname')
    ]
)

def page_switcher(pathname):
    if pathname == '/':
        return[
            html.H1('CHOOSE YOUR LS HERO')
        ]
    else:
        return[
            html.H1('CHOOSE YOUR DS VILLAIN')
        ]



# Call the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)