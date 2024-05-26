import pandas as pd
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html, callback
import plotly.express as px
import plotly.graph_objects as go
import base64

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], meta_tags=[
    {"name": "viewport", "content": "width=device-width, initial-scale=1"}
])



data_1 = pd.read_csv('deliveries.csv')
data_2 = pd.read_csv("matches.csv")

rcb = 'rcb.png'
kings11 = 'kings11.png'
DelhiD = 'daredevils.png'
MI = 'mi.png'
kkr = 'kkr.png'
rr = 'rr_.png'
deccan = 'deccan.png'
csk = 'csk.png'
kochi = 'kochi.png'
Pune_war = 'punewar.png'
srh = 'srh.png'
gujratlions = 'GL.png'
risingpune = 'rpsg.png'
delhic = 'capitals.png'
punjabk = 'punkings.png'
lucknow = 'lsg.png'
gt = 'titans.png'

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "14rem",
    "padding": "1rem 1rem",
    "background-color": "#800020",
}
CONTENT_STYLE = {
    "margin-left": "14rem",
    "margin-right": "0rem",
    "padding": "1rem 1rem",
    "background-color": "#c686ee",

}

sidebar = html.Div(
    [
        dbc.Row([html.H2('Dashboard', style={'text-align': 'center', 'color': 'white'})]),
        dbc.Row([html.Hr(style={'color': 'white'})]),
        dbc.Row([html.Br()]),
        dbc.Row([html.H6('Season', className="display-12", style={'color': 'white', 'text-align': 'center'})]),
        dbc.Row([

            dbc.Card(
                dbc.CardBody([
                    dbc.Row([

                        dcc.Dropdown(data_2.season.unique(), '2023', id='dropdown1',
                                     style={'borderRadius': '15px', 'width': '150px', 'margin-right': '0rem'}),

                    ]),

                ]),
                style={'borderRadius': '15px', 'margin-left': '0rem', 'fontFamily': 'Helvetica', 'font-weight': 'bold',
                       'background-color': '#574f5c', 'width': '250px'}
            )

        ]),

        dbc.Row([html.Br()]),
        dbc.Row([html.H6('Match Type', className="display-12", style={'color': 'white', 'text-align': 'center'})]),
        dbc.Row([

            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(data_2.match_type.unique(), 'Final', id='dropdown2',
                                         style={'borderRadius': '15px', 'width': '150px', 'margin-left': '0rem'}),
                        ]),
                    ]),

                ]),
                style={'borderRadius': '15px', 'margin-left': '0rem', 'fontFamily': 'Helvetica', 'font-weight': 'bold',
                       'background-color': '#574f5c', 'width': '250px'}
            )

        ]),

        dbc.Row([html.Br()]),
        dbc.Row([html.H6('Match Id', className="display-12", style={'color': 'white', 'text-align': 'center'})]),
        dbc.Row([

            dbc.Card(
                dbc.CardBody([
                    dbc.Row([
                        dbc.Col([
                            dcc.Dropdown(data_2.id.unique(), 1370353, id='dropdown3',
                                         style={'borderRadius': '15px', 'width': '150px', 'margin-left': '0rem'}),
                        ]),
                    ]),

                ]),
                style={'borderRadius': '15px', 'margin-left': '0rem', 'fontFamily': 'Helvetica', 'font-weight': 'bold',
                       'background-color': '#574f5c', 'width': '250px'}
            )

        ])

        # dcc.Dropdown(data_2.season.unique(),'2023',id='dropdown1',style={'borderRadius': '15px','width':'200px', 'margin-left':'0rem'}),
        #  dcc.Dropdown(data_2.match_type.unique(),'Final',id='dropdown2',style={'borderRadius': '15px','width':'200px', 'margin-left':'0rem'}),
        #   dcc.Dropdown(data_2.id.unique(),1370353,id='dropdown3',style={'borderRadius': '15px','width':'200px', 'margin-left':'0rem'})

    ],
    style=SIDEBAR_STYLE
)

