import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output
import app1, app2, app4
from flask import Flask, url_for


'''This is the app for the Rural School in Georgia.'''

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
GA_CSV_PATH = DATA_PATH.joinpath("ga_data_overall_success.csv")

GAdemographics_df = pd.read_csv(GA_CSV_PATH)


app3 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True,
    assets_folder=str(DATA_PATH.joinpath("../assets").resolve()))

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.NavbarBrand("School Statistics", href="/pages/home"),
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/app"),
                    dbc.DropdownMenu(
                        [
                            dbc.DropdownMenuItem("Education Stats", header=True),
                            dbc.DropdownMenuItem("Rural School GA", href="http://127.0.0.1:8053/"),
                            dbc.DropdownMenuItem("Private School FL", href="http://127.0.0.1:8052/"),
                            dbc.DropdownMenuItem("Kaggle Data", href="http://127.0.0.1:8051/"),
                            dbc.DropdownMenuItem("Primitive Data Analysis", href="http://127.0.0.1:8054/"),
                        ],
                        in_navbar=True,
                        label="Education Stats",
                        color="secondary",
                    ),
                    dbc.NavLink("About", href="/pages/about"),
                ],
                className="ml-auto",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
)


def layout3():
    layout = html.Div([
        navbar,
        dbc.Container([
            html.Div([
                html.H1("Georgia Rural School", style={"padding": "10px"}),
                html.P(
                    '''The Georgia Milestones data uses the following features: ...''',
                    style={"padding": "10px"}),
                html.H3("Neural Network Model", style={"padding": "10px"}),
            ]),

            dbc.Row([
                dbc.Col([
                    html.Img(src='../assets/neural.png', alt="Neural Network Model",
                             style={'width': '90%', 'height': '60%'}),
                    html.P(
                        '''We created a neural network model with two layers as shown on the left.\n
                        The Georgia Milestones data uses the following features: gender, ethnicity, English-language learners (ELL),
                        students with disabilities (SWD), economic disadvantage (ED), student support team (ST), gifted, absences,
                        Lexile level, and previous year’s scores.''',
                        style={"padding": "10px"}),
                ],
                    width=6
                ),
                dbc.Col([
                    html.P(''),
                    html.P(''),
                    html.H3("Accuracy Results and Feature Ranking for Georgia Milestones"),
                    html.P(''),
                    html.Div([
                        html.Table([
                            html.Thead(
                                html.Tr([html.Th("Test"), html.Th("Accuracy")])
                            ),
                            html.Tbody([
                                html.Tr([html.Td("English Language Arts (ELA)"), html.Td("0.867")]),
                                html.Tr([html.Td("Math (MATH)"), html.Td("0.933")]),
                                html.Tr([html.Td("Science (SCIE)"), html.Td("0.667")]),
                                html.Tr([html.Td("Social Studies (SOCI)"), html.Td("0.900")]),
                                html.Tr([html.Td("Overall (Passing all four tests)"), html.Td("0.833")])
                            ]),
                        ],
                            style={"margin": "10px"},
                        )
                    ],
                        className="col-md-5"
                    ),
                ],
                    width=6
                ),
            ]),

            html.Div([
                dbc.Row([
                    dbc.Col(
                        html.Img(src='../assets/ga_features.png', alt="GA Features",
                                 style={'width': '100%', 'height': '80%'}),
                        width=6),
                    dbc.Col(
                        html.A(
                            html.Img(src='../assets/ga_tableau.png', alt="Georgia Tableau",
                                     style={'width': '100%', 'height': '80%', 'padding-left': '70px'}),
                            href="https://public.tableau.com/app/profile/sahmirah.muhammad/viz/RuralGAPublicSchoolData/Story1",
                            target="_blank"),
                        width=6),
                ]),
                style={"padding": "10px"}
            ),

            dbc.Row([
                dbc.Col(width=6),
                dbc.Col(
                    dcc.Graph(id="scatter_plot_data2"),
                ),
            ]),
        ]),
    ])
    return layout



@app3.callback(
    Output("scatter_plot_data2", "figure"),
    Input("student-dropdown2", "value"),)

def update_student_data3(ethnicity):
    scatter_data3 = px.scatter(
        GAdemographics_df,
        x="MATH 21 Scale Score",
        y="ELA 21 Scale Score",
        color="Gender",
        template="plotly_dark",
        labels={"Gender": "Gender"},
        hover_data=GAdemographics_df.columns,
        title="Math versus Reading per Gender",
    )

    return scatter_data3

app3.layout = layout3

if __name__ == '__main__':
    app3.run_server(port=8053, debug=True)
