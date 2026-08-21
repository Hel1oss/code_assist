import dash 
from dash import html as page, dcc, Input, Output, State, MATCH, ALL, callback, ctx, callback_context, no_update
import dash_bootstrap_components as dbc
import time
from assets.custom_component import *
app = dash.Dash(__name__)
items_list = ["abv", "Overview", "BooleanSwitch", "ColorPicker", "Gauge bar", "GraduatedBar"]
items = [{"id":id, "label":label} for id, label in enumerate(items_list, start=1)]


messages = []
app.layout = page.Div([
    
    page.Div( page.Div(
            ### Loaded from callback and Live in the custom_component
              className="chat-nav",
              id="navbar")
            ),
    dcc.Store(id='chat-store-u'),
    dcc.Store(id='chat-store-b'),
    dcc.Store(
            id="items-store",
            data=items
        ),
    page.Div([
        custom_button(Images("hamburger.svg"), 
                      "open-nav",
                      styles={'position': "absolute",
                            "top": "10px",
                            "left": "10px",
                            "zIndex": 1000
                            }
                      ), 
        page.Div([
         page.Header([page.H1('My App')], 
                     style={"margin": "auto"}
                     )
          ],
          className="chat-scroll",
          id="chat"
     ),
        page.Div([
          html.Div(id="dummy", style={"display": "none"}),
          dbc.Textarea(id="chat-box", style={"overflow": "hidden", "resize": "none", "height":"24px"}),
          dbc.Button('send', id='send')
        ],
          className="chat-input"
     )
     ], 
    className="chat-main"
)
],
    className="main-bg"
)

@callback(
    Output("chat-box", "style"),
    Input("chat-box", "value"),
)
def resize_textarea(value):
    lines = max(1, len((value or "").split("\n")))

    return {
        "overflow": "auto",
        "resize": "none",
        "height": f"{lines * 24}px",
        "maxHeight": f"{24 * 5}px",
    }

@callback(Output('navbar', 'className'),
          Output('navbar', 'children'),
          Input('open-nav', 'n_clicks'),
          Input("items-store", "data"))
def navbar_side(n_clicks, data):
     n_clicks = n_clicks or 0

     if n_clicks % 2:
        return "chat-nav-hid", navbar_close()

     return "chat-nav", navbar_open(data)

@callback(
    Output({"type": "item", "index": ALL}, "className"),
    Input({"type": "item", "index": ALL}, "n_clicks"),
    State("items-store", "data"),
    prevent_initial_call=True,
)
def select_item(_, data):
    if not ctx.triggered_id:
        return no_update

    item_id = ctx.triggered_id["index"]
    values = next(i['label'] for i in data if i['id'] == item_id)
    return [
        "sidebar-item active"
        if item["id"]["index"] == item_id
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


    item_id = ctx.triggered_id["index"]
    values = next(i['label'] for i in data if i['id'] == item_id)
    print(values)
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


# @callback(
#     Output({"type": "Del", "index": ALL}, "className"),
#     Input({"type": "Del", "index": ALL}, "n_clicks"),
#     prevent_initial_call=True,
# )

####--------------------------------------------------------

lorem = """Lorem Ipsum is simply dummy text of the printing 
and typesetting industry. Lorem Ipsum has been the 
industry's standard dummy text ever since 1966, when designers 

at Letraset and James Mosley, the librarian at St Bride Printing 
Library in London, took a 1914 Cicero translation and scrambled 
it to make dummy text for Letraset's Body Type sheets. 

It has survived not only many decades, but also the leap into 
electronic typesetting, remaining essentially unchanged. 
It was popularised thanks to these sheets and more recently

with desktop publishing software like Aldus PageMaker and 
Microsoft Word including versions of Lorem Ipsum.
"""

# @callback(
#      Output('chat', "children"),
#      Input('chat-store-u', 'data'),
#      Input('chat-store-b', 'data'),
#      prevent_initial_call=True
# )
# def chat_renderer(*args):
#      chat_box = []
#      # print(messages)
#      print("renderer", ctx.triggered_id)
#      if ctx.triggered_id in {'chat-store-u', 'chat-store-b'}:
#           for chat in messages:
#                if chat[0] == "user":
#                     chat_box.append(chat_user(chat[1]))
#                if chat[0] == "bot":
#                     chat_box.append(chat_bot(chat[1]))
#           return chat_box
#      else:
#           return no_update


@callback(
    Output('chat', 'children', allow_duplicate=True),
    Input('chat-store-u', 'data'),
    State('chat', 'children'),
    prevent_initial_call=True
)
def render_user_msg(data, children):
    if ctx.triggered_id == 'chat-store-u' and data:
        return (children or []) + [chat_user(data)]
    return no_update


@callback(
    Output('chat', 'children', allow_duplicate=True),
    Input('chat-store-b', 'data'),
    State('chat', 'children'),
    prevent_initial_call=True
)
def render_bot_msg(data, children):
    if ctx.triggered_id == 'chat-store-b' and data:
        return (children or []) + [chat_bot(data)]
    return no_update

@callback(
     Output('chat-store-u', 'data'),
     Output('chat-box', 'value'),
     Input('send', 'n_clicks'),
     State('chat-box', 'value')
)
def chat_user_receiver(nclick, chat_state):
     if chat_state and ctx.triggered_id == "send":
          messages.append(('user', chat_state))
          return chat_state, ''
     else:
          return no_update, no_update

@callback(
     Output('chat-store-b', 'data'),
     Input('chat-store-u', 'data'),
)
def chat_bot_receiver(data):
     if ctx.triggered_id == "chat-store-u":
          time.sleep(2)
          messages.append(('bot', lorem))
          return lorem
     return no_update



if __name__ == '__main__':
    app.run(debug=True, threaded=True)