main_content = html.Div([
    dbc.Row([html.Br()]),

    dbc.Row([
        dbc.Card(dbc.Col(html.H4("Indian Premier League", className="display-5",
                                 style={'color': '#012fac', 'text-align': 'center'})),
                 style={'borderRadius': '15px', 'margin-left': '2rem',
                        'fontFamily': 'Helvetica',
                        'font-weight': 'bold', 'background-color': 'white', 'width': '1045px'}), ]),

    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([
        dbc.Card(
            dbc.CardBody([
                dbc.Row([
                    dbc.Col(
                        [html.Img(id='team1_logo', style={'height': '300px', 'width': '300px', 'margin-left': '4rem'})],
                        width=5),
                    # html.Img(src=f"data:image/png;base64,{encoded_image}", style={'width': '50%'})
                    dbc.Col([html.P('   ', className="display-10", style={'margin-left': '8rem', 'color': 'white'})],
                            width=2),
                    dbc.Col(
                        [html.Img(id='team2_logo', style={'height': '300px', 'width': '300px', 'margin-left': '4rem'})],
                        width=5)
                ]),
                dbc.Row([
                    dbc.Col(
                        [html.H5(id='team1', className="display-5", style={'color': 'white', 'text-align': 'center'})],
                        width=5),
                    dbc.Col([html.P('vs', className="display-10", style={'text-align': 'center', 'color': 'white'})],
                            width=2),
                    dbc.Col(
                        [html.H5(id='team2', className="display-5", style={'color': 'white', 'text-align': 'center'})],
                        width=5)
                ]),
                dbc.Row([
                    dbc.Col([html.H5('', className='card-text')], width=4),
                    dbc.Col(
                        [html.P(id='venue', className="display-10", style={'color': 'white', 'text-align': 'center'})],
                        width=4),
                    dbc.Col([html.H5('', className='card-text')], width=4)
                ]),
                dbc.Row([
                    dbc.Col([html.H5('', className='card-text')], width=4),
                    dbc.Col(
                        [html.P(id='city', className="display-10", style={'color': 'white', 'text-align': 'center'})],
                        width=4),
                    dbc.Col([html.H5('', className='card-text')], width=4)
                ]),

            ]),
            style={'borderRadius': '15px', 'margin-left': '2rem', 'fontFamily': 'Helvetica', 'font-weight': 'bold',
                   'background-color': '#574f5c', 'width': '1045px', 'height': '550px'}
        )
    ]),
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([
        dbc.Col([dbc.Card([
            dbc.CardHeader(html.H5('Toss', className='card-text', style={'text-align': 'center'})),
            dbc.CardBody([
                dbc.Row([
                    dbc.Col([
                        html.P(id='toss', className="display-10", style={'text-align': 'center', 'color': 'white'})
                    ]),
                ]),
                dbc.Row([html.P(id='toss_d', className="display-10", style={'text-align': 'center', 'color': 'white'})])

            ], style={'background-color': '#574f5c', 'height': '100px'})
        ], style={'width': '250px', 'borderRadius': '15px', 'margin-left': '.5rem'})], width=3),
        dbc.Col([dbc.Card([
            dbc.CardHeader(html.H5('Onfield Umpires', className='card-text', style={'text-align': 'center'})),
            dbc.CardBody([
                dbc.Row(
                    [html.P(id='umpire1', className="display-10", style={'text-align': 'center', 'color': 'white'})]),
                dbc.Row(
                    [html.P(id='umpire2', className="display-10", style={'text-align': 'center', 'color': 'white'})])

            ], style={'background-color': '#574f5c', 'height': '100px'})
        ], style={'width': '250px', 'borderRadius': '15px', 'margin-left': '.5rem'})], width=3),

        dbc.Col([dbc.Card([
            dbc.CardHeader(html.H5('Winner', className='card-text', style={'text-align': 'center'})),
            dbc.CardBody([
                dbc.Row(
                    [html.P(id='winner', className="display-10", style={'text-align': 'center', 'color': 'white'})]),
                dbc.Row([html.P(id='wonby', className="display-10", style={'text-align': 'center', 'color': 'white'})])

            ], style={'background-color': '#574f5c', 'height': '100px'})
        ], style={'width': '250px', 'borderRadius': '15px', 'margin-left': '.5rem'})], width=3),

        dbc.Col([dbc.Card([
            dbc.CardHeader(html.H5('Player of the Match', className='card-text', style={'text-align': 'center'})),
            dbc.CardBody([
                dbc.Row([html.P(id='mom', className="display-10", style={'text-align': 'center', 'color': 'white'})]),
                dbc.Row([html.Br()])

            ], style={'background-color': '#574f5c', 'height': '100px'})
        ], style={'width': '250px', 'borderRadius': '15px', 'margin-left': '.5rem'})], width=3)

    ]),
    dbc.Row([html.Br()]),
    dbc.Row([html.Br()]),
    dbc.Row([
        dbc.Col([

            dbc.Card([
                dbc.CardHeader(html.H5(id='team_1', className='card-text', style={'text-align': 'left'})),
                dbc.CardBody([
                    dbc.Row([html.P('Top Run Scorers', className="display-10",
                                    style={'text-align': 'center', 'color': 'white'})]),
                    dbc.Row([dcc.Graph(id='team1_graph', config={'displayModeBar': False}, style={'width': '490px'})]),
                    dbc.Row([html.Br()])
                ], style={'background-color': '#574f5c'})
            ], style={'width': '520px', 'borderRadius': '15px', 'margin-left': '.5rem'})
        ]),
        dbc.Col([
            dbc.Card([
                dbc.CardHeader(html.H5(id='team_2', className='card-text', style={'text-align': 'left'})),
                dbc.CardBody([
                    dbc.Row([html.P('Top Run Scorers', className="display-10",
                                    style={'text-align': 'center', 'color': 'white'})]),
                    dbc.Row([dcc.Graph(id='team2_graph', config={'displayModeBar': False}, style={'width': '490px'})]),
                    dbc.Row([html.Br()])
                ], style={'background-color': '#574f5c'})
            ], style={'width': '520px', 'borderRadius': '15px', 'margin-left': '.5rem'})
        ])
    ]),
    dbc.Row([html.Br()]),
    dbc.Row([html.P('Developed by Kartik and it contains data till 2023 since inception.',
                    style={'margin-left': '2rem', 'color': 'black'})]),
    dbc.Row([html.Br()])

], style=CONTENT_STYLE)

