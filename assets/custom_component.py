import dash 
from dash import *
from dash import html as page
import dash_bootstrap_components as dbc
import time

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
            "fontFamily": "monospace",
            "width": f"{(1+len(item['label'])*1.3)}ch",
            "cursor": "text"
        },
    )

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

def Images(image):
    return html.Img(
        src=f"/assets/image/{image}",
        className="svgs"
    )

def custom_button(image:str, 
                  ids_button: str, 
                  styles: dict, 
                  transparent=True,
                  cls:str=None):
    cls = "custom-button" if not cls else f"custom-button {cls}"
    styles = dict(styles or {})

    if transparent:
        styles["background"] = "transparent"

    return dbc.Button(image, 
                    id= ids_button, 
                    style=styles,
                    className=cls,
                    outline=False)
    


#-----------------------------------------------------------------


def navbar_open(items):
     return [
     page.P("close"),
     page.Div(
          [
        page.Div(
            [
                rename_bar(item), 
                custom_button(Images("three-dot-vert.svg"),
                    ids_button={"type": "pop", "index": item["id"]},
                    styles={"margin-left": "auto", "width":"30px", "height":"30px"},
                    ),
                dbc.Popover(
                    dbc.PopoverBody([
                        custom_button(Images("trash.svg"),
                            ids_button={"type": "Del", "index": item["id"]},
                            styles={"width":"40px", "height":"40px"},
                            cls="trash",
                            transparent=False
                            )
                    ]),
                    target={"type": "pop", "index": item["id"]},
                    style={"backgroundColor": "#1e1e1e"},
                    trigger="legacy",
                    hide_arrow=True,
                ),
                ],
                id={"type": "item", "index": item["id"]},
                className="sidebar-item",
                n_clicks=0,
            )
        for item in items
     ]
   )
]

def navbar_close(): 
     return []