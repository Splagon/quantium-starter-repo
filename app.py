from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('./formatted_data.csv')

fig = px.line(df, x="date", y="sales", color=r"region")

app.layout = html.Div(children=[
    html.Title(children="Soul Foods' Sales"),
    html.H1(children="Soul Foods' Sales"),
    html.Div(children='''
        As prices increased in early January, so did total daily revenue
    '''),

    dcc.Graph(
        id='soul_foods_sales',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)