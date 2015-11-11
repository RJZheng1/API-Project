import urllib2
import json
from bs4 import BeautifulSoup

#API here
def getAPI(name):
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(name)
    result = json.loads(urllib2.urlopen(url).read())
    key = result['query']['pages'].keys()[0]
    info = result[u'query']['pages'][key]['revisions'][0]
    soup = BeautifulSoup(info['*'],'html.parser')
    print soup
    
getAPI("Germany")
