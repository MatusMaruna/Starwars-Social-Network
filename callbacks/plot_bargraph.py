from app import app
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
import json
import numpy as np
import array
import pandas as pd
import dash
import callbacks.read_file
from networkx.readwrite import json_graph


@app.callback(
    dash.dependencies.Output('bargraph', 'figure'),
    dash.dependencies.Input('season', 'value'),
    dash.dependencies.Input('linkage', 'value'),
    dash.dependencies.Input('computation', 'value'),
    dash.dependencies.Input('season_2', 'value'),
    dash.dependencies.Input('linkage_2', 'value'),
    dash.dependencies.Input('computation_2', 'value'),
    dash.dependencies.Input('network_1', 'hoverData'),
    dash.dependencies.Input('network_2', 'hoverData'),
)
def plot_bargraph(season, linkage, computation, season_2, linkage_2, computation_2, hoverdata, hoverdata_2):
    if season and linkage is not None:
        if hoverdata is not None:
            if 'text' in hoverdata['points'][0]:
                hoverdata = hoverdata['points'][0]['text']
        elif hoverdata_2 is not None:
            if 'text' in hoverdata_2['points'][0]:
                hoverdata = hoverdata_2['points'][0]['text']
        else:
            hoverdata = ''
        datafile = 'datasets\starwars-episode-' + \
            str(season)+'-'+str(linkage)+'.json'
        data, G = callbacks.read_file.process_file(datafile)
        result_centrality = nx.betweenness_centrality(G, weight='value')
        result_degree_centrality = nx.degree_centrality(G)
        colors = ['blue', ] * len(G.nodes())
        i = 0
        temp = {}
        for node in G.nodes():
            name = G.nodes[node]['name']
            value = G.nodes[node]['value'] if computation is None else result_centrality[
                node] if computation == 'betweenness' else result_degree_centrality[node] if computation == 'degree' else G.nodes[node]['value']
            temp[name] = value
            if name == hoverdata:
                colors[i] = 'red'
            i += 1
        bar_data = pd.DataFrame.from_dict(temp, orient='index')
        bar_data['color'] = colors
        bar_data.reset_index(inplace=True)
        bar_data.columns = ['name', 'value', 'color']
        bar_data = bar_data.sort_values(
            ['value', 'name'], ascending=[False, True])

        if season_2 and linkage_2 is not None:
            datafile_2 = 'datasets\starwars-episode-' + \
                str(season_2)+'-'+str(linkage_2)+'.json'
            data_2, G_2 = callbacks.read_file.process_file(datafile_2)
            result_centrality_2 = nx.betweenness_centrality(
                G_2, weight='value')
            result_degree_centrality_2 = nx.degree_centrality(G_2)
            colors_2 = ['green', ] * len(G_2.nodes())
            i = 0
            temp_2 = {}
            for node in G_2.nodes():
                name = G_2.nodes[node]['name']
                value = G_2.nodes[node]['value'] if computation_2 is None else result_centrality_2[
                    node] if computation_2 == 'betweenness' else result_degree_centrality_2[node] if computation_2 == 'degree' else G_2.nodes[node]['value']
                temp_2[name] = value
                if name == hoverdata:
                    colors_2[i] = 'red'
                i += 1
            bar_data_2 = pd.DataFrame.from_dict(temp_2, orient='index')
            bar_data_2['color'] = colors_2
            bar_data_2.reset_index(inplace=True)
            bar_data_2.columns = ['name', 'value', 'color']
            result = pd.concat([bar_data, bar_data_2])
            result = result.sort_values(
                ['value', 'name'], ascending=[False, True])
            return go.Figure(data=[go.Bar(name='S' + str(season) + ' ' + str(linkage[0:3]) + ' ' + str(computation if len(computation) <= 5 else computation[0:5]), x=bar_data.name, y=bar_data.value, marker_color=bar_data.color), go.Bar(name='S' + str(season_2) + ' ' + str(linkage_2[0:3]) + ' ' + str(computation_2 if len(computation_2) <= 5 else computation_2[0:5]), x=bar_data_2.name, y=bar_data_2.value, marker_color=colors_2)], layout={"title": "Bar Graph", "showlegend": True, "margin": dict(l=15, r=15, t=30, b=0), "paper_bgcolor": "LightSteelBlue", "xaxis": dict(categoryorder='array', categoryarray=result['name'])})
        return go.Figure(data=[go.Bar(name='S' + str(season) + ' ' + str(linkage[0:3]) + ' ' + str(computation if len(computation) <= 5 else computation[0:5]), x=bar_data.name, y=bar_data.value, marker_color=bar_data.color)], layout={"title": "Bar Graph", "showlegend": True, "margin": dict(l=15, r=15, t=30, b=0), "paper_bgcolor": "LightSteelBlue", "barmode": "stack", "xaxis": dict(categoryorder='array', categoryarray=bar_data['name'])})

    else:
        raise dash.exceptions.PreventUpdate
