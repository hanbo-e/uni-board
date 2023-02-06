import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_core_components as dcc
import dash_html_components as html
from dash.exceptions import PreventUpdate

import pandas as pd
import plotly.express as px

from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import datetime


from apps.db_manager import df, ENGINE, Session, session

from app import app

#df_temp = df.tail(10)
#df_temp['Colloquium_Date'] = pd.to_datetime(df_temp['Colloquium_Date'])
#df_temp['Colloquium_Date'] = df_temp['Colloquium_Date'].dt.strftime('%Y-%m-%d')
#print(df_temp.dtypes)

layout = html.Div(
    [
        html.Br(),
        html.H3("Last ten database entries:", style = {"text-align":"left"}),
        dash_table.DataTable(
            id="table",
            columns=[{"name": i, "id": i} for i in df.columns],
            #data = df_temp.to_dict("rows"),
            data=df.tail(10).to_dict("rows"),
            # style_data_conditional=[
            #     {
            #         'if': {'column_id': 'Colloquium_Date'},
            #         'format': {'value': '{:%Y-%m-%d}'.format}
            #     }
            # ],            
        ),
        html.Br(),
        html.P(
            "Fill in new colloquium information below and click on 'save to database':",
            style={"margin": "10px", "font-size": "18px", "text-align":"left"},
        ),
        html.H2(id="error-message", style={"color": "red", "fontsize": "18px", "text-align":"left"}),
        html.Div(
            id="all-inputs-container",
            children=[
                html.Div(
                    children=[
                        html.Label("First Supervisor"),
                        dcc.Input(
                            id="input-box-1",
                            type="text",
                            value="",
                            placeholder="Title. First Name Last Name",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Second Supervisor"),
                        dcc.Input(
                            id="input-box-2",
                            type="text",
                            value="",
                            placeholder="Title. First Name Last Name",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Main Supervisor"),
                        dcc.Dropdown(
                            id="input-box-3",
                            value="",
                            options=[
                                {"label": "First Supervisor is Main", "value": "First"},
                                {
                                    "label": "Second Supervisor is Main",
                                    "value": "",
                                },
                            ],
                            # style={'width':'14%'}
                        ),
                    ],
                    style={"width": "15%"},
                ),
                html.Div(
                    children=[
                        html.Label("Student Name"),
                        dcc.Input(
                            id="input-box-4",
                            type="text",
                            value="",
                            placeholder="First Name Last Name",
                        ),
                    ]
                ),
                html.Div(
                    children=[
                        html.Label("Gender"),
                        dcc.Dropdown(
                            id="input-box-5",
                            value="",
                            options=[
                                {"label": "Male", "value": "male"},
                                {"label": "Female", "value": "female"},
                                {"label": "Other", "value": "other"},
                            ],
                            # style={'width':'100%'}
                        ),
                    ],
                    style={"width": "11%"},
                ),
                html.Div(
                    children=[
                        html.Label("Colloquium Date"),
                        dcc.DatePickerSingle(
                            id="input-box-6", min_date_allowed="2000-01-01"
                        ),
                    ],
                    style={"width": "14%"},
                ),
            ],
            style={
                "display": "flex",
                "justify-content": "space-around",
                "align-items": "center",
                "padding": "15px",
                "border": "1px solid black",
                "border-radius": "10px",
            },
        ),
        html.Br(),
        html.Button(
            "Save to Database",
            id="add-button",
            style={"width": "20%", "background": "#FEEECD", "margin": "10px", "float":"left"},
        ),
    ]
)


@app.callback(
    [Output("table", "data"), Output("error-message", "children")],
    [Input("add-button", "n_clicks")],
    [
        State("input-box-1", "value"),
        State("input-box-2", "value"),
        State("input-box-3", "value"),
        State("input-box-4", "value"),
        State("input-box-5", "value"),
        State("input-box-6", "date"),
    ],
)
def add_row(n_clicks, value1, value2, value3, value4, value5, value6):
    if n_clicks:
        # print(f"value1 = {value1}")
        if "" in [value1, value2, value3, value4, value5, value6]:
            return [df.tail(10).to_dict("rows"), "All fields need to be filled"]
        else:
            converted_date = datetime.date.fromisoformat(value6)
            semester = ""
            if converted_date.month >= 4 and converted_date.month <= 9:
                semester = f"Summer Semester {converted_date.year}"
            else:
                if converted_date.month > 9 or converted_date.month < 4:
                    if converted_date.month < 4:
                        semester = f"Winter Semester {converted_date.year-1}"
                    else:
                        semester = f"Winter Semester {converted_date.year}"
            print(f"The calculated Semester is: {semester}")
            new_row = [value1, value2, value3, value4, value5, converted_date, semester]
            df.loc[len(df)] = new_row
            stmt = text(
                """
                INSERT INTO mytable (First_Supervisor, Second_Supervisor, Main_Status, Student_Name, Gender, Colloquium_Date, Semester)
                VALUES (:First_Supervisor, :Second_Supervisor, :Main_Status, :Student_Name, :Gender, :Colloquium_Date, :Semester)
                """
            )
            session.execute(
                stmt,
                {
                    "First_Supervisor": value1,
                    "Second_Supervisor": value2,
                    "Main_Status": value3,
                    "Student_Name": value4,
                    "Gender": value5,
                    "Colloquium_Date": converted_date,
                    "Semester": semester,
                },
            )
            session.commit()
            print("went into add row function")
    return df.tail(10).to_dict("rows"), ""
