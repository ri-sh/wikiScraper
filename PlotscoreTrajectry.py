from teamList import teams
from getPremLeague import *
import plotly.plotly as py
import pandas as pd
from plotly.graph_objs import *
py.sign_in("plotlyusername", "password")




Teamdata={}
for key in teams :

    wiki="http://en.wikipedia.org/wiki/List_of_"+key+"_seasons"
    print key,getPremLeague(wiki)
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