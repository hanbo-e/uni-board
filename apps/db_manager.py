# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:58:45 2023

@author: eevae
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pathlib

from sqlalchemy import create_engine
# from sqlalchemy import inspect

from app import app

PATH = pathlib.Path(__file__).parent #method to use when run as imported module
DATA_PATH = PATH.joinpath("../datasets/mydatabase.db").resolve()

#db_path = 'datasets/mydatabase.db'
#ENGINE = create_engine('sqlite:///datasets/mydatabase.db')

ENGINE = create_engine(f"sqlite:///{DATA_PATH}")

# for checking db connection problems
# connection = ENGINE.connect()
# ENGINE.url
# inspector = inspect(ENGINE)
# print(inspector.get_table_names())

# as this is a small data set I will load the data once into a df instead of querying in callbacks
df = pd.read_sql_table('mytable', ENGINE)

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )

layout = html.Div([
    dcc.Input(
        id='sql-query',
        value='SELECT * FROM dataframe',
        style={'width': '100%'},
        type='text'
    ),
    html.Button('Run Query', id='run-query'),

    html.Hr(),

    html.Div([
        html.Div(id='table-container', className="four columns"),

        html.Div([
            html.Div([
                html.Div([
                    html.Label('Select X'),
                    dcc.Dropdown(
                        id='dropdown-x',
                        clearable=False,
                    )
                ], className="six columns"),
                html.Div([
                    html.Label('Select Y'),
                    dcc.Dropdown(
                        id='dropdown-y',
                        clearable=False,
                    )
                ], className="six columns")
            ], className="row"),
            html.Div(dcc.Graph(id='graph'), className="ten columns")
        ], className="eight columns")
    ], className="row"),

    # hidden store element
    html.Div(id='table-store', style={'display': 'none'})
])


# @app.callback(
#     dash.dependencies.Output('table-store', 'children'),
#     [dash.dependencies.Input('run-query', 'n_clicks')],
#     state=[dash.dependencies.State('sql-query', 'value')])
# def sql(number_of_times_button_has_been_clicked, sql_query):
#     dff = pd.read_sql_query(
#         sql_query,
#         ENGINE
#     )
#     return dff.to_json()


# @app.callback(
#     dash.dependencies.Output('table-container', 'children'),
#     [dash.dependencies.Input('table-store', 'children')])
# def dff_to_table(dff_json):
#     dff = pd.read_json(dff_json)
#     return generate_table(dff)


# @app.callback(
#     dash.dependencies.Output('graph', 'figure'),
#     [dash.dependencies.Input('table-store', 'children'),
#      dash.dependencies.Input('dropdown-x', 'value'),
#      dash.dependencies.Input('dropdown-y', 'value')])
# def dff_to_table(dff_json, dropdown_x, dropdown_y):
#     dff = pd.read_json(dff_json)
#     return {
#         'data': [{
#             'x': dff[dropdown_x],
#             'y': dff[dropdown_y],
#             'type': 'bar'
#         }],
#         'layout': {
#             'margin': {
#                 'l': 20,
#                 'r': 10,
#                 'b': 60,
#                 't': 10
#             }
#         }
#     }


# @app.callback(
#     dash.dependencies.Output('dropdown-x', 'options'),
#     [dash.dependencies.Input('table-store', 'children')])
# def create_options_x(dff_json):
#     dff = pd.read_json(dff_json)
#     return [{'label': i, 'value': i} for i in dff.columns]


# @app.callback(
#     dash.dependencies.Output('dropdown-y', 'options'),
#     [dash.dependencies.Input('table-store', 'children')])
# def create_options_y(dff_json):
#     dff = pd.read_json(dff_json)
#     return [{'label': i, 'value': i} for i in dff.columns]


# app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

# if __name__ == '__main__':
#     app.run_server(debug=True)