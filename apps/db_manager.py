# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:58:45 2023

@author: hanbo-e
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

# def generate_table(dataframe, max_rows=10):
#     return html.Table(
#         # Header
#         [html.Tr([html.Th(col) for col in dataframe.columns])] +

#         # Body
#         [html.Tr([
#             html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
#         ]) for i in range(min(len(dataframe), max_rows))]
#     )

layout = html.Div([

])