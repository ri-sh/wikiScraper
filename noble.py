from bs4 import BeautifulSoup
import urllib2

wiki = "http://en.wikipedia.org/wiki/List_of_Nobel_laureates"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
table = soup.find("table", { "class" : "wikitable sortable" })
Year = []
Physics = []
Chemistry = []
Medicine = []
Literature = []
Peace = []
Economics = []
cells = table.findAll("tr")
for row in cells:
    m=row.findAll("td")
    if (len(m)>0):
        print BeautifulSoup(str(m[1])).find_all("span", { "class" : "fn" })
        names=BeautifulSoup(str(m[1])).find_all("span", { "class" : "fn" })

        na=[name.find(text=True).encode('utf-8') for name in names]
        print "############################################"
        Year.append(int((m[0].find(text=True))))
        Physics.append(na)
        Chemistry.append((m[2].find(text=True)).encode('utf-8'))
        Medicine.append(m[3].find(text=True).encode('utf-8'))
        Literature.append(m[4].find(text=True).encode('utf-8'))
        Peace.append(m[5].find(text=True).encode('utf-8'))
        Economics.append(m[5].find(text=True).encode('utf-8'))
