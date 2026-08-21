import dash
from dash import html as page, dcc, Input, Output, State, ALL, callback, ctx, no_update
import dash_bootstrap_components as dbc


DEFAULT_ITEMS = [
    {"id": 5, "label": "Overview"},
    {"id": 6, "label": "BooleanSwitch"},
    {"id": 7, "label": "ColorPicker"}
]

def rename_bar(item):
    return dcc.Input(
        value=item["label"],
        id={"type": "rename", "index": item["id"]},
        debounce=True,
        style={
            "background": "transparent",
            "border": "none",
            "outline": "none",
            "boxShadow": "none",
            "padding": "0",
            "margin": "0",
            "width": f"{len(item['label'])*1.2}ch",
            "cursor": "text"
        },
    )

def navbar_open(items):
    return page.Div(
        [
            page.Div(
                [
                    rename_bar(item),
                    dbc.Button(
                        "D",
                        id={"type": "Del", "index": item["id"]},
                        color="danger",
                        style={"margin-left": "auto"},
                    ),
                ],
                id={"type": "item", "index": item["id"]},
                className="sidebar-item",
            )
            for item in items
        ]
    )


app = dash.Dash(__name__)

app.layout = page.Div(
    [
        dcc.Store(
            id="items-store",
            data=DEFAULT_ITEMS
        ),

        page.Header(
            [
                page.H1("My App", id="Head")
            ]
        ),

        page.Div(id="navbar"),
    ],
    className="chat-scroll",
)


@callback(
    Output("navbar", "children"),
    Input("items-store", "data"),
)
def render_navbar(items):
    return navbar_open(items)
    

@callback(
    Output("Head", "children"),
    Output({"type": "item", "index": ALL}, "className"),
    Input({"type": "item", "index": ALL}, "n_clicks"),
    State("items-store", "data"),
    prevent_initial_call=True,
)
def select_item(_, data):
    if not ctx.triggered_id:
        return no_update, no_update

    clicked = ctx.triggered_id["index"]
    values = next(i['label'] for i in data if i['id'] == clicked)

    return values, [
        "sidebar-item active"
        if item["id"]["index"] == clicked
        else "sidebar-item"
        for item in ctx.inputs_list[0]
    ]


@callback(
    Output("items-store", "data", allow_duplicate=True),
    Input({"type": "Del", "index": ALL}, "n_clicks"),
    State("items-store", "data"),
    prevent_initial_call=True,
)
def delete_item(clicks, data):
    if not ctx.triggered_id:
        return no_update

    # no button has been clicked
    if not any(c for c in clicks if c):
        return no_update


    clicked = ctx.triggered_id["index"]
    values = next(i['label'] for i in data if i['id'] == clicked)
    print(clicked)
    return [item for item in data if item['label'] != values]


@callback(
    Output("items-store", "data", allow_duplicate=True),
    Input({"type": "rename", "index": ALL}, "value"),
    State("items-store", "data"),
    prevent_initial_call=True,
)
def rename_item(values, items):
    if not ctx.triggered_id:
        return no_update

    item_id = ctx.triggered_id["index"]

    for value, item in zip(values, items):
        if item["id"] == item_id:
            item["label"] = value
            break

    return items

 
if __name__ == "__main__":
    app.run(debug=True)