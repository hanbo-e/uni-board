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
        html.Label('Student Name'),
        html.Div(dcc.Input(id='student_name_input', placeholder='First Name Last Name'
                              )),        # student
        
        html.Label('Gender'),
        html.Div(dcc.Dropdown(id='gender_dropdown',
                              options=[{'label': 'Male', 'value': 'male'}, 
                                       {'label': 'Female', 'value': 'female'},
                                       {'label': 'Other', 'value': 'other'}],
                              persistence=True,
                              persistence_type='session'
                              ),
                 ),        # gender
        
        
        # colloqium date
        
        html.Button(children='Submit', id='submit-button', n_clicks=0)
    ]),
    html.Label('Output Box: '),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), 
              [Input('submit-button', 'n_clicks')],
              [State('first_supervisor_input', 'value'), 
               State('second_supervisor_input', 'value'), 
               State('main_supervisor_dropdown', 'value')],
              prevent_initial_call=True
              )
def update_output(n_clicks, dropdown1_value, dropdown2_value, input_value):
    return f'Dropdown 1: {dropdown1_value}, Dropdown 2: {dropdown2_value}, Input: {input_value}'
