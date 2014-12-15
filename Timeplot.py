from teamList import teams
from getPremLeague import *
import plotly.plotly as py
import pandas as pd
from plotly.graph_objs import *
py.sign_in("username", "password")




Teamdata={}
for key in teams :

    wiki="http://en.wikipedia.org/wiki/List_of_"+key+"_seasons"
    #print key,getPremLeague(wiki)
    Teamdata[key]=getPremLeague(wiki)
data=[]
for key in teams:
    wins=pd.Series(Teamdata[key]["Wins"]).cumsum()
    data.append(
    Scatter(
    x=Teamdata[key]["Years"],
    y=wins,
    name=key, mode='lines'
            )
            )





layout = Layout(
    title='PremLeague Team Trajectory 1992-2013 ',
    xaxis=XAxis(title='Year'),
    yaxis=YAxis(title='Total Matches Won'),
    legend=Legend(x=0.0,y=1.0))

fig = Figure(data=Data(data), layout=layout)

py.iplot(fig, filename='Visualizing Premier League Match TRajectory 1992-2013')