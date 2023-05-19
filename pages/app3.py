import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
EXAMS_CSV_PATH = DATA_PATH.joinpath("ga_data_overall_success.csv")

GAdemographics_df = pd.read_csv(EXAMS_CSV_PATH)

app3 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=False
)
app3.css.append_css({"external_url": "/static/style.css?v=1.0"})

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/app")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Rural School GA", href="/app3"),
                dbc.DropdownMenuItem("Private School FL", href="/app2"),
                dbc.DropdownMenuItem("Kaggle Data", href="/app1")],
            nav=True,
            in_navbar=True,
            label="Education Stats",
        ),
        dbc.NavItem(dbc.NavLink("About", href="/pages/about")),
    ],
    brand="School Statistics",
    brand_href="/pages/home",
    style={"marginBottom": 5},
    color="black",
    dark=True,
)

@app3.callback(
    Output("scatter_plot_data2", "figure"),
    Input("student-dropdown2", "value"),
)
def update_student_data3(ethnicity):
    scatter_data3 = px.scatter(
        GAdemographics_df,
        x="MATH 21 Scale Score",
        y="ELA 21 Scale Score",
        color="Gender",
        template="plotly_dark",
        labels={"Gender": "Gender"},
        hover_data=GAdemographics_df.columns,
        title="Scatter Plot",
    )
    return scatter_data3


def layout3():
    layout = dbc.Container(
        [
            navbar,
            html.H2("Georgia Rural School", style={"padding": "20px"}),
            html.P(
                '''The Georgia Milestones data uses the following features: 
                gender, ethnicity, English-language learners (ELL), students with 
                disabilities (SWD), economic disadvantage (ED), student support team (ST), 
                gifted, absences, Lexile level, and previous year’s scores.'''
            ),
            html.P(
                '''
                Acronym Key:<br>
                ELL: English Language Learner<br>
                SWD: Student with Disability<br>
                ED: Economically Disadvantaged<br>
                SST: Student Support Team<br>
                Lexile: measure of reading ability <br>
                Achievement Levels: <br>
                1 - Beginning Learner (failing)<br>
                2 - Developing Learner<br>
                3 - Proficient Learner<br>
                4 - Distinguished Learner
                '''
            ),
            html.H3("Neural Network Model"),
            html.P("We created a neural network model with two layers as shown below:"),
            html.Img(src="static/image.png", alt="Image Description"),

            html.P("The compiling and training is shown below:"),
            html.P(
                '''
                We used the same model for Georgia Milestones data from Union County and a
                data set from Kaggle (<a href="https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics">https://www.kaggle.com/datasets/rkiattisak/student-performance-in-mathematics</a>). 
                The Georgia Milestones data uses the following features: gender, ethnicity, English-language learners (ELL), 
                students with disabilities (SWD), economic disadvantage (ED), student support team (ST), gifted, absences, 
                Lexile level, and previous year’s scores.
                '''
            ),
            html.H3("Accuracy Results for Georgia Milestones"),
            html.Table(
                [
                    html.Thead(
                        html.Tr([html.Th("Test"), html.Th("Accuracy")])
                    ),
                    html.Tbody(
                        [
                            html.Tr([html.Td("English Language Arts (ELA)"), html.Td("0.867")]),
                            html.Tr([html.Td("Math (MATH)"), html.Td("0.933")]),
                            html.Tr([html.Td("Science (SCIE)"), html.Td("0.667")]),
                            html.Tr([html.Td("Social Studies (SOCI)"), html.Td("0.900")]),
                            html.Tr([html.Td("Overall (Passing all four tests)"), html.Td("0.833")]),
                        ]
                    ),
                ],
                style={"margin": "20px"},
            ),
            dcc.Dropdown(
                id="student-dropdown2",
                options=[
                    {"label": student_id, "value": student_id}
                    for student_id in GAdemographics_df["Overall Pass"]
                ],
                value=GAdemographics_df["Overall Pass"].iloc[0],
            ),
            dcc.Graph(id="scatter_plot_data2"),
        ],
        fluid=True,
    )
    return layout

app3.layout = layout3

if __name__ == '__main__':
    app3.run_server(port=8053, debug=True)
