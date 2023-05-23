import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output
from flask import Flask, url_for


PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
PC_CSV_PATH = DATA_PATH.joinpath("new_PC_data.csv")
PCdemographics_df = pd.read_csv(PC_CSV_PATH)


app2 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True,
    assets_folder=str(DATA_PATH.joinpath("../assets").resolve())
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/app")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Rural School GA", href="app3"),
                dbc.DropdownMenuItem("Private School FL", href="app2"),
                dbc.DropdownMenuItem("Kaggle Data", href="app1"),
                dbc.DropdownMenuItem("Primitive Data Analysis", href="app4")],

            nav=True,
            in_navbar=True,
            label="Education Stats"
        ),
        dbc.NavItem(dbc.NavLink("About", href="/pages/about")),
    ],
    brand="School Statistics",
    brand_href="/pages/home",
    style={"marginBottom": 5},
    color="black",
    dark=True
)

@app2.callback(
    Output("scatter_plot_data2", "figure"),
    Input("student-dropdown2", "value"),
)
def update_student_data2(student_id):
    filtered_df = PCdemographics_df[PCdemographics_df["StudentID"] == student_id]
    
    # Convert numerical grades to categorical labels
    grade_labels = {
        9: "Grade 9",
        10: "Grade 10",
        11: "Grade 11",
        12: "Grade 12",
        "Unknown": "Unknown"
    }
    filtered_df.loc[:, "Grade"] = filtered_df["Grade"].map(grade_labels)
    
    scatter_data2 = px.scatter(
        filtered_df,
        x="Course_Type",
        y="Section_Grade",
        color="Grade",
        template="plotly_dark",
        labels={"Course_Type": "Course Type"},
        color_discrete_map={
            "Grade 9": "blue",
            "Grade 10": "green",
            "Grade 11": "orange",
            "Grade 12": "rgb(255, 0, 0)",  # Change the color mapping to red
            "Unknown": "gray"
        }
    )

    scatter_data2.update_traces(marker=dict(size=28,color="red"))
    scatter_data2.update_layout(title="Course Grade per Student Data")

    return scatter_data2


@app2.callback(
    Output("scatter_plot_alldata", "figure"),
    Input("student-dropdown2", "value"),
)
def update_all_student(student_id):
    scatter_all_data = px.scatter(
        PCdemographics_df,
        x="Grade",
        y="Section_Grade",
        color="Course_Type",
        template="plotly_dark",
        labels={"Course_Type": "Course Type"},
        color_discrete_map={
            "Grade 9": "blue",
            "Grade 10": "green",
            "Grade 11": "orange",
            "Grade 12": "red",
            "Unknown": "gray"
        },
    )

    scatter_all_data.update_traces(marker=dict(size=18))
    scatter_all_data.update_layout(title="Course Grades per Grade")

    return scatter_all_data

def layout2():
    print("Rendering layout2")
    layout = dbc.Container(
        [
            navbar,
            html.H3("The Problem with Standardizing Students", style={"padding": "10px"}),
            html.P('''Establishing standardized grading systems in independent schools can be a challenge due to the wide range of courses and resources. 
                The course offerings in independent schools make it difficult to find a pattern, identify issues and increases the features.
            '''),
            html.H3("Florida Private School Data", style={"padding": "10px"}),
            html.Img(src='../assets/pc_features.png', alt="My Image", style={'width': '70%', 'height': '50%'}),

            html.P(''),
            dcc.Graph(id="scatter_plot_data2"),  # Add this line to display the graph
            dcc.Dropdown(
                id="student-dropdown2",
                options=[
                    {"label": str(student_id), "value": student_id}
                    for student_id in PCdemographics_df["StudentID"]
                ],
                value=PCdemographics_df["StudentID"].iloc[0],
            ),

            dcc.Graph(id="scatter_plot_alldata")
        ]
    )
    return layout

app2.layout = layout2

if __name__ == '__main__':
    app2.run_server(port=8052, debug=True)
