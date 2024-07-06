import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load data
df = pd.read_csv('data.csv')

# Initialize Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Interactive Data Visualization'),
    dcc.Dropdown(
        id='category-dropdown',
        options=[{'label': cat, 'value': cat} for cat in df['Category'].unique()],
        value=df['Category'].unique()[0]
    ),
    dcc.Graph(id='bar-plot'),
    dcc.Interval(
        id='interval-component',
        interval=1*1000,  # in milliseconds
        n_intervals=0
    )
])

@app.callback(
    Output('bar-plot', 'figure'),
    [Input('category-dropdown', 'value'), Input('interval-component', 'n_intervals')]
)
def update_graph(selected_category, n_intervals):
    filtered_df = df[df['Category'] == selected_category]
    fig = px.bar(filtered_df, x='Subcategory', y='Value', title=f'Values in {selected_category}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
