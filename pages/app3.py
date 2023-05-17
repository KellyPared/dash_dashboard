import dash
import dash_bootstrap_components as dbc
import pandas as pd
import pathlib
import plotly.express as px
from dash import dcc
from dash import Dash, html, Input, Output, State, callback
from pages import app1, app2, app3
from components.navbar import Navbar

navbar = Navbar()

app = Dash(__name__)
server = app.server

def layout3():
    print("Rendering layout3")
    layout = dbc.Container(
        [
            navbar,
            html.H1("Georgia Rural School", style={"padding": "20px"}),
            # Add components specific to app 1
        ],
        fluid=True
    )
    return layout


navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/app")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Rural School GA", href="/app3"),
                dbc.DropdownMenuItem("Private School FL", href="/app2"),
                dbc.DropdownMenuItem("Kaggle Data", href="/app1"),
            ],
            nav=True,
            in_navbar=True,
            label="Education Stats",
        ),
        dbc.NavItem(dbc.NavLink("About", href="/pages/about")),
    ],
    brand="School Statistics",
    brand_href="/pages/home",    
    style={"margin-bottom": 5},
    color="black",
    dark=True,
)


if __name__ == '__main__':
    app.run_server(debug=True)
