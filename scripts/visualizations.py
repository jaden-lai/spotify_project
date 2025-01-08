import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from ..data_pipeline import DB_URL

def generate_dashboard(df):
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

    app.layout = html.Div([
        html.H1("Spotify Recent Tracks Analysis"),
        dcc.Graph(
            id='track-analytics',
            figure=px.bar(df, x='artist_name', title="Most Played Artists")
        ),
    ])

    app.run_server(debug=True)

if __name__ == "__main__":
    # Assuming the transformed data is loaded into a DataFrame 'df'
    df = pd.read_sql('recent_tracks', DB_URL)
    generate_dashboard(df)
