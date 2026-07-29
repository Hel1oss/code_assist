import dash
from dash import html as page, dcc, Input, Output, callback, ctx, State, no_update
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
listed_text = []

app.layout = page.Div([
    page.Header([page.H1('My App', id="head"), dcc.Button("Print", id="print-it")]),
    page.Main([

        page.Div([
        page.Div(
        dcc.RangeSlider(
            marks=None,
            tooltip={"placement": "right", "always_visible": False},
            allow_direct_input=False,
            id="slider",
            vertical=True,
            reverse=True,
            # verticalHeight = 800
            ),
            style={"marginTop":"5px","height": "100%", "width": "40px", "paddingInline":"10px"}
        ),
        page.Div(id="textflow", style={"marginLeft": "2em",
                                       "height": "fit-content",
                                       "overflowY": "hidden",
                                       "overflowX": "auto"
                                       }),
        dcc.Store(id="slider_vector")


        ], style= {"border":"2px solid red", 
                   "display":"flex", 
                   "flexDirection": "row",
                   "height":"80vh",
                   "width":"60vw", 
                   "overflowY": "auto",
                   "whiteSpace": "nowrap", 
                    }
        )
        ], style={"height":"100vh"}
    )
],
    className="main-bg"
)
@callback(Output('textflow', 'children'),
          Output("slider", "max"),
          Output("slider", "value"),
          Output("slider", "verticalHeight"),
          Output("slider_vector", "data"),
          Input('slider', 'value'))
def update(value):
    from main_backend import text_deployer
    data = text_deployer()
    vertical_height = (20.7 * len(data))
    
    def text_display(data: list, css_class: str):
        return page.Div(
                [page.P(f"{n}. {text}") for n, text in data],
                className=css_class
            )

    if not value:
        children = [page.P(f"{n}. {text}") for n, text in enumerate(data)]
        return children, (len(data) - 1), [0, (len(data)-1)], vertical_height, [0, (len(data)-1)]
    
    else:
        start = value[0]
        end = value[1]

        inactive_start = enumerate(data[:start])
        active = enumerate(data[start:end+1], start=start)
        inactive_end = enumerate(data[end+1:], start=end+1)

        children = [
            text_display(inactive_start, "inactive"),
            text_display(active, "active"),
            text_display(inactive_end, "inactive")
        ]
        return children, (len(data) - 1), [start, end], vertical_height, [start, end]
    

@callback(Output('head', 'children'),
          Input('print-it', "n_clicks"),
          State("slider_vector", "data"))
def printing(clicks, states):
    print(states)
    from main_backend import text_deployer
    if ctx.triggered_id == "print-it":
        start, end = states
        data = text_deployer()
        # print(states)
        print("\n".join(data[start: end+1]))
        return "Success"
    return no_update

if __name__ == '__main__':
    app.run(debug=True)
