from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import urllib2
soup=''
def getPremLeague(wiki):
    """
    input takes the wiki url of football club season list url is
    in form <"http://en.wikipedia.org/wiki/List_of_"+" FOotball team name"+"_F.C._seasons">
    returns a dictionary containing
    {
        'Years': a numpy array of the year of prem league match starting from 1992 to 2103
        'Wins':  a numpy array of year wise no of matches won
        'Draw':  a numpy array of year wise no of matches draw
        'Lose':  a numpy array of year wise no of matches lost
        'Position': a list containg the rank of the team in  year
        'Topscorer': a list containing the Top Goal Scorer
        'Topgoals':  a list containing the Top Goal scored by the top scorer
    }

    """
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    #print soup
    table = soup.find("table", { "class" : "wikitable sortable" })
    if (table==None):
        table = soup.find("table", { "class" : "wikitable plainrowheaders" })
    if(table ==None):
        soup.find("table", { "class" : "wikitable plainrowheaders sortable" })


    won=[]
    draw=[]
    lose=[]
    years=[]
    position=[]
    TopScorer=[]
    Topgoal=[]
    #print table
    for row in table.findAll("tr"):

        cells = row.findAll("td")
        #print cells

        if len(cells) > 4:
            if(len(cells[2].text)<=2 and len(cells[0].text.encode('ascii','ignore'))>1 ):

                if("Prem" in (cells[0].text.encode('ascii','xmlcharrefreplace') )):
                    #print type(cells[0].text),"#",cells[0].text
                    yrs=BeautifulSoup(str(row.findAll("th")))
                    #print  cells[0].text,yrs.text[1:5],cells[2].text[:2],cells[8].text,cells[len(cells)-2].text,cells[len(cells)-1].text
                    if (yrs.text[1:5]!='2014'):

                        years.append(int(yrs.text[1:5]))
                        #print "++++++++++++++++++++"
                        won.append(int((cells[2].text[:2])))
                        draw.append(int(cells[3].text[:2]))
                        lose.append(int(cells[3].text[:2]))
                        position.append(cells[8].text)
                        TopScorer.append(cells[len(cells)-2].text)
                        Topgoal.append(int(cells[len(cells)-1].text[:2]))
    Team={'Years':np.array(years),
           'Wins':np.array(won),
           'Draws':np.array(draw),
           'Lose' :np.array(lose),
           'Position':position,
           'Topscorer':TopScorer,
           'Topgoal':np.array(Topgoal),


        }
    return Team

