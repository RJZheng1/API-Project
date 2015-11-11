import urllib2
import json
from bs4 import BeautifulSoup

#API here
def getAPI(name):
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&rvprop=content&format=json".format(name)
    result = json.loads(urllib2.urlopen(url).read())
    key = result['query']['pages'].keys()[0]
    info = result[u'query']['pages'][key]['extract']
    soup = BeautifulSoup(info, 'html.parser')
    paragraphs = []
    for p in soup.find_all('p'):
        paragraphs.append(p.get_text().encode("ascii","ignore"))
    for i in paragraphs:
        print i
        
getAPI("Germany")