app.layout = html.Div([sidebar, main_content])


@app.callback(
    Output('dropdown2', 'options'),
    Input('dropdown1', 'value')
)
def update_match_types(selected_season):
    if selected_season:
        # Filter the data based on selected season
        filtered_data = data_2[data_2['season'] == selected_season]
        # Get unique match types for the selected season
        match_types = filtered_data['match_type'].unique()
        # Return options for dropdown2
        return [{'label': match_type, 'value': match_type} for match_type in match_types]
    else:
        return []


@app.callback(
    Output('dropdown3', 'options'),
    Input('dropdown1', 'value'),
    Input('dropdown2', 'value')
)
def update_match_ids(selected_season, selected_match_type):
    if selected_season and selected_match_type:
        # Filter the data based on selected season and match type
        filtered_data = data_2[(data_2['season'] == selected_season) & (data_2['match_type'] == selected_match_type)]
        # Return options for dropdown3
        return [{'label': match_id, 'value': match_id} for match_id in filtered_data['id'].unique()]
    else:
        return []


@app.callback(
    [Output('team1', 'children'),
     Output('team2', 'children'),
     Output('venue', 'children'),
     # Output('date', 'children'),
     Output('city', 'children'),
     Output('team1_logo', 'src'),
     Output('team2_logo', 'src'),
     Output('toss', 'children'),
     Output('toss_d', 'children'),
     Output('umpire1', 'children'),
     Output('umpire2', 'children'),
     Output('winner', 'children'),
     Output('wonby', 'children'),
     Output('mom', 'children'),
     Output('team_1', 'children'),
     Output('team_2', 'children'),
     Output('team1_graph', 'figure'),
     Output('team2_graph', 'figure')
     ],
    [Input('dropdown1', 'value'),
     Input('dropdown2', 'value'),
     Input('dropdown3', 'value')]
)
def update_match_details(selected_season, selected_match_type, selected_match_id):
    if selected_season and selected_match_type and selected_match_id:
        # Filter the data based on selected season, match type, and match id
        filtered_data = data_2[(data_2['season'] == selected_season) &
                               (data_2['match_type'] == selected_match_type) &
                               (data_2['id'] == selected_match_id)]
        if not filtered_data.empty:
            match_details = filtered_data.iloc[0]
            team1 = match_details['team1']
            team2 = match_details['team2']
            if match_details['toss_decision'] == 'field':
                toss_d = 'Choosed to field'
            else:
                toss_d = 'Choosed to bat'
            # Update the elements with match details
            u1 = match_details['umpire1']
            u2 = match_details['umpire2']
            w = match_details['winner']
            mom = match_details['player_of_match']
            wb = 'Won by' + ' ' + str(int(match_details['result_margin'])) + ' ' + match_details['result']

            d = data_1[(data_1['match_id'] == selected_match_id)]
            d1 = d.groupby(['batter', 'batting_team'])['total_runs'].sum().reset_index()
            d2 = d.groupby(['batter', 'batting_team'])['extra_runs'].sum().reset_index()
            runs = d1['total_runs'] - d2['extra_runs']
            d1['Runs Scored'] = runs
            d1['Runs Scored'] = d1['Runs Scored'].apply(lambda x: 0 if x < 0 else x)
            d3 = d1.sort_values(by='Runs Scored')
            d3 = d3.rename(columns={'batter': 'Batsman'})
            d4 = d3[d3['batting_team'] == team1]
            d5 = d3[d3['batting_team'] == team2]
            t1 = team1 + ' ' + 'Total Score:' + ' ' + str(sum(d4['total_runs']))
            t2 = team2 + ' ' + 'Total Score:' + ' ' + str(sum(d5['total_runs']))
            fig1 = px.bar(d4, x='Runs Scored', y='Batsman', orientation='h', template='plotly_white',
                          color_discrete_sequence=['#c686ee'])
            fig2 = px.bar(d5, x='Runs Scored', y='Batsman', orientation='h', template='plotly_white',
                          color_discrete_sequence=['#c686ee'])
            fig1.update_layout(
                xaxis_showgrid=False,
                yaxis_showgrid=False,
                xaxis_title='',  # Remove x-axis label
                yaxis_title='',
                legend=dict(title=None),  # Remove legend title
                title=None,  # Remove title
                margin=dict(l=0, r=0, t=0, b=0),  # Set margin to remove extra space
                showlegend=False,  # Hide legend
                annotations=[],  # Remove annotations
                updatemenus=[],

            )
            fig2.update_layout(
                xaxis_showgrid=False,
                yaxis_showgrid=False,
                xaxis_title='',  # Remove x-axis label
                yaxis_title='',
                legend=dict(title=None),  # Remove legend title
                title=None,  # Remove title
                margin=dict(l=0, r=0, t=0, b=0),  # Set margin to remove extra space
                showlegend=False,  # Hide legend
                annotations=[],  # Remove annotations
                updatemenus=[],

            )

            return team1, team2, match_details['venue'], match_details['city'], team_logo(team1), team_logo(team2), \
            match_details['toss_winner'], toss_d, u1, u2, w, wb, mom, t1, t2, fig1, fig2
        else:
            return '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''
    else:
        return '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''


