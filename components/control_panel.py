import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import os

class ControlPanel: 


    def get_controls(self): 
        controls = dbc.Card(
        [
            dbc.Tabs([
                dbc.Tab(children=[
                    dbc.FormGroup(
                        [
                            dbc.Label("Dataset", style={'font-weight': 'bold'}), 
                            dbc.Card([                        
                                dbc.Label("Season"),
                                dcc.Dropdown(
                                    id="season",
                                    options=[{"label": 'Season ' + str(x), "value": x} for x in range(1,8)] + [{"label": 'All Seasons', "value": 'all'}],
                                    multi=False, 
                                    disabled=False,
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Starwars season'

                                ),
                                dbc.Label("Network linkage", style={'margin-top': '20px'}),
                                dcc.Dropdown(
                                    id="linkage",
                                    options=[{"label": 'Interaction', "value": 'interactions'}, 
                                            {"label": 'Mentions', "value": 'mentions'}],
                                    multi=False, 
                                    disabled=False,
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select network edge linkage'
                                ), 
                            ], body=True),
                            dbc.Label("Display", style={'font-weight': 'bold'}),
                            dbc.Card([  
                                dbc.Label("Node Color Encoding"),
                                dcc.Dropdown(
                                    id="colorenc",
                                    options=[{"label": 'Character Appearances', "value": 'scenes'}, 
                                            {"label": 'Communities', "value": 'communities'}, 
                                            {"label": 'Betweenness Centrality', "value": 'betweenness'}, 
                                            {"label": 'Degree Centrality', "value": 'degree'}],
                                    multi=False, 
                                    disabled=False,
                                    clearable=False,
                                    value='scenes',
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Node Color Encoding'
                                ),
                                dbc.Label("Girivan-Newman Iterations", style={'margin-top': '20px'}),
                                dcc.Slider(
                                    id='iterations',
                                    min=1,
                                    max=2,
                                    step=1,
                                    value=1,
                                    disabled=True,
                                ),
                                html.Div(id='iterations_display', style={'margin-top': 20}),
                                dbc.Label("Barchart Value", style={'margin-top': '20px'}),
                                dcc.Dropdown(
                                    id="computation",
                                    options=[{"label": 'Character Appearances', "value": 'scenes'}, 
                                            {"label": 'Betweenness Centrality', "value": 'betweenness'}, 
                                            {"label": 'Degree Centrality', "value": 'degree'}],
                                    multi=False, 
                                    disabled=False,
                                    clearable=False,
                                    value='scenes',
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Barchart value'
                                ),
                                dbc.Label("Graph Layout", style={'margin-top': '20px'}),
                                dcc.Dropdown(
                                    id="layout",
                                    options=[{"label": 'Kamada Kawai', "value": 'kamada'}, 
                                            {"label": 'Circular', "value": 'circular'}, 
                                            {"label": 'Spring', "value": 'spring'}, 
                                            {"label": 'Spectral', "value": 'spectral'}],
                                    multi=False, 
                                    disabled=False,
                                    clearable=False,
                                    value = 'kamada',
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Graph Layout'
                                ), 
                                dbc.Label("Show Node Labels", style={'margin-top': '20px'}),
                                dcc.Checklist(
                                    id="show",
                                    options=[
                                        {'label': ' Enable ', 'value': 'show'}
                                    ],
                                    value =['show']
                                )
                            ], body=True),
                        ],
                    )
                ], label='Network #1'), 
                dbc.Tab(id='tab2', children=[
                    dbc.FormGroup(
                        [
                            dbc.Label("Dataset", style={'font-weight': 'bold'}), 
                            dbc.Card([                        
                                dbc.Label("Season"),
                                dcc.Dropdown(
                                    id="season_2",
                                    options=[{"label": 'Season ' + str(x), "value": x} for x in range(1,8)] + [{"label": 'All Seasons', "value": 'all'}],
                                    multi=False, 
                                    disabled=False,
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Starwars season'

                                ),
                                dbc.Label("Network linkage", style={'margin-top': '20px'}),
                                dcc.Dropdown(
                                    id="linkage_2",
                                    options=[{"label": 'Interaction', "value": 'interactions'}, 
                                            {"label": 'Mentions', "value": 'mentions'}],
                                    multi=False, 
                                    disabled=False,
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select network edge linkage'
                                ), 
                            ], body=True),
                            dbc.Label("Display", style={'font-weight': 'bold'}),
                            dbc.Card([  
                                dbc.Label("Node Color Encoding"),
                                dcc.Dropdown(
                                    id="colorenc_2",
                                    options=[{"label": 'Character Appearances', "value": 'scenes'}, 
                                            {"label": 'Communities', "value": 'communities'}, 
                                            {"label": 'Betweenness Centrality', "value": 'betweenness'}, 
                                            {"label": 'Degree Centrality', "value": 'degree'}],
                                    multi=False, 
                                    disabled=False,
                                    clearable=False,
                                    value='scenes',
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Node Color Encoding'
                                ),
                                dbc.Label("Girivan-Newman Iterations", style={'margin-top': '20px'}),
                                dcc.Slider(
                                    id='iterations_2',
                                    min=1,
                                    max=2,
                                    step=1,
                                    value=1,
                                    disabled=True,
                                ),
                                html.Div(id='iterations_display_2', style={'margin-top': 20}),
                                dbc.Label("Barchart Value", style={'margin-top': '20px'}),
                                dcc.Dropdown(
                                    id="computation_2",
                                    options=[{"label": 'Character Appearances', "value": 'scenes'}, 
                                            {"label": 'Betweenness Centrality', "value": 'betweenness'}, 
                                            {"label": 'Degree Centrality', "value": 'degree'}],
                                    multi=False, 
                                    disabled=False,
                                    clearable=False,
                                    value='scenes',
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Barchart Value'
                                ),
                            dbc.Label("Graph Layout", style={'margin-top': '20px'}),
                                dcc.Dropdown(
                                    id="layout_2",
                                    options=[{"label": 'Kamada Kawai', "value": 'kamada'}, 
                                            {"label": 'Circular', "value": 'circular'}, 
                                            {"label": 'Spring', "value": 'spring'}, 
                                            {"label": 'Spectral', "value": 'spectral'}],
                                    multi=False, 
                                    disabled=False,
                                    clearable=False,
                                    value = 'kamada',
                                    style={'height': '36px', 'width': '300px'}, 
                                    placeholder='Select Graph Layout'
                                ), 
                            dbc.Label("Show Node Labels", style={'margin-top': '20px'}),
                                dcc.Checklist(
                                    id="show_2",
                                    options=[
                                        {'label': ' Enable ', 'value': 'show'}
                                    ],
                                    value =['show']
                                )    
                            ], body=True),
                        ],
                    )
                ], label='Network #2', disabled=True), 
            ]) 
        ], body=True)
        return controls