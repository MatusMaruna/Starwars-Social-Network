from app import app
import dash


@app.callback(
    dash.dependencies.Output('iterations_display_2', 'children'),
    dash.dependencies.Output('iterations_display_2', 'style'),
    dash.dependencies.Input('iterations_2', 'disabled'),
    dash.dependencies.Input('iterations_2', 'value'),
)
def tab_enable(disabled, value):
    if not disabled:
        return 'Selected Value: ' + str(value), {'margin-top': 20, 'visibility': 'visible'}
    else:
        return '', {'margin-top': 20, 'visibility': 'hidden'}
