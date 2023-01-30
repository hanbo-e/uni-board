import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html

import pandas as pd
import plotly.express as px

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import datetime


from apps.db_manager import df, ENGINE, Session, session
#from apps.professors import df, ENGINE, Session, session
from app import app

layout = html.Div([ 
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.tail(10).to_dict("rows"),
        # style_data_conditional=[
        #     {
        #         'if': {'column_id': 'Colloquium_Date'},
        #         'format': lambda x: x.strftime('%Y-%m-%d')
        #     }
        # ]
    ),
    html.Button('Add Row', id='add-button'),
    dcc.Input(id='input-box-1', type='text', value=''),
    dcc.Input(id='input-box-2', type='text', value=''),
    dcc.Input(id='input-box-3', type='text', value=''),
    dcc.Input(id='input-box-4', type='text', value=''),
    dcc.Input(id='input-box-5', type='text', value=''),
    #dcc.Input(id='input-box-6', type='text', value=''),
    dcc.DatePickerSingle(
    id='input-box-6', 
    #date=datetime.datetime(2023, 1, 22), 
    #display_format='YYYY-MM-DD'
),

    dcc.Input(id='input-box-7', type='text', value=''),
])

@app.callback(
    Output('table', 'data'),
    [Input('add-button', 'n_clicks')],
    [State('input-box-1', 'value'),
      State('input-box-2', 'value'),
      State('input-box-3', 'value'),
      State('input-box-4', 'value'),
      State('input-box-5', 'value'),
      State('input-box-6', 'date'),
      State('input-box-7', 'value')]
)
def add_row(n_clicks, value1, value2, value3, value4, value5, value6, value7):
    if n_clicks:
        #converted_date = pd.to_datetime(value6).strftime('%Y-%m-%dT%H:%M:%S')
        converted_date = datetime.date.fromisoformat(value6)
        new_row = [value1, value2, value3, value4, value5, converted_date, value7]
        df.loc[len(df)] = new_row
        stmt = text("""
            INSERT INTO mytable (First_Supervisor, Second_Supervisor, Main_Status, Student_Name, Gender, Colloquium_Date, Semester)
            VALUES (:First_Supervisor, :Second_Supervisor, :Main_Status, :Student_Name, :Gender, :Colloquium_Date, :Semester)
            """)
        session.execute(stmt, {"First_Supervisor": value1, "Second_Supervisor": value2, "Main_Status": value3, 
                                "Student_Name": value4, "Gender": value5, "Colloquium_Date": converted_date, "Semester": value7})
        session.commit()
        print('went into add row function')
    return df.tail(10).to_dict("rows")