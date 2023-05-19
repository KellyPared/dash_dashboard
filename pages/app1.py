import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc, html, Input, Output
from dash.dependencies import State

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../data").resolve()
EXAMS_CSV_PATH = DATA_PATH.joinpath("exams.csv")

demographics_df = pd.read_csv(EXAMS_CSV_PATH)
demographics_df.reset_index(inplace=True)
demographics_df.rename(
    columns={'index': 'student_id', 'race/ethnicity': 'race_ethnicity', 'parental level of education': 'parent_education'},
    inplace=True)

app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True)

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


def layout1():
    layout = dbc.Container(
        [
            navbar,
            html.H2("The Problem with Standardizing Students", style={"padding": "20px"}),
            
            html.P(
                "Education demographics is a complex and multifaceted field with various factors such as test scores, financial incomes, gender, race, ethnicity, "
                "school location, and parental education levels. This area of study has many problems that can make it difficult to obtain accurate and reliable data.",
                className="custom-text",
            ),
            
            html.P("Here are three key problems in education demographics:", className="custom-text"),
            
            dbc.ListGroup(
                [
                    dbc.ListGroupItem(
                        "Lack of standardized data collection methods: Different educational institutions and organizations may use different methods to collect data, leading to inconsistencies and difficulties in comparing and analyzing the information.",
                        className="custom-list-item",
                    ),
                    dbc.ListGroupItem(
                        "Data privacy concerns: Education demographics often involve sensitive information about students and their families. Ensuring data privacy and security while still extracting valuable insights can be challenging.",
                        className="custom-list-item",
                    ),
                    dbc.ListGroupItem(
                        "Limited representation: Some demographic groups may be underrepresented or overlooked in education data, leading to biased analyses and inadequate policy decisions.",
                        className="custom-list-item",
                    ),
                ],
                flush=True,
                className="custom-list",
            ),
            
            html.H2("Kaggle Data", style={"padding": "20px"}),
            
            html.P(
                "This dataset contains information on the performance of high school students in mathematics, including their grades and demographic information. The data was collected from three high schools in the United States.",
                className="custom-text",
            ),
            
            dbc.Table(
                [
                    html.Thead(
                        html.Tr([html.Th("Attribute"), html.Th("Description")])
                    ),
                    html.Tbody(
                        [
                            html.Tr([html.Td("Gender"), html.Td("The gender of the student (male/female)")]),
                            html.Tr([html.Td("Race/ethnicity"), html.Td("The student's racial or ethnic background (Asian, African-American, Hispanic, etc.)")]),
                            html.Tr([html.Td("Parental level of education"), html.Td("The highest level of education attained by the student's parent(s) or guardian(s)")]),
                            html.Tr([html.Td("Lunch"), html.Td("Whether the student receives free or reduced-price lunch (yes/no)")]),
                            html.Tr([html.Td("Test preparation course"), html.Td("Whether the student completed a test preparation course (yes/no)")]),
                            html.Tr([html.Td("Math score"), html.Td("The student's score on a standardized mathematics test")]),
                            html.Tr([html.Td("Reading score"), html.Td("The student's score on a standardized reading test")]),
                            html.Tr([html.Td("Writing score"), html.Td("The student's score on a standardized writing test")]),
                        ],
                        className="custom-table",
                    ),
                ],
                bordered=True,
                responsive=True,
            ),
            
            html.H3(children='Student Demographics'),
            dcc.Graph(id='scatter_plot_data'),
            html.P('Select a student index to view individual Student Demographics.'),
            html.H3(children='Student Information by Student Index'),
            html.Div(id='demographic-table'),       
            dcc.Dropdown(
                id='student-dropdown',
                options=[{'label': student_id, 'value': student_id} for student_id in demographics_df['student_id']],
                value=demographics_df['student_id'].iloc[0],),
            html.H3(children='Student Information Overview by Demographics'),
            dcc.Graph(id='update_score_graph', figure={}),
            
            
        ],
        style={"padding": "20px"},
        fluid=True,
    )
    return layout



@app.callback(
    Output('scatter_plot_data', 'figure'),
    Output('demographic-table', 'children'),
    Output('update_score_graph', 'figure'),
    Input('student-dropdown', 'value'),
    # prevent_initial_call=True  # Disable caching for this callback
)
def update_student_data(student_index):
    print(f"student_index: {student_index}")

    scatter_data = px.scatter(
        demographics_df,
        x='math score',
        y='writing score',
        color='gender',
        template='plotly_dark',
        labels={"race_ethnicity": "Race/Ethnicity"},
    )

    student_row = demographics_df.loc[demographics_df['student_id'] == student_index]
    student_id = student_row['student_id'].iloc[0]
    gender = student_row['gender'].iloc[0]
    race_ethnicity = student_row['race_ethnicity'].iloc[0]
    parent_education = student_row['parent_education'].iloc[0]
    lunch = student_row['lunch'].iloc[0]
    test_prep = student_row['test preparation course'].iloc[0]
    math_score = student_row['math score'].iloc[0]
    reading_score = student_row['reading score'].iloc[0]
    writing_score = student_row['writing score'].iloc[0]

    demographic_table = html.Table(
        [
            html.Tr([html.Td('Student ID:'), html.Td(student_id)]),
            html.Tr([html.Td('Gender:'), html.Td(str(gender))]),
            html.Tr([html.Td('Race/Ethnicity:'), html.Td(str(race_ethnicity))]),
            html.Tr([html.Td('Parental Level of Education:'), html.Td(str(parent_education))]),
            html.Tr([html.Td('Lunch:'), html.Td(str(lunch))]),
            html.Tr([html.Td('Test Preparation Course:'), html.Td(str(test_prep))]),
            html.Tr([html.Td('Math Score:'), html.Td(str(math_score))]),
            html.Tr([html.Td('Reading Score:'), html.Td(str(reading_score))]),
            html.Tr([html.Td('Writing Score:'), html.Td(str(writing_score))]),
        ],
        style={'margin-top': '20px', 'margin-bottom': '20px'},
    )

    subjects = ['Math', 'Reading', 'Writing']
    scores = [math_score, reading_score, writing_score]
    score_df = pd.DataFrame({'Subject': subjects, 'Score': scores})

    score_data = px.bar(
        data_frame=score_df,
        x='Subject',
        y='Score',
        labels={'Score': 'Score'},
        hover_data={'Subject': False, 'Score': ':.2f'},
    )

    score_data.update_traces(hovertemplate='Subject: %{x}<br>Score: %{y}')
    print("scatter_data:", scatter_data)
    print("demographic_table:", demographic_table)
    print("score_data:", score_data)

    return scatter_data, demographic_table, score_data


app.layout = layout1

if __name__ == "__main__":
    app.run_server(port=8051,debug=True)