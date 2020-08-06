import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import sampling_numbers, data_distributions, sampling_period

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

LOGO_STYLE = {
    'height': '75%', 'width': '75%'
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.Div([html.Img(src=app.get_asset_url('pangea-hiv-logo.png'), style=LOGO_STYLE)]),
        html.H2("Bioinformatics Dashboard", className="display-5"),
        html.Hr(),
        html.P("Navigation", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", id="home-link"),
                dbc.NavLink("Sampling Numbers", href="/sampling-numbers", id="sampling-numbers-link"),
                dbc.NavLink("Data Distributions", href="/data-distributions", id="data-distributions-link"),
                dbc.NavLink("Sampling Period", href="/sampling-period", id="sampling-period-link"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

logo = html.Div([html.Img(src=app.get_asset_url('pangea-hiv-logo.png'), style={'height': '10%', 'width': '10%'})])

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    sidebar,
    content
])

index_page = html.Div([
    html.H5('Welcome to the PANGEA Bioinformatics Dashboard!'),
    html.Br(),
    html.P('I hope you are having a lovely day :)')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index_page
    elif pathname == "/sampling-numbers":
        return sampling_numbers.layout
    elif pathname == "/data-distributions":
        return data_distributions.layout
    elif pathname == "/sampling-period":
        return sampling_period.layout
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True)
