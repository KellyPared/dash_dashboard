import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
import dash_bootstrap_components as dbc

from PIL import Image

pil_img1 = Image.open("../assets/overall.png")
pil_img2 = Image.open("../assets/plotted.png")
pil_img3 = Image.open("../assets/spread.png")
pil_img4 = Image.open("../assets/spread2.png")


app4 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True,
    assets_folder="assets"
)


navbar = dbc.NavbarSimple(children=[
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
    dark=True,)

def layout4():
    layout = dbc.Container(
        [
            navbar,
            html.H2("Analyzing On a Yearly Basis", style={"padding": "20px"}),
            html.P(
                "Education demographics is a complex and multifaceted field with various factors...",
                className="custom-text",
            ),
            html.Div(
                children=[
                    html.Div(
                        html.Img(src=pil_img1, className="image-style"),
                        className="image-container"
                    ),
                    html.Div(
                        html.Img(src=pil_img2, className="image-style"),
                        className="image-container"
                    ),
                    html.Div(
                        html.Img(src=pil_img3, className="image-style"),
                        className="image-container"
                    ),
                    html.Div(
                        html.Img(src=pil_img4, className="image-style"),
                        className="image-container"
                    ),
                   
                ],
                className="grid-container"
            ),
        ],
        style={"padding": "20px"},
        fluid=True,
    )
    return layout

app4.layout = layout4

if __name__ == "__main__":
    app4.run_server(port=8054, debug=True)
