import urllib2
import json

#API here 
url = "https://en.wikipedia.org/w/api.php?action=query&titles=Germany&prop=revisions&rvprop=content&format=json"

request = urllib2.urlopen(url)
result = request.read()
r = json.loads(result)
print r.keys()
print r[u'query'].keys()
print r[u'query'][u'pages'].keys()
print r[u'query'][u'pages'][u'11867'].keys()
print r[u'query'][u'pages'][u'11867'][u'revisions']


