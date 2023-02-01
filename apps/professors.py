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
#from apps.db_manager import df, ENGINE, Session, session

fig = px.bar(df, x= "Semester")
fig.update_layout(
    yaxis_title="Number of Students",
    title='Total Number of Supervisions per Semester',
    title_x=0.5
    )

layout = html.Div([
    html.Br(),
    html.Header(
        html.H1('Thesis Supervision Hours')
        ),
    html.Br(),
    html.H4('Please select a semeseter and a professor:', style={'text-align': 'left'}),
    html.Div(id='button-container',
             #style={'width': '90%'},
             children = [
        #html.Label('Select a Semester:'),
        html.Div(dcc.Dropdown(
            id='semester-dropdown', placeholder='Select a Semester', clearable=False,
            persistence=True, persistence_type='session',
            options=[{'label': x, 'value': x} for x in sorted(df.Semester.unique())]
        ), className='six columns', style={'margin':'10px'}),
        #html.Label('Select a Professor:'),
        html.Div(dcc.Dropdown(
            id='professor-dropdown', placeholder='Select a Professor', clearable=False,
            persistence=True, persistence_type='session',
            options=[{'label': x, 'value': x} for x in sorted(df.First_Supervisor.unique())],
            searchable=True
        ), className='six columns', style={'margin':'10px'}),
        
    ], className='row'),
    html.Br(),    
    html.Div(id='output-container',style={'padding':'10px'}),
    html.Br(),
    html.Div(id='cointainer-of-card-containers', children=[
        html.Div(id='card-container',
                 children=[
                     html.Label('Total Main Supervisions for', style={'font-size': '18px'}),
                     html.Div(id='main_count_card', children='',
                              ),
                     ],
                              style={'display': 'inline', 
                                    'float':'left', 
                                    'width': '10%', 
                                    'text-align': 'center', 
                                    'border': '1px solid black', 
                                    'padding': '10px',
                                    'margin': '10px',
                                    'border-radius': '10px',
                                    'background':'#FEEECD'}
                ),
        html.Div(id='card-container-2',
                 children=[
                     html.Label('Total Secondary Supervisions for', style={'font-size': '18px'}),
                     html.Div(id='ancillary_count_card', children='',
                              ),
                     
                     ],
                              style={'display': 'inline', 
                                    'float':'left', 
                                    'width': '10%',
                                    #'width' : '',
                                    'text-align': 'center', 
                                    'border': '1px solid black', 
                                    'padding': '10px',
                                    'margin': '10px',
                                    'border-radius': '10px',
                                    'background':'#F6F9ED'}
                 ),
        #html.Br(),
        html.Div([
            dcc.Graph(id='my-bar', figure=fig)
            ], 
            style={'width':'75%',
                      #'text-align':'center'
                      #'float':'right'
                      }
                      ),
        
        ], 
        style={
            "display": "flex",
            #"justify-content": "space-between",
            "align-items": "center",
            "padding": "10px",
            #"border": "1px solid black",
            #'border-radius': '10px'
            }
        ),
    
], style={'width':'75%', 'margin':'0 auto', 'text-align': 'center'})



@app.callback(Output('output-container', 'children'),
     [Input(component_id='semester-dropdown', component_property='value'),
      Input(component_id='professor-dropdown', component_property='value')])
def display_results(semester_chosen, professor_chosen):
    df_fltrd = df[df['Semester'] == semester_chosen]
    df_fltrd = df_fltrd[(df_fltrd['First_Supervisor'].isin([professor_chosen])) | 
                     (df_fltrd['Second_Supervisor'].isin([professor_chosen]))]
    return html.Table(style={'margin':'auto','textAlign':'center','padding':'10px'}, children=[
        # Header
        #html.Tr([html.Th(col,style={'padding':'10px'}) for col in df_fltrd.columns]),
        html.Tr([html.Th(col,style={'padding':'10px'}) for col in ['First Supervisor',
                                                                   'Second Supervisor',
                                                                   'Main Supervisor',
                                                                   'Student',
                                                                   'Gender',
                                                                   'Colloquium Date',
                                                                   'Semester']]),
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
    return html.P(f"{professor_chosen}: {main_count}", style={'font-size': '20px'}), html.P(f"{professor_chosen}: {ancillary_count}", style={'font-size': '20px'})
