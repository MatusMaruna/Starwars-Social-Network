from app import app
import dash 




@app.callback(
    dash.dependencies.Output('tab2', 'disabled'),
    dash.dependencies.Input('season','value'), 
    dash.dependencies.Input('linkage', 'value')
)

def tab_enable(season, linkage): 
    if season and linkage: 
        return False
    else: 
        return True