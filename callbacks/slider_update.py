from app import app
import dash


@app.callback(
    dash.dependencies.Output('iterations_display', 'children'),
    dash.dependencies.Output('iterations_display', 'style'),
    dash.dependencies.Input('iterations', 'disabled'),
    dash.dependencies.Input('iterations', 'value'),
)
def tab_enable(disabled, value):
    if not disabled:
        return 'Selected Value: ' + str(value), {'margin-top': 20, 'visibility': 'visible'}
    else:
        return '', {'margin-top': 20, 'visibility': 'hidden'}
