import dash
#from dash import html
import dash_html_components as html
import dash_bootstrap_components as dbc

stylesheetname='dbc.themes.CERULEAN'
#BS = "https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/superhero/bootstrap.min.css"
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = html.Div([
  html.H1([
    'Poverty And Equity ',
    html.Span('Database', style={'color': 'hotpink'})],
          style={'fontSize': '40px'}),
  html.H2('The World Bank'),
  dbc.Tabs([
    dbc.Tab([
      html.Ul([
        html.Li('Number of Economies: 170'),
        html.Li('Temporal Coverage: 1974 - 2019'),
        html.Li('Update Frequency: Quarterly'),
        html.Li('Last Updated: March 18, 2020'),
        html.Li([
          'Source: ',
          html.A('https://datacalalog.worldbank.org/dataset/poverty-and-equity-database',
                  href='https://datacatalog.worldbank.org/dataset/poverty-and-equity-database')
        ])
      ])

    ], label='Key Facts'),
    dbc.Tab([
      html.Ul([
        html.Br(),
        html.Li('Book title: Interactive Dashboards and Data Apps with Plotly and Dash'),
        html.Li(['GitHub repo: ',
                html.A('https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash',
                href='https://github.com/PacktPublishing/Interactive-Dashboards-and-Data-Apps-with-Plotly-and-Dash')])
      ])

    ], label='Project Info')
  ])
])

if __name__ == '__main__':
  app.run_server(host='127.0.0.1', port='8050', debug=True)
