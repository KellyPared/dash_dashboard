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

#Gender,Ethnicity,ELL,SWD,ED,SST,Gifted,Absences,Lexile,MATH 21 Scale Score,ELA 21 Scale Score,ELA 22 Pass,MATH 22 Pass,SCIE 22 Pass,SOCI 22 Pass,Subjects Passed,Overall Pass

def update_student_data3(student_id):
    filtered_df = GAdemographics_df[GAdemographics_df["StudentID"] == student_id]
    
    scatter_data3 = px.scatter(
        GAdemographics_df,
        x="MATH 21 Scale Score",
        y="ELA 21 Scale Score",
        color="Course_Type",
        template="plotly_dark",
        labels={"Gender": "Gender"},
        hover_data=GAdemographics_df.columns,
        title="Scatter Plot",
    )

    print(filtered_df)
    return scatter_data3





# Define the layout for the app
def layout3():
    layout = dbc.Container(
        [
            navbar,
            html.H1("Georgia Rural School", style={"padding": "20px"}),
            # Add components specific to app 3
            # For example, you can add tables, graphs, or other components to display the data
        ],
        fluid=True
    )
    return layout

# Set the layout for the app
app3.layout = layout3

# Run the app if the script is executed directly
if __name__ == '__main__':
    app3.run_server(port=8053, debug=True)
