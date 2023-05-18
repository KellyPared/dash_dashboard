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
# GAdemographics_df.reset_index(inplace=True)

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
            html.P('''The Georgia Milestones data uses the following features: 
            gender, ethnicity, English-language learners (ELL), students with 
            disabilities (SWD), economic disadvantage (ED), student support team (ST), 
            gifted, absences, Lexile level, and previous year’s scores.'''),
            html.P('''The accuracy results for Georgia Milestones are shown below:'''),
            
            dcc.Dropdown(
                id="student-dropdown2",
                options=[{"label": student_id, "value": student_id} for student_id in GAdemographics_df["Overall Pass"]],
                value=GAdemographics_df["Overall Pass"].iloc[0],
            ),
            dcc.Graph(id="scatter_plot_data2"),
        ],
        fluid=True
    )
    return layout

app3.layout = layout3


if __name__ == '__main__':
    app3.run_server(port=8053, debug=True)
