from app import app
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
import json
import numpy as np
import pandas as pd
import dash
import callbacks.read_file
from networkx.readwrite import json_graph


@app.callback(
    dash.dependencies.Output('network_1', 'figure'),
    dash.dependencies.Output('iterations', 'disabled'),
    dash.dependencies.Output('iterations', 'max'),
    dash.dependencies.Output('iterations', 'marks'),
    dash.dependencies.Input('season', 'value'),
    dash.dependencies.Input('linkage', 'value'),
    dash.dependencies.Input('colorenc', 'value'),
    dash.dependencies.Input('iterations', 'value'),
    dash.dependencies.Input('layout', 'value'),
    dash.dependencies.Input('show', 'value'),
)
def plot_network_1(season, linkage, colorenc, iterations, layout, show):
    if season and linkage and layout is not None:
        datafile = 'datasets\starwars-episode-' + \
            str(season)+'-'+str(linkage)+'.json'
        data, G = callbacks.read_file.process_file(
            datafile, colorenc, layout, True if show else False, iterations=iterations)

        return go.Figure(data=data,
                         layout=go.Layout(
                             title="Network #1",
                             showlegend=False,
                             hovermode='closest',
                             margin=dict(l=15, r=15, t=30, b=0),
                             xaxis=dict(showgrid=False, zeroline=False,
                                        showticklabels=False),
                             yaxis=dict(showgrid=False, zeroline=False,
                                        showticklabels=False),
                             paper_bgcolor="LightSteelBlue")
                         ), False if colorenc == 'communities' else True, len(G.nodes())-2 if colorenc == 'communities' else 2, {i: str(i) for i in range(1, len(G.nodes())-2, 5)} if colorenc == 'communities' else {}
    else:
        raise dash.exceptions.PreventUpdate
