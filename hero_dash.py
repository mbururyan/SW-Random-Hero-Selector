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

# Navigation Bar that will act as our header

navbar = dbc.NavbarSimple(
    children = [
        dbc.NavItem(dbc.NavLink('GitHub', href = 'https://github.com/mbururyan')),
    ],

    brand = 'STAR WARS',
    color = 'Primary',
    dark = True

)

navbar2 = html.Nav(
    className = 'nav',
    children = [
        html.A('STAR WARS')
    ],
)




app.layout = html.Div(
    children = [
        navbar2
    ]
)



# Call the app
if __name__ == '__main__':
    app.run_server(debug=True, dev_tools_ui=False)