# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 08:30:28 2023

@author: eevae

Based on code from here: https://github.com/Coding-with-Adam/Dash-by-Plotly/tree/master/Deploy_App_to_Web/Multipage_App
"""
import dash

# meta tags are for responsive layout in mobile apps

app = dash.Dash(__name__, suppress_callback_exceptions=(True),
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
server = app.server
