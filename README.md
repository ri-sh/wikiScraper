#wikiScraper

##Scraper to scrape Premier League Data From Wikipedia using BeautifulSoup 

Manchester United Csv

| Season | Won | Draws | Lost | Position | Top goalscorer       | Goals |
|--------|-----|-------|------|----------|----------------------|-------|
| 1992   | 24  | 12    | 12   | 1st      | Mark Hughes          | 16    |
| 1993   | 27  | 11    | 11   | 1st      | Eric Cantona         | 25    |
| 1994   | 26  | 10    | 10   | 2nd      | Andrei Kanchelskis   | 15    |
| 1995   | 25  | 7     | 7    | 1st      | Eric Cantona         | 19    |
| 1996   | 21  | 12    | 12   | 1st      | Ole Gunnar Solskjaer | 19    |
| 1997   | 23  | 8     | 8    | 2nd      | Andy Cole            | 25    |
| 1998   | 22  | 13    | 13   | 1st      | Dwight Yorke         | 29    |
| 1999   | 28  | 7     | 7    | 1st      | Andy Cole            | 22    |
| 2000   | 24  | 8     | 8    | 1st      | Teddy Sheringham     | 21    |
| 2001   | 24  | 5     | 5    | 3rd      | Ruud van Nistelrooy  | 36    |
| 2002   | 25  | 8     | 8    | 1st      | Ruud van Nistelrooy  | 44    |
| 2003   | 23  | 6     | 6    | 3rd      | Ruud van Nistelrooy  | 30    |
| 2004   | 22  | 11    | 11   | 3rd      | Wayne Rooney         | 17    |
| 2005   | 25  | 8     | 8    | 2nd      | Ruud van Nistelrooy  | 24    |
| 2006   | 28  | 5     | 5    | 1st      | Wayne Rooney         | 23    |
| 2007   | 27  | 6     | 6    | 1st      | Cristiano Ronaldo    | 42    |
| 2008   | 28  | 6     | 6    | 1st      | Cristiano Ronaldo    | 26    |
| 2009   | 27  | 4     | 4    | 2nd      | Wayne Rooney         | 34    |
| 2010   | 23  | 11    | 11   | 1st      | Dimitar Berbatov     | 21    |
| 2011   | 28  | 5     | 5    | 2nd      | Wayne Rooney         | 34    |
| 2012   | 28  | 5     | 5    | 1st      | Robin van Persie     | 30    |
| 2013   | 19  | 7     | 7    | 7th      | Wayne Rooney         | 19    |



 * getPremLeague.py
###### takes the wiki url of football club season list url is

######    in form <"http://en.wikipedia.org/wiki/List_of_"+" FOotball team name_F.C."+"_seasons">
######    returns a dictionary containing
######    {
######        'Years': a numpy array of the year of prem league match starting from 1992 to 2103
######        'Wins':  a numpy array of year wise no of matches won
######        'Draw':  a numpy array of year wise no of matches draw
######        'Lose':  a numpy array of year wise no of matches lost
######        'Position': a list containg the rank of the team in  year
######        'Topscorer': a list containing the Top Goal Scorer
######        'Topgoals':  a list containing the Top Goal scored by the top scorer
######    }

* teamList.py -
###### contains list of team name in Premier league
*writeCsv.py -
###### generates the csv file for example 

