from app import app
import networkx as nx
import plotly.graph_objects as go
import plotly.express as px
import json
import numpy as np
import pandas as pd


def process_file(filename, colorenc='scenes', layout='kamada', show_labels=False, iterations=2):
    G = read_json_file(filename)

    # Turn Multigraph into Simple undirected graph to match dataset
    G = nx.Graph(G)

    # Position nodes in network

    switch = {
        'kamada': nx.kamada_kawai_layout(G),
        'circular': nx.circular_layout(G),
        'spring': nx.spring_layout(G),
        'spectral': nx.spectral_layout(G)
    }

    positions = switch.get(layout)
    nx.set_node_attributes(G, positions, 'coord')

    # Assign edge coordinates based on node coordinates
    edge_x = []
    edge_y = []
    for edge in G.edges():
        x0, y0 = G.nodes[edge[0]]['coord']
        x1, y1 = G.nodes[edge[1]]['coord']
        temp_x = []
        temp_x.append(x0)
        temp_x.append(x1)
        temp_x.append(None)
        edge_x.append(temp_x)
        temp_y = []
        temp_y.append(y0)
        temp_y.append(y1)
        temp_y.append(None)
        edge_y.append(temp_y)

    # Assign edge thickness
    edge_thick = []
    for u, v, a in G.edges(data=True):
        edge_thick.append(a['value'])

    # Scale edge thickness between 2 and 10
    temp = np.array(edge_thick)
    temp = np.interp(temp, (temp.min(), temp.max()), (2, 10))
    edge_thick = temp.tolist()

    # Create plotly traces for edges within the network
    traces = {}
    for i in range(0, len(edge_x)):
        traces['trace_' + str(i)] = go.Scatter(x=edge_x[i],
                                               y=edge_y[i],
                                               line=dict(
            color='rgba(255,'+str(round(255-(edge_thick[i]*25.5))) + ', 0,' +
            str(edge_thick[i]/10 if show_labels else 1) + ')',
            width=edge_thick[i]),
            hoverinfo='text')
    data = list(traces.values())

    # Store node coordinates for plotting
    node_x = []
    node_y = []
    for node in G.nodes():
        x, y = G.nodes[node]['coord']
        node_x.append(x)
        node_y.append(y)

    # Create plotly trace for nodes within the network
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text' if show_labels else 'markers',
        textposition="bottom center",
        hoverinfo='text',
        hovertext='text',
        marker=dict(
            showscale=True,
            colorscale='YlGnBu',
            reversescale=True,
            color=[],
            size=10,
            colorbar=dict(
                thickness=15,
                title='# of scenes the character appeared in',
                xanchor='left',
                titleside='right'
            ),
            line_width=2))

    result_centrality = nx.betweenness_centrality(G, weight='value')
    result_degree_centrality = nx.degree_centrality(G)
    comp = nx.algorithms.community.girvan_newman(G)

    if colorenc == 'betweenness':
        node_trace.marker.colorbar.title.text = 'betweenness centrality value'
        for result in result_centrality:
            G.nodes[result]['value'] = result_centrality[result]
    elif colorenc == 'degree':
        node_trace.marker.colorbar.title.text = 'degree centrality value'
        for result in result_degree_centrality:
            G.nodes[result]['value'] = result_degree_centrality[result]
    elif colorenc == 'communities':
        node_trace.marker.showscale = False
        node_trace.marker.colorscale = None
        for i in range(1, iterations-1):
            result_community = tuple(sorted(c) for c in next(comp))
        result_community = tuple(sorted(c) for c in next(comp))
        for result in result_community:
            for id in result:
                G.nodes[id]['value'] = i
            i += 1

    # Assign names and color to nodes within the network
    node_names = []
    node_color = []
    node_text = []
    for node in G.nodes():
        name = G.nodes[node]['name']
        color = G.nodes[node]['value']
        node_names.append(name)
        node_color.append(color)
        text = str(name) + '    ' + str(color)
        node_text.append(text)
    node_trace.text = node_names
    node_trace.marker.color = node_color
    node_trace.hovertext = node_text
    data.append(node_trace)

    return data, G


# Method to read json file and return networkX graph
def read_json_file(filename):
    with open(filename) as f:
        js_graph = json.load(f)
    return nx.readwrite.json_graph.node_link_graph(js_graph)
