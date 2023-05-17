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
except FileNotFoundError:
    print(f"File '{PC_CSV_PATH}' not found.")
    PCdemographics_df = pd.DataFrame()  # Empty DataFrame to handle missing file
except Exception as e:
    print(f"An error occurred while reading the CSV file: {e}")
    PCdemographics_df = pd.DataFrame()  # Empty DataFrame to handle other exceptions

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True
)
app.css.append_css({"external_url": "/static/style.css?v=1.0"})

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

def layout2():
    print("Rendering layout2")
    layout = dbc.Container(
        [
            navbar,
            html.H1("Florida Private School Data", style={"padding": "20px"}),
            html.P(
                """Education demographics is a complex and multifaceted field with various factors such as test scores, financial incomes, gender, race, ethnicity,
                school location, and parental education levels. This area of study has many problems that can make it difficult to obtain accurate and reliable data."""
            ),
            
            html.H3(children="Student Demographics"),
            dcc.Graph(id="scatter_plot_data2"),
            dcc.Dropdown(
                id="student-dropdown2",
                options=[
                    {"label": str(index), "value": index}
                    for index in PCdemographics_df["index"]
                ],
                value=PCdemographics_df["index"].iloc[0],
            ),
        ]
    )
    return layout

# APP STUFF GRAPHS AND CALLBACKS
# _______________________________

@app.callback(
    Output("scatter_plot_data2", "figure"),
    Input("student-dropdown2", "value"),
)
def update_student_data2(student_index):
    scatter_data2 = px.scatter(
        PCdemographics_df,
        x="Grade",
        y="Section_Grade",
        color="Course_Type",
        template="plotly_dark",
        labels={"Course_Type": "Course Type"},
    )
    return scatter_data2

app.layout = layout2

if __name__ == "__main__":
    app.run_server(debug=True)
