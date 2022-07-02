from dash import Dash, html, dcc, Input, Output, State, no_update
import dash_bootstrap_components as dbc
import plotly.express as px

import aplicacao.datas_lancamentos as datas_lancamentos
import aplicacao.imports_datasets as imports
import aplicacao.distribuicoes as distribuicoes
import aplicacao.distribuicoes_popularidades as distribuicoes_popularidades
import aplicacao.correlacao as correlacao
import aplicacao.weeks_on_chart as weeks_on_chart
import aplicacao.atributos_popularidade as atributos_popularidade
import aplicacao.radar as radar
import aplicacao.evolucao_generos as evolucao_generos
import aplicacao.popularidade_generos as popularidade_generos

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.layout = dbc.Container(children=[
    dbc.Row([
        html.H1("Visualizações de dados musicais", style={'text-align': 'center'}),
        html.P("A música pode ser definida como uma importante expressão cultural, \
            ela pode refletir a sociedade e seu povo no momento em que foi criada. \
            Um exemplo claro deste fato é em relação ao período da ditadura militar \
            brasileira, instaurada em 1964 e que durou até 1985, onde havia forte \
            censura relacionada a arte. E, para driblar a opressão, os artistas que \
            desejavam, por meio da música, fazer alguma crítica ao atual regime \
            precisavam alterar as letras de modo que estas passassem uma mensagem de forma \
            subliminar para que não fossem classificadas como ativismo político."),
        html.P("Outro fator importante relacionado as músicas é o fator comercial. \
            Atualmente, a indústria musical mundial movimenta bilhões de dólares, portanto \
            criar visualizações que permitam dar uma noção, mesmo que pequena e informal, \
            sobre o que torna uma música popular é algo bem importante, além de ser uma boa \
            curiosidade. Nosso trabalho, portanto, consiste na criação de visualizações de dados musicais \
            provenientes do conjunto de dados MusicOset, que contém dados relacionados a popularidade \
            das músicas, características acústicas e líricas, e metadados, que são informações textuais \
            e numéricas sobre as músicas.")
    ]),
    dbc.Row([
        html.H2("Núvens de palavras", style={'text-align': 'center'}),
        dbc.Col([
            html.H3("Títulos das músicas", style={'text-align': 'center'}),
            html.Img(src=app.get_asset_url("titles.png"), style={"width": "100%"}),
    ]),
        dbc.Col([
            html.H3("Letras das músicas", style={'text-align': 'center'}),
            html.Img(src=app.get_asset_url("lyrics.png"), style={"width": "100%"})
        ]),
        html.P("Com o conhecimento das palavras mais comuns nas músicas, podem ser inferidos\
         quais são os temas mais recorrentes no universo musical. Para esse fim, um bom tipo\
          de visualização é uma núvem de palavras. Sendo assim, apresentamos uma núvem de\
           palavras para títulos e outra para letras de músicas. Em particular, é notória\
            a recorrência de temas relacionados a amor, com a ocorrencia de palavras como\
             'love', 'heart', 'kissing', entre outras, tanto nas letras quanto nos títulos.")
    ]),
    dbc.Row([
        html.H2("Distribuições das características das músicas", style={'text-align': 'center'}),
        html.P("Uma música pode ser caracterizada por vários atributos. No caso do Spotify, os \
            atributos disponíveis e explorados por este trabalho incluem:"),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas1', figure=distribuicoes.charts[0]),
                html.P("Duração das músicas dada em minutos", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas2', figure=distribuicoes.charts[1]),
                html.P("Medida de quão acústica é a música, sendo esta uma \
                    medida inversamente proporcional ao quão eletrônica ela seria", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas3', figure=distribuicoes.charts[2]),
                html.P("O quão dançável é considerada a faixa", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas4', figure=distribuicoes.charts[3]),
                html.P("Atributo relacionado à percepção do quão energética é a música, \
                    geralmente relacionado a alguns tipos de ritmo considerados mais animados", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas5', figure=distribuicoes.charts[4]),
                html.P("O quão instrumental é a faixa (em \
                    detrimento da presença de mais vocais, por exemplo)", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas6', figure=distribuicoes.charts[5]),
                html.P("Quantifica a sensação passada por uma performance ao vivo", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas7', figure=distribuicoes.charts[6]),
                html.P("Quantifica a percepção subjetiva de quão \
                    barulhenta é a música, inversamente proporcional à percepção de silêncio, \
                    medida em decibéis (dB)", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas8', figure=distribuicoes.charts[7]),
                html.P("Quanto de fala (trechos não cantados) a música contém", style={'text-align': 'center'})
            ])
        ]),
        dbc.Row([
            dbc.Col([
                dcc.Graph(id='caracteristicas9', figure=distribuicoes.charts[8]),
                html.P("Descreve o quão positiva é considerada a faixa", style={'text-align': 'center'})
            ]),
            dbc.Col([
                dcc.Graph(id='caracteristicas10', figure=distribuicoes.charts[9]),
                html.P("Dado em batidas por minuto, relacionado à velocidade rítmica da música", style={'text-align': 'center'})
            ])
        ]),
        html.P("A análise das distribuições desses atributos permite uma série de inferências a respeito \
            das propriedades musicais mais comuns. Alguns atributos tendem a ser bem concentrados em \
            valores comuns. Isso pode ser observado nos atributos 'speechiness' e 'duration_m', por exemplo, \
            de forma que existem poucas músicas de duração superior a 5 minutos e poucas músicas com um \
            grau de speechiness muito elevado. Por outro lado, alguns atributos possuem faixas mais \
            balanceadas entre as músicas, como é o caso de 'valence', por exemplo. Além disso, no caso \
            geral, boa parte dos atributos aparentam se caracterizar por uma distribuição normal.")
    ]),
    dbc.Row([
        html.H2("Distribuição dos álbuns, artistas e músicas populares versus o total", style={'text-align': 'center'}),

        dbc.Row([
            html.H3("Álbuns", style={'text-align': 'center'}),
            dcc.Graph(id='albumsPopularidade', figure=distribuicoes_popularidades.charts[0])
        ]),
        dbc.Row([
            html.H3("Artistas", style={'text-align': 'center'}),
            dcc.Graph(id='artistasPopularidade', figure=distribuicoes_popularidades.charts[1])
        ]),
        dbc.Row([
            html.H3("Músicas", style={'text-align': 'center'}),
            dcc.Graph(id='musicasPopularidade', figure=distribuicoes_popularidades.charts[2])
        ]),
    ]),
    dbc.Row([
        html.H2("Correlações entre atributos musicais", style={'text-align': 'center'}),

        dbc.Row([
                html.H3("Correlações entre atributos relacionados à expressividade das músicas", style={'text-align': 'center'}),
                dcc.Graph(id='correlacao1', figure=correlacao.fig_1),
                html.P("A característica valência mede a positividade da música, a\
                    'danceabilidade' mede o quão dançante uma música é, já a energia representa uma medida perceptiva de intensidade e atividade de uma música.\
                    Todas essas caracterpisticas estão em um intervalo de 0 a 1. A característica tempo é relacionada ao ritmo da música, ela é medida em batidas\
                    por minuto."),
            ]),
            dbc.Row([
                html.H3("Correlações entre atributos relacionados a alguma coisa (arrumar palavra boa)", style={'text-align': 'center'}),
                dcc.Graph(id='correlacao2', figure=correlacao.fig_2),
                html.P("A característica 'instrumentalness' prevê se uma música não contém vocais, a característica 'acousticness' é uma medida de confiança se a música\
                    é acústica e 'speechiness' detecta a presença de palavras faladas em uma música. Todas essas caracterpisticas estão em um intervalo de 0 a 1. \
                    Já a característica 'loudness' é o volume geral de uma faixa em decibéis"),
            ])
    ]),
    dbc.Row([
            html.H2("Distribuições temporais do lançamento das músicas", style={'text-align': 'center'}),
            dcc.Graph(id='datas_lancamentos', figure=datas_lancamentos.fig)
    ]),
    dbc.Row([
            html.H2("Distribuição de semanas que as músicas permanecem na Billboard 100", style={'text-align': 'center'}),
            dcc.Graph(id='weeks_on_chart', figure=weeks_on_chart.weeks_on_chart)
    ]),
    dbc.Row([
            html.H2("Relação entre o número de semanas que a música permaneceu na Billboard 100, sua posição máxima no ranking e sua popularidade", style={'text-align': 'center'}),
            dcc.Graph(id='weeks_on_chart_peak_position', figure=weeks_on_chart.weeks_on_chart_peak_position)
    ]),
    dbc.Row([
            html.H2("Atributos médios por popularidade", style={'text-align': 'center'}),
            dcc.Graph(id='atributos_popularidade', figure=atributos_popularidade.fig)
    ]),
    dbc.Row([
        dcc.Dropdown(id='musics',
            options=imports.df_metadata_songs['song_name'], value = ['thank u, next', 'Sunflower - Spider-Man: Into the Spider-Verse'],
            multi=True
        ),
        dcc.Graph(id='radar', figure=radar.atribute_radar([]))
    ]),
    dbc.Row([
        html.H2("Distribuição de artistas pelo mundo", style={'text-align': 'center'}),

        html.Div(
            children=[
                html.Iframe(
                    src="assets/mapa.html",
                    style={"width": "100%", "min-height": "640px", "background":"url(assets/loading.gif) center center no-repeat"},
                )
            ]
        )
    ]),
    dbc.Row([
        html.H2("Evolução do Gêneros", style={'text-align': 'center'}),
        dbc.Col(evolucao_generos.image_card, width=3), dbc.Col(evolucao_generos.graph_card, width=8)
    ], justify="around"),
    dbc.Row([
        html.H2("Pontuação anual dos gêneros", style={'text-align': 'center'}),
        dcc.Dropdown(id='music_genres',
            options=popularidade_generos.music_genres, value = ['rock'],
            multi=True
        ),
        dcc.Graph(id='genres_scores', figure=popularidade_generos.compare_genres([]))
    ]),
])

@app.callback(
    Output("radar", "figure"),
    Input("musics", "value"),
)
def update_radar(value):
    return radar.atribute_radar(value)

@app.callback(
    Output("popover", "is_open"),
    [Input("popover-bottom-target", "n_clicks")],
    [State("popover", "is_open")],
)
def toggle_popover(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    [Output("line_chart", "figure"),
     Output("the_alert", "children")],
    [Input("genre_chosen", "value")]
)
def update_graph_card(genres):
    if len(genres) == 0:
        return no_update, alert
    else:
        df_filtered = evolucao_generos.df[evolucao_generos.df["genre"].isin(genres)]
        df_filtered = df_filtered.groupby(["ano", "genre"])[['num']].sum().reset_index()
        fig = imports.px.line(df_filtered, x="ano", y="num", color="genre",
                      labels={"ano": "Year", "num": "# Genres"}).update_traces(mode='lines+markers')
        return fig, no_update

def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    Output("genres_scores", "figure"),
    Input("music_genres", "value"),
)
def update_genres_scores(value):
    return popularidade_generos.compare_genres(value)

if __name__ == '__main__':
    app.run_server(debug=True)
