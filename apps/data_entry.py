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


layout = html.Div(style={'textAlign': 'center'}, children=[
    
    html.H1('Data Entry Page', style={'textAlign': 'center'}),
    
    html.Form(children=[
        html.Div(children=[
            html.Label('First Supervisor'),
            dcc.Input(type='text', id='first-supervisor-input')
        ]),
        html.Div(children=[
            html.Label('Second Supervisor'),
            dcc.Input(type='text', id='second-supervisor-input')
        ]),
        
        # html.Div(children=[
        #     html.Label('Main Status'),
        #     dcc.Input(type='text', id='main-status-input', placeholder='Who is the main supervisor?')
            
        # ]),
        
        html.Div(children=[html.Label('Main'),
            dcc.Dropdown(
            id='main-dropdown', placeholder='Who is the main supervisor?',
            options=[{'label': 'First Supervisor', 'value': 'First'}, {'label': 'Second Supervisor', 'value': 'Second'}],
            #style={'width': '200px', 'display':'flex', 'align-items':'center'}
        )]),             
        
        
        html.Div(children=[
            html.Label('Student Name'),
            dcc.Input(type='text', id='student-name-input')
        ]),
        html.Div(children=[
            html.Label('Student Gender'),
            dcc.Input(type='text', id='student-gender-input')
        ]),
        html.Div(children=[
            html.Label('Colloquium Date'),
            dcc.Input(type='text', id='colloquium-date-input', placeholder = 'yyyy-mm-dd',
                      pattern = '^(20[0-9][0-9])-(0[1-9]|1[012])-(0[1-9]|[12][0-9]|3[01])$')
        ]),
        html.Button('Submit', type='submit', id='submit-button'),
        html.Div(id = 'error-message')
    ])
])

# Create a callback function to check the format of the 'colloquium-date' input
@app.callback(Output('error-message', 'children'),
              [Input('submit-button', 'n_clicks')],
              [State('colloquium-date-input', 'value')])
def validate_colloquium_date(n_clicks, colloquium_date):
    if n_clicks is None:
        raise PreventUpdate
    else:
        try:
            datetime.strptime(colloquium_date, '%Y-%m-%d')
            return ''
        except ValueError:
            return 'Incorrect Format'

# Create a callback function to update the submit button's label and disable the button if there is an error
@app.callback(Output('submit-button', 'disabled'),
              [Input('error-message', 'children')])
def update_submit_button(error_message):
    return True if error_message else False
