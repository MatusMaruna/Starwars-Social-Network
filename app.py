import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np
from components.control_panel import ControlPanel


# App Init

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Control Graph Init
controls = ControlPanel().get_controls()

# Network #1 Init

fig_network_1 = go.Figure(layout={"title": "Network #1", "margin": dict(
    l=15, r=15, t=30, b=0), "paper_bgcolor": "LightSteelBlue"})

# Network #2 Init

fig_network_2 = go.Figure(layout={"title": "Network #2", "margin": dict(
    l=15, r=15, t=30, b=0), "paper_bgcolor": "LightSteelBlue"})

# Bar Graph Init
fig_bargraph = go.Figure(layout={"title": "Bar Graph", "margin": dict(
    l=15, r=15, t=30, b=0), "paper_bgcolor": "LightSteelBlue"})


# Layout
app.layout = dbc.Container(
    [
        html.H5("Star Wars Social Graph"),
        html.Hr(),
        dbc.Row([
            dbc.Col(controls, md=2.9),
            dbc.Col([
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id="network_1",
                                          figure=fig_network_1,
                                          clear_on_unhover=True), md=6,  style={"border-radius": "19px", "background-color": "LightSteelBlue", "border": "1px solid grey"}),
                        dbc.Col(dcc.Graph(id="network_2",
                                          figure=fig_network_2,
                                          clear_on_unhover=True), md=6, style={"border-radius": "19px", "background-color": "LightSteelBlue", "border": "1px solid grey"}),
                    ],
                    align="center",
                    style={"margin-bottom": "10px"}
                ),
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id="bargraph",
                                          figure=fig_bargraph), style={"border-radius": "19px", "background-color": "LightSteelBlue", "border": "1px solid grey", "width": "300px"})
                    ],
                    align="center",
                    style={"margin-bottom": "0px"}
                ),


            ]),
        ]),
        html.Div(id='network_1_json', style={'display': 'none'})
    ],
    fluid=True,
)
