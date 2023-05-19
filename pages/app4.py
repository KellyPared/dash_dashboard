import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from PIL import Image

pil_img1 = Image.open("assets/overall.png")
pil_img2 = Image.open("assets/plotted.png")
pil_img3 = Image.open("assets/spread.png")
pil_img4 = Image.open("assets/spread2.png")
pil_img5 = Image.open("assets/spread3.png")

app4 = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    title="Evaluation of Education Standards",
    url_base_pathname="/",
    suppress_callback_exceptions=True,
    assets_folder="assets"
)
app4.css.append_css({
    "external_url": "https://your-stylesheet-url.com"
})
navbar = dbc.NavbarSimple()

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
                    html.Div(
                        html.Img(src=pil_img5, className="image-style"),
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