def team_logo(team_name):
    if team_name == 'Royal Challengers Bangalore':
        with open(rcb, "rb") as f:
            rcb_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{rcb_encoded}"
    elif team_name == 'Kings XI Punjab':
        with open(kings11, "rb") as f:
            kings11_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{kings11_encoded}"
    elif team_name == 'Delhi Daredevils':
        with open(DelhiD, "rb") as f:
            delhid_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{delhid_encoded}"
    elif team_name == 'Mumbai Indians':
        with open(MI, "rb") as f:
            MI_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{MI_encoded}"
    elif team_name == 'Kolkata Knight Riders':
        with open(kkr, "rb") as f:
            kkr_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{kkr_encoded}"
    elif team_name == 'Rajasthan Royals':
        with open(rr, "rb") as f:
            rr_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{rr_encoded}"
    elif team_name == 'Deccan Chargers':
        with open(deccan, "rb") as f:
            deccan_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{deccan_encoded}"
    elif team_name == 'Chennai Super Kings':
        with open(csk, "rb") as f:
            csk_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{csk_encoded}"
    elif team_name == 'Kochi Tuskers Kerala':
        with open(Kochi, "rb") as f:
            Kochi_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{Kochi_encoded}"
    elif team_name == 'Pune Warriors':
        with open(Pune_war, "rb") as f:
            Pune_war_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{Pune_war_encoded}"

    elif team_name == 'Sunrisers Hyderabad':
        with open(srh, "rb") as f:
            srh_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{srh_encoded}"
    elif team_name == 'Gujarat Lions':
        with open(gujratlions, "rb") as f:
            gujratlions_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{gujratlions_encoded}"

    elif (team_name == 'Rising Pune Supergiants' or team_name == 'Rising Pune Supergiant'):
        with open(risingpune, "rb") as f:
            risingpune_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{risingpune_encoded}"

    elif team_name == 'Delhi Capitals':
        with open(delhic, "rb") as f:
            delhic_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{delhic_encoded}"

    elif team_name == 'Punjab Kings':
        with open(punjabk, "rb") as f:
            punjabk_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{punjabk_encoded}"
    elif team_name == 'Lucknow Super Giants':
        with open(lucknow, "rb") as f:
            lucknow_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{lucknow_encoded}"

    else:
        with open(gt, "rb") as f:
            gt_encoded = base64.b64encode(f.read()).decode()
        return f"data:image/png;base64,{gt_encoded}"


if __name__ == "__main__":
    app.run_server(port=8016)