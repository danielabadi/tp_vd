import imports_datasets as imports

from dash import Dash, html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

df = imports.df_metadata_genres

# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

alert = dbc.Alert("Please choose Genres from dropdown to avoid further disappointment!", color="danger",
                  dismissable=True),  # use dismissable or duration=5000 for alert to close in x milliseconds

image_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Quantity of genres since 1960s", className="card-title"),
                html.H6("Choose Genres:", className="card-text"),
                html.Div(id="the_alert", children=[]),
                dcc.Dropdown(id='genre_chosen', options=[{'label': d, "value": d} for d in df["genre"].unique()],
                             value=["dance pop", "contemporary country", "funk"], multi=True, style={"color": "#000000"}),
                html.Hr()
            ]
        ),
    ],
    color="light",
)

graph_card = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H4("Genres 1960-2018", className="card-title", style={"text-align": "center"}),
                dbc.Button(
                    "About Genres", id="popover-bottom-target", color="info"
                ),
                dbc.Popover(
                    [
                        dbc.PopoverHeader("All About Genres:"),
                        dbc.PopoverBody(
                            "Genres are about the type of each music (Wikipedia)"),
                    ],
                    id="popover",
                    target="popover-bottom-target",  # needs to be the same as dbc.Button id
                    placement="bottom",
                    is_open=False,
                ),
                dcc.Graph(id='line_chart', figure={}),

            ]
        ),
    ],
    color="light",
)

# *********************************************************************************************************
# app.layout = html.Div([
#     dbc.Row([dbc.Col(image_card, width=3), dbc.Col(graph_card, width=8)], justify="around")
# ])

# *********************************************************************************************************

# @app.callback(
#     Output("popover", "is_open"),
#     [Input("popover-bottom-target", "n_clicks")],
#     [State("popover", "is_open")],
# )
# def toggle_popover(n, is_open):
#     if n:
#         return not is_open
#     return is_open

# @app.callback(
#     [Output("line_chart", "figure"),
#      Output("the_alert", "children")],
#     [Input("genre_chosen", "value")]
# )
# def update_graph_card(genres):
#     if len(genres) == 0:
#         return no_update, alert
#     else:
#         df_filtered = df[df["genre"].isin(genres)]
#         df_filtered = df_filtered.groupby(["ano", "genre"])[['num']].sum().reset_index()
#         fig = px.line(df_filtered, x="ano", y="num", color="genre",
#                       labels={"ano": "Year", "num": "# Genres"}).update_traces(mode='lines+markers')
#         return fig, no_update

# def toggle_modal(n1, n2, is_open):
#     if n1 or n2:
#         return not is_open
#     return is_open

# if __name__ == "__main__":
#     app.run_server(debug=True)