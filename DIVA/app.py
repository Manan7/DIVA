# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# import pandas as pd

# data = pd.read_csv("Data_API.csv")
# data["Datetime_updated"] = pd.to_datetime(data["Datetime_updated"], format="%Y-%m-%d")
# data.sort_values("Datetime_updated", inplace=True)
# data['Price_USD'].groupby(data['Datetime_updated']).sum()
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import chart_studio.plotly as py
import plotly.graph_objs as go
import plotly.express as px
external_stylesheets =['https://codepen.io/chriddyp/pen/bWLwgP.css', dbc.themes.BOOTSTRAP, 'style.css']
import numpy as np
import pandas as pd 

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server 

df = pd.read_csv('Data_API.csv',nrows=10000000,low_memory=False)

navbar = dbc.Nav()

# country iso with counts
# col_label = "Cateogry"
# col_values = "count"

# v = df[col_label].value_counts()
# new = pd.DataFrame({
#     col_label: v.index,
#     col_values: v.values
# })

# bar1 =  dcc.Graph(id='bar1',
#               figure={
#         'data': [go.Bar(x=new['Restaurant Name'],
#                         y=new['Votes'])],
#         'layout': {'title':dict(
#             text = 'Top Restaurants in India',
#             font = dict(size=20,
#             color = 'white')),
#         "paper_bgcolor":"#111111",
#         "plot_bgcolor":"#111111",
#         'height':600,
#         "line":dict(
#                 color="white",
#                 width=4,
#                 dash="dash",
#             ),
#         'xaxis' : dict(tickfont=dict(
#             color='white'),showgrid=False,title='',color='white'),
#         'yaxis' : dict(tickfont=dict(
#             color='white'),showgrid=False,title='Number of Votes',color='white')
#     }})
col_label0 = "Date"
col_values0 = "count"

v = df["Datetime_updated"].value_counts().sort_index()
new = pd.DataFrame({
    col_label0: v.index,
    col_values0: v.values
})
col_label01 = "USD/Date"
col_values01 = "count"
v2 = df['Price_USD'].groupby(df['Datetime_updated']).sum()
new2 = pd.DataFrame({
    col_label01: v2.index,
    col_values01: v2.values
})
trace_1 = go.Scatter(x = new['Date'], y = new['count'],
                    name = 'Daily Volume of NFTs',
                    line = dict(width = 2,
                                color = 'rgb(229, 151, 50)'))
trace_2 = go.Scatter(x = new2['USD/Date'], y = new2['count'],
                    name = 'Daily Transaction of NFTs',
                    line = dict(width = 2,
                                color = 'rgb(212, 106, 54)'))
layout = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')
fig = go.Figure(data = [trace_1,trace_2], layout = layout)
# groupby country code/city and count rating
col_label = "Collection"
col_values = "count"

v = df[col_label].value_counts().head(10)
new = pd.DataFrame({
    col_label: v.index,
    col_values: v.values
})

bar1 =  dcc.Graph(id='bar1',
              figure={
        'data': [go.Bar(x=new['Collection'],
                        y=new['count'])],
        'layout': {'title':dict(
            text = 'Top Collections based on Count',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':600,
        "line":dict(
                color="white",
                width=4,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Number of Collections',color='white')
    }})


# pie chart - rating

col_label2 = "Category"
col_values2 = "count"

v1 = df[col_label2].value_counts().head(10)
new = pd.DataFrame({
    col_label2: v1.index,
    col_values2: v1.values
})

bar2 =  dcc.Graph(id='bar2',
              figure={
        'data': [go.Bar(x=new['Category'],
                        y=new['count'])],
        'layout': {'title':dict(
            text = 'Top Categories based on Count',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':600,
        "line":dict(
                color="white",
                width=4,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Number of Categories',color='white')
    }})
    ###
col_label3 = "Market"
col_values3 = "count"

v2 = df[col_label3].value_counts().head(10)
new = pd.DataFrame({
    col_label3: v2.index,
    col_values3: v2.values
})

bar3 =  dcc.Graph(id='bar3',
              figure={
        'data': [go.Bar(x=new['Market'],
                        y=new['count'])],
        'layout': {'title':dict(
            text = 'Top Market based on Count',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':600,
        "line":dict(
                color="white",
                width=4,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Number of Categories',color='white')
    }})
##
col_label4 = "Crypto"
col_values4 = "count"

v3 = df[col_label4].value_counts().head(10)
new = pd.DataFrame({
    col_label4: v3.index,
    col_values4: v3.values
})

bar4 =  dcc.Graph(id='bar4',
              figure={
        'data': [go.Bar(x=new['Crypto'],
                        y=new['count'])],
        'layout': {'title':dict(
            text = 'Highest grossing Crypto currency in the market',
            font = dict(size=20,
            color = 'white')),
        "paper_bgcolor":"#111111",
        "plot_bgcolor":"#111111",
        'height':600,
        "line":dict(
                color="white",
                width=4,
                dash="dash",
            ),
        'xaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='',color='white'),
        'yaxis' : dict(tickfont=dict(
            color='white'),showgrid=False,title='Number of CryptoCurrency',color='white')
    }})
timegraph = dcc.Graph(id = 'plot', figure = fig)
graphrow = dbc.Row([dbc.Col(timegraph,md=12)])                     
graphRow1 = dbc.Row([dbc.Col(bar1,md=6), dbc.Col(bar2, md = 6)])
graphRow2 = dbc.Row([dbc.Col(bar3, md=6), dbc.Col(bar4, md=6)])
app.layout = html.Div([navbar,html.Br(),graphrow,html.Br(),graphRow1,html.Br(),graphRow2], style={'backgroundColor':'black'})

if __name__ == '__main__':
    app.run_server(debug=True,port=8056)
