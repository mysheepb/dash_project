import pandas as pd
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Output, Input

poverty_data = pd.read_csv('data/PovStatsData.csv')

stylesheetname=dbc.themes.LITERA
'''
The full list of available themes is CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, PULSE, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, YETI.
'''
#BS = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[stylesheetname])

app.layout = html.Div([
    dcc.Dropdown(id='year_dropdown',
                 value='2010',
                 options=[{'label': year, 'value': str(year)}
                          for year in range(1974, 2019)]),
    dcc.Graph(id='population_chart'),
])





if __name__ == '__main__':
  app.run_server(host='127.0.0.1', port='8050', debug=True)
