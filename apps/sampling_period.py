from datetime import datetime

import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

df = pd.read_csv('/Users/laurat/Desktop/2020-05-05_pangea_db_sharing_extract.csv')
df = df[['geo_country', 'visit_dt']]
df['visit_dt'] = df['visit_dt'].apply(lambda x: datetime.strptime(x, '%Y-%m-%d').date())
df['visit_year'] = df['visit_dt'].apply(lambda x: x.year)
del df['visit_dt']
df = df.groupby(['geo_country', 'visit_year']).size().reset_index()
df.rename(columns={0: 'count'}, inplace=True)
df = df[df['visit_year'] >= 2000]

# x-axis is year of sampling
fig = px.bar(df, x="visit_year", y="count", color="geo_country", barmode="stack")
fig.update_layout(
    title={
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title='Sampling year',
    yaxis_title='Number of samples',
    legend_title='Country',
    xaxis={'type': 'category'})
fig.update_traces(hovertemplate=None)

layout = html.Div(children=[

    dcc.Graph(figure=fig),
    html.Div(id='sampling-period-content')])
