import dash 
from dash import html as page, dcc, Input, Output, State, MATCH, ALL, callback, ctx, callback_context, no_update
import dash_bootstrap_components as dbc
import time
app = dash.Dash(__name__)
items = ["Overview", "BooleanSwitch", "ColorPicker", "Gauge", "GraduatedBar"]


def navbar_open(items):
     return [
     page.P("close"),
     page.Div([
     page.Div(
     [
        item, 
        dbc.Button(
               "D",
               id={"type": "Del", "index": item},
               color="danger",
               style={"margin-left": "auto"},
               ),
        ],
        id={"type": "item", "index": item},
        className="sidebar-item",
        n_clicks=0,
    )
    for item in items
     ])
]

def navbar_close(): 
     return [
          page.P("Op"),
          
     ]

messages = []
app.layout = page.Div([
    
    page.Div( page.Div(className="chat-nav",
              id="navbar")
            ),
    dcc.Store(id='chat-store-u'),
    dcc.Store(id='chat-store-b'),
    dcc.Store(
            id="items-store",
            data=items
        ),
    page.Div([
        dbc.Button('tab', id="open-nav", style={
                                                  'position': "absolute",
                                                  "top": "10px",
                                                  "left": "10px",
                                                  "zIndex": 1000,
                                             }), 
        page.Div([
         page.Header([page.H1('My App')], 
                     style={"margin": "auto"}
                     )
          ],
          className="chat-scroll",
          id="chat"
     ),
        page.Div([
          dbc.Input(id="chat-box"),
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
    prevent_initial_call=True,
)
def select_item(_):
    if not ctx.triggered_id:
        return no_update

    clicked = ctx.triggered_id["index"]

    return [
        "sidebar-item active"
        if item["id"]["index"] == clicked
        else "sidebar-item"
        for item in ctx.inputs_list[0]
    ]


@callback(
    Output("items-store", "data"),
    Input({"type": "Del", "index": ALL}, "n_clicks"),
    State("items-store", "data"),
    prevent_initial_call=True,
)
def delete_item(clicks, items):
    if not ctx.triggered_id:
        return no_update

    # no button has been clicked
    if not any(c for c in clicks if c):
        return no_update


    clicked = ctx.triggered_id["index"]
    print(clicked)
    return [item for item in items if item != clicked]

# @callback(
#     Output({"type": "Del", "index": ALL}, "className"),
#     Input({"type": "Del", "index": ALL}, "n_clicks"),
#     prevent_initial_call=True,
# )

####--------------------------------------------------------

def chat_user(text):
     return page.P(text, 
                   style={"margin-left": "auto", 
                         "border":"1px red solid", 
                         "gap":"1em", 
                         "borderRadius":"20px 20px 0px 20px",
                         "padding":"1em",
                         "maxWidth":"60%",
                         "whiteSpace":"pre-wrap"}
                         )
def chat_bot(text):
     return page.Div(text, 
                   style={"margin-right": "auto", 
                         "border":"1px lime solid", 
                         "gap":"1em", 
                         "borderRadius":"20px 20px 20px 0px",
                         "padding":"1em",
                         "maxWidth":"60%",
                         "whiteSpace":"pre-wrap"}
                         )

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
