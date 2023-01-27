# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 11:50:27 2023

@author: eevae
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:34:31 2023

@author: eevae
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd
import pathlib
from app import app

from dash.exceptions import PreventUpdate
import datetime

from apps.db_manager import df

layout = html.Div([
    html.H1('Supervision Data Entry'),
     html.Div([
        html.Label('First Supervisor'),
        html.Div(dcc.Input(id='first_supervisor_input', placeholder='Title First Name Last Name'
                              )),
        html.Label('Second Supervisor'),
        html.Div(dcc.Input(id='second_supervisor_input', placeholder='Title First Name Last Name'
                              )),
        
        html.Label('Main Supervisor'),
        html.Div(dcc.Dropdown(id='main_supervisor_dropdown',
                              options=[{'label': 'First Supervisor is Main', 'value': 'First'}, 
                                       {'label': 'Second Supervisor is Main', 'value': 'Second'}],
                              persistence=True,
                              persistence_type='session'
                              ),
                 ),
        html.Div(children=[html.Label('Main'),
            dcc.Dropdown(
            id='main-status-dropdown', placeholder='Who is the main supervisor?',
            options=[{'label': 'First Supervisor', 'value': 'First'},
                     {'label': 'Second Supervisor', 'value': 'Second'}],
            persistence=True,
            persistence_type='session'
        )]), 
        
        html.Button(children='Submit', id='submit-button', n_clicks=0)
    ]),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), 
              [Input('submit-button', 'n_clicks')], #mutliple inputs, outputs need to be in a list
              [State('dropdown1', 'value'), 
               State('dropdown2', 'value'), 
               State('input', 'value')],
              prevent_initial_call=True #last thing added
              )
def update_output(n_clicks, dropdown1_value, dropdown2_value, input_value):
    return f'Dropdown 1: {dropdown1_value}, Dropdown 2: {dropdown2_value}, Input: {input_value}'

# layout = html.Div(style={'textAlign': 'center'}, children=[
    
#     html.H1('Data Entry Page', style={'textAlign': 'center'}),
    
#     html.Form(children=[
#         html.Div(children=[
#             html.Label('First Supervisor'),
#             dcc.Input(type='text', id='first-supervisor-input')
#         ]),
#         html.Div(children=[
#             html.Label('Second Supervisor'),
#             dcc.Input(type='text', id='second-supervisor-input')
#         ]),
        
#         # html.Div(children=[
#         #     html.Label('Main Status'),
#         #     dcc.Input(type='text', id='main-status-input', placeholder='Who is the main supervisor?')
            
#         # ]),
        
#         html.Div(children=[html.Label('Main'),
#             dcc.Dropdown(
#             id='main-status-dropdown', placeholder='Who is the main supervisor?',
#             options=[{'label': 'First Supervisor', 'value': 'First'}, {'label': 'Second Supervisor', 'value': 'Second'}],
#             persistence=True,
#             persistence_type='session'
#         )]),             
        
        
#         html.Div(children=[
#             html.Label('Student Name'),
#             dcc.Input(type='text', id='student-name-input')
#         ]),
#         html.Div(children=[
#             html.Label('Student Gender'),
#             dcc.Input(type='text', id='student-gender-input')
#         ]),
#         html.Div(children=[
#             html.Label('Colloquium Date'),
#             dcc.Input(type='text', id='colloquium-date-input', placeholder = 'yyyy-mm-dd',
#                       pattern = '^(20[0-9][0-9])-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$')
#         ]),
#         html.Button('Submit', type='submit', id='submit-button', n_clicks=0),
#         #html.Div(id = 'error-message'),
#         html.Div(id = 'output-data-form')
#     ])
# ])

# # Create a callback function to check the format of the 'colloquium-date' input
# @app.callback(Output('output-data-form','children'),
#               [Input('submit-button', 'n_clicks')],
#               [State('first-supervisor-input', 'value'),
#                State('second-supervisor-input', 'value'),
#                State('main-status-dropdown', 'value'),
#                State('student-name-status', 'value'),
#                State('student-gender-input', 'value'),
#                State('colloquium-date-input', 'value')
#                ],
#                prevent_initial_call=True
#               )
# def update_output(n_clicks,
#                   first_supervisor_value,
#                   second_supervisor_value,
#                   main_status_value,
#                   student_name_value,
                  
#                   gender_value,
#                   colloquium_date_value
#                   ):
#     # return None
#     return f"""First is: {first_supervisor_value}, Second is: {second_supervisor_value}
#  etc: {main_status_value}{student_name_value}-{gender_value} - {colloquium_date_value}"""

# @app.callback(Output('output', 'children'), 
#               [Input('submit-button', 'n_clicks')], #mutliple inputs, outputs need to be in a list
#               [State('dropdown1', 'value'), 
#                State('dropdown2', 'value'), 
#                State('input', 'value')],
#               prevent_initial_call=True #last thing added
#               )
# def update_output(n_clicks, dropdown1_value, dropdown2_value, input_value):
#     return f'Dropdown 1: {dropdown1_value}, Dropdown 2: {dropdown2_value}, Input: {input_value}