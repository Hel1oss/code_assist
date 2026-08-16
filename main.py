import dash
from dash import html as page, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
app = dash.Dash(__name__)

def navbar_open():
     return [
          page.P("close"),
          dbc.Button('tab', id="open-nav")
     ]

def navbar_close(): 
     return [
          page.P("Op"),
          dbc.Button('tab', id="open-nav")
     ]

app.layout = page.Div([
   
    page.Div(navbar_open(), 
              className="chat-nav",
              id="navbar"
            ),
    page.Div([
        page.Header([page.H1('My App')]),
        page.Main([page.P('test')])
    ], 
    className="chat-main"
)
],
    className="main-bg"
)


@callback(Output('navbar', 'className'),
          Output('navbar', 'children'),
          Input('open-nav', 'n_clicks'))
def update(value, count=[0]):
      count[0] += value if value else 0 
      print(count[0])
      if value and count[0]%2 == 1:
           return "chat-nav-hid", navbar_close()
      else:
           return "chat-nav", navbar_open()

if __name__ == '__main__':
    app.run(debug=True)
