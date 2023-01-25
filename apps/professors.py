# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:34:31 2023

@author: hanbo-e
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

from apps.db_manager import df

layout = html.Div([
    html.H1('Thesis Supervision Hours', style={"textAlign": "center"}),

    html.Div([
        html.Div(dcc.Dropdown(
            id='semester-dropdown', value='Winter Semester 2022', clearable=False, # why is the default value not showing?
            persistence=True, persistence_type='session',
            options=[{'label': x, 'value': x} for x in sorted(df.Semester.unique())]
        ), className='six columns'),

        html.Div(dcc.Dropdown(
            id='professor-dropdown', value='Prof. B. F. Skinner', clearable=False,
            persistence=True, persistence_type='session', #this controls if the last info clicked will stay the same
            options=[{'label': x, 'value': x} for x in sorted(df.First_Supervisor.unique())],
            searchable=True
        ), className='six columns'),
        
    ], className='row'),
    
    html.Div(id='output-container',style={'padding':'10px'}),
    html.Div(id='main_count_card', children='', style={'display': 'inline', 
                                                       'float':'left', 'width': '50%', 'text-align': 'center', 'border': '1px solid black', 'padding': '10px'}),
html.Div(id='ancillary_count_card', children='', style={'display': 'inline', 
                                                        'float':'left', 'width': '50%', 'text-align': 'center', 'border': '1px solid black', 'padding': '10px'}),

])



@app.callback(Output('output-container', 'children'),
     [Input(component_id='semester-dropdown', component_property='value'),
      Input(component_id='professor-dropdown', component_property='value')])
def display_results(semester_chosen, professor_chosen):
    df_fltrd = df[df['Semester'] == semester_chosen]
    df_fltrd = df_fltrd[(df_fltrd['First_Supervisor'].isin([professor_chosen])) | 
                     (df_fltrd['Second_Supervisor'].isin([professor_chosen]))]
    return html.Table(style={'margin':'auto','textAlign':'center','padding':'10px'}, children=[
        # Header
        html.Tr([html.Th(col,style={'padding':'10px'}) for col in df_fltrd.columns]),
        # Body
        *[html.Tr([
            html.Td(df_fltrd.iloc[i][col],style={'padding':'10px'}) for col in df_fltrd.columns
        ]) for i in range(min(len(df_fltrd),5))]
    ])

@app.callback(
    Output('main_count_card', 'children'),
    Output('ancillary_count_card', 'children'),
    [Input(component_id='semester-dropdown', component_property='value'),
      Input(component_id='professor-dropdown', component_property='value')]
)
def display_results_2(semester_chosen, professor_chosen):
    df_fltrd = df[df['Semester'] == semester_chosen]
    df_fltrd = df_fltrd[(df_fltrd['First_Supervisor'].isin([professor_chosen])) | 
                     (df_fltrd['Second_Supervisor'].isin([professor_chosen]))]
    rows_1 = len(df_fltrd[(df_fltrd['First_Supervisor'] == professor_chosen)
                           & (df_fltrd['Main_Status'] == 'First')])
    rows_2 = len(df_fltrd[(df_fltrd['Second_Supervisor'] == professor_chosen)
                           & (df_fltrd['Main_Status'] == 'Second')])
    main_count = rows_1 + rows_2
    ancillary_count = len(df_fltrd) - main_count
    return html.H3('Total Main Supervisions: {}'.format(main_count)), html.H3('Total Ancillary Supervisions: {}'.format(ancillary_count))