import urllib2
import json


#API here
def getAPI(name):
    url = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=revisions&rvprop=content&format=json".format(name)    
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    print r.keys()
    print r[u'query'].keys()
    key = r[u'query'][u'pages'].keys()[0]
    print r[u'query'][u'pages'][key].keys()
    print r[u'query'][u'pages'][key][u'revisions']

getAPI("Germany")
