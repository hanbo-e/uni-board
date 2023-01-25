# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 21:29:46 2023

@author: eevae
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import pathlib
from app import app



layout = html.Div([
    html.H1('My Form App'),
#    html.Form([
     html.Div([
        html.Label('Dropdown 1'),
        html.Div(dcc.Dropdown(id='dropdown1', 
                              options=[{'label': 'Option 1', 'value': 1}, {'label': 'Option 2', 'value': 2}] 
                              )),
        html.Label('Dropdown 2'),
        html.Div(dcc.Dropdown(id='dropdown2', 
                              options=[{'label': 'Option A', 'value': 'A'}, {'label': 'Option B', 'value': 'B'}]
                              )),
        html.Label('Input'),
        html.Div(dcc.Input(id='input', type='text', placeholder='Enter Text')),
        html.Button(children='Submit', id='submit-button', n_clicks=0)
    ]),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), 
              [Input('submit-button', 'n_clicks')], 
              [State('dropdown1', 'value'), 
               State('dropdown2', 'value'), 
               State('input', 'value')])
def update_output(n_clicks, dropdown1_value, dropdown2_value, input_value):
    return f'Dropdown 1: {dropdown1_value}, Dropdown 2: {dropdown2_value}, Input: {input_value}'

# import sqlite3

# # Connect to the database (or create it if it doesn't exist)
# conn = sqlite3.connect('mydatabase.db')

# # Create the table
# conn.execute('''CREATE TABLE mytable (input1 text, input2 text, input3 text)''')

# @app.callback(
#     Output('submit-button', 'disabled'),
#     [Input('input1-dropdown', 'value'),
#      Input('input2-dropdown', 'value'),
#      Input('input3-input', 'value')]
# )
# def save_to_db(input1, input2, input3):
#     # Save the input values to the database
#     conn.execute(f"INSERT INTO mytable (input1, input2, input3) VALUES ('{input1}', '{input2}', '{input3}')")
#     conn.commit()
#     return False