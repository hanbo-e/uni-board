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
from datetime import datetime

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
                              #persistence=True,
                              #persistence_type='session'
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
                              #persistence=True,
                              #persistence_type='session'
                              ),
                 ),        # gender
        
        
        html.Label('Colloquium Date'),
        html.Div(dcc.Input(id='colloquium_date_input', placeholder='yyyy-mm-dd',
                           pattern = "\20[0-9][0-9]\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])*",
                           required = True
                              )),         # colloqium date
        html.Br(),
        
        html.Button(children='Submit', id='submit-button', n_clicks=0)
    ]),
    html.Label('Output Box: '),
    html.Div(id='output')
])

@app.callback(Output('output', 'children'), 
              [Input('submit-button', 'n_clicks')],
              [State('first_supervisor_input', 'value'), 
               State('second_supervisor_input', 'value'), 
               State('main_supervisor_dropdown', 'value'),
               State('student_name_input', 'value'),
               State('gender_dropdown', 'value'),
               State('colloquium_date_input', 'value')
               ],
              prevent_initial_call=True
              )
def update_output_data(n_clicks,
                       first_supervisor_value, 
                       second_supervisor_value,
                       main_value,
                       name_value,
                       gender_value,
                       colloquium_value):
    date = datetime.strptime(colloquium_value, '%Y-%m-%d')
    semester = ''
    if date.month >= 4 and date.month <= 9:
        semester = f'Summer Semester {date.year}'
    else:
        if date.month > 9 or date.month < 4:
            if date.month < 4:
                semester = f'Winter Semester {date.year-1}'
            else:
                semester = f'Winter Semester {date.year}'
    return f"""First: {first_supervisor_value},
Second: {second_supervisor_value}, 
Main: {main_value},
Name: {name_value},
Gender: {gender_value}, 
Colloquium: {colloquium_value}
Semester: {semester}"""

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