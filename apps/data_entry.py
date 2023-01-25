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
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

layout = html.Div([
    html.H1('Data Entry Page', style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.H3('First Supervisor'),
            dcc.Input(id='first-supervisor-input', type='text', placeholder='Enter First Supervisor')
        ], className='six columns', style={'text-align': 'center'}),

        html.Div([
            html.H3('Second Supervisor'),
            dcc.Input(id='second-supervisor-input', type='text', placeholder='Enter Second Supervisor')
        ], className='six columns', style={'text-align': 'center'}),
    ], className='row'),

    html.Div([
        html.Div([
            html.H3('Main Status'),
            dcc.Input(id='main-status-input', type='text', placeholder='Enter Main Status')
        ], className='six columns', style={'text-align': 'center'}),

        html.Div([
            html.H3('Student Name'),
            dcc.Input(id='student-name-input', type='text', placeholder='Enter Student Name')
        ], className='six columns', style={'text-align': 'center'}),
    ], className='row'),
    
    html.Div([
        html.Div([
            html.H3('Student Gender'),
            dcc.Input(id='gender-input', type='text', placeholder='Enter Gender')
        ], className='six columns', style={'text-align': 'center'}),
        html.Div([
            html.H3('Colloquium Date'),
            dcc.Input(id='colloquium-date-input', type='text', placeholder='Enter Colloquium Date')
        ], className='six columns', style={'text-align': 'center'}),        
        ], className='row')
    ])
