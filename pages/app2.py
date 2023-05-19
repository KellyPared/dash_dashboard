import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
PC_CSV_PATH = DATA_PATH.joinpath("new_PC_data.csv")

try:
    PCdemographics_df = pd.read_csv(PC_CSV_PATH)
    # print(PCdemographics_df.head()) 
except FileNotFoundError:
    # print(f"File '{PC_CSV_PATH}' not found.")
    PCdemographics_df = pd.DataFrame() 
except Exception as e:
    # print(f"An error occurred while reading the CSV file: {e}")
    PCdemographics_df = pd.DataFrame()  

#PCdemographics_df['Grade'] = pd.Categorical(PCdemographics_df['Grade'], ordered=True, categories=["Grade 9", "Grade 10", "Grade 11", "Grade 12"])


app2 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=False
)
app2.css.append_css({"external_url": "/static/style.css?v=1.0"})

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/app")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Rural School GA", href="/app3"),
                dbc.DropdownMenuItem("Private School FL", href="/app2"),
                dbc.DropdownMenuItem("Kaggle Data", href="/app1")
            ],
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
    filtered_df["Grade"] = filtered_df["Grade"].map(grade_labels)
    
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
            "Grade 12": "red",
            "Unknown": "gray"
        }
    )
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
        }
    )
    
    return scatter_all_data




def layout2():
    print("Rendering layout2")
    layout = dbc.Container(
        [
            navbar,
            html.H2("The Problem with Standardizing Students", style={"padding": "20px"}),
            html.P(
                """Education demographics is a complex and multifaceted field with various factors such as test scores, financial incomes, gender, race, ethnicity,
                school location, and parental education levels. This area of study has many problems that can make it difficult to obtain accurate and reliable data."""
            ),
            html.H3("Florida Private School Data", style={"padding": "20px"}),
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
    app2.run_server(port=8052, debug=True) #port=8052
