import plotly.express as px
import pandas as pd
import plotly.graph_objs as oGraph
import psycopg2
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output, ctx
from db_queries.connect_to_db import connect_to_db as connect
v_user = 111
conn = connect.connect_to_db()
statment = f""" select air_temperature, valid_time from weather.forecast where location_id = 52230 and approved_time = 'xx'"""
df_x = pd.read_sql_query(statment, con=conn)
app = Dash(__name__)


def select_graph(type):
    if type == 'line':
        fig = px.line(
            df_x,
            x="valid_time",
            y="air_temperature"
        )
    elif type == 'bar':
        fig = px.bar(
            df_x,
            x="valid_time",
            y="air_temperature"
        )

    return fig


def generate_table(df, max_rows=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ])
    ])


app.layout = html.Div([
    html.H4(children='ETL Mini-project'),
    generate_table(df_x),
    dcc.Graph(id="graphPlotly"),
    html.Button(id='btn_line',
                children='Line', n_clicks=0),
    html.Button(id='btn_bar', children='Bar', n_clicks=0)
])

last_triggered_id = 'btn_line'


@app.callback(
    Output(component_id='graphPlotly', component_property='figure'),
    [Input(component_id='btn_line',
           component_property='n_clicks')],
    [Input(component_id='btn_bar',
           component_property='n_clicks')]
)
def graph_update(btn_line, btn_bar):
    global last_triggered_id

    if 'btn_line' == ctx.triggered_id:
        last_triggered_id = ctx.triggered_id
        fig = select_graph('line')
    elif 'btn_bar' == ctx.triggered_id:
        last_triggered_id = ctx.triggered_id
        fig = select_graph('bar')
    else:
        if 'btn_line' == last_triggered_id:
            fig = select_graph('line')
        elif 'btn_bar' == last_triggered_id:
            fig = select_graph('bar')

    fig.update_layout(
        font_family="Arial",
        font_size=20,
        title_font_family="Verdana",
        title_font_size=30,
        font_color="#000000",
        title_font_color="#ACACAC",
        width=800,
        height=600,
        title=f"air_temperature for Falsterbo",
        xaxis_title="time",
        yaxis_title="air_temperature",
    )

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
