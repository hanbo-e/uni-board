# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:30:41 2023

@author: hanbo-e
Based on helpful code and tutorial from here:
https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Deploy_App_to_Web/Multipage_App
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Connect to main app.py file
from app import app
from app import server

# Connect to your app pages
from apps import professors, data_entry, db_manager


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div([
        dcc.Link('Thesis Supervision | ', href='/apps/professors'),
        dcc.Link(' Data Entry Page | ', href='/apps/data_entry'),
        #dcc.Link(' Data Entry Page | ', href='/apps/data_entry2'),
        dcc.Link(' Database Viewer | ', href='/apps/db_manager'),
        #dcc.Link(' Test Ground', href='/apps/test')
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):

    if pathname == '/apps/professors':
        return professors.layout
    if pathname == '/apps/data_entry':
        return data_entry.layout
    if pathname == '/apps/db_manager':
        return db_manager.layout
    # if pathname == '/apps/test':
    #    return test.layout
    else:
        return professors.layout


if __name__ == '__main__':
    #app.run_server(debug=False)
    app.run_server(host='127.0.0.1', port=8000)