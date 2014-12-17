from teamList import teams
from getPremLeague import *
import plotly.plotly as py
import pandas as pd
from plotly.graph_objs import *
py.sign_in("plotlyusername", "password")


teams=list(['Arsenal_F.C.',
'Aston_Villa_F.C.',
#'Burnley_F.C.',
'Chelsea_F.C.',
'Crystal_Palace_F.C.',
'Everton_F.C.',
'Hull_City_A.F.C.',
#'Leicester_City',
'Liverpool_F.C.',
'Manchester_City_F.C.',
'Manchester_United_F.C.',
'Newcastle_United_F.C.',
#'Queens_Park_Rangers',
#'Southampton_F.C.',
'Stoke_City_F.C.',
'Sunderland_A.F.C.',
'Swansea_City_A.F.C.',
#'Tottenham_Hotspur_F.C.',
#'West_Bromwich_Albion',
#'West_Ham_United',
]
)


Teamdata={}
for key in teams :

    wiki="http://en.wikipedia.org/wiki/List_of_"+key+"_seasons"
    print key,getPremLeague(wiki)
    writeCsv(key)
    Teamdata[key]=getPremLeague(wiki)
data=[]
for key in teams:
    wins=(Teamdata[key]["Wins"])
    data.append(
    Scatter(
    x=Teamdata[key]["Years"],
    y=wins,
    name=key, mode='lines'
            )
            )





layout = Layout(
    title='Visualizing Premier League Matches 1992-2013 ',
    xaxis=XAxis(title='Year'),
    yaxis=YAxis(title='Season Matches won'),
    legend=Legend(x=0.0,y=1.0))

fig = Figure(data=Data(data), layout=layout)

py.iplot(fig, filename='Visualizing Premier League Matches 1992-2013')