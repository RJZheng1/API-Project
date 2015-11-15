import urllib2
import json
from bs4 import BeautifulSoup

#Gets first paragraph from Wikipedia about the location
def getWiki(location):
    '''
    This will return the title of an article that mostly closely matches your query.
    action=query allows you to get information and data
    list=search is a submodule used for searching through titles and text. Data is returned in a list.
    srsearch={} specifies what you are searching for
    srlimit=1 limits the results to just one page
    format=json will return the data in json format
    '''
    url1 = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&srlimit=1&format=json".format(location)
    result1 = json.loads(urllib2.urlopen(url1).read())
    if len(result1['query']['search']) == 0:
        return None
    place = result1['query']['search'][0]['title'].replace(" ", "%20")
    '''
    This will return the text in an article.
    action=query allows you to get information and data
    titles={} will look for the wikipedia article with the specified title
    prop=extracts will return plain-text or limited HTML extracts of the page
    format=json will return the data in json format
    '''
    url2 = "https://en.wikipedia.org/w/api.php?action=query&titles={}&prop=extracts&format=json".format(place)
    result2 = json.loads(urllib2.urlopen(url2).read())
    key = result2['query']['pages'].keys()[0]
    info = result2[u'query']['pages'][key]['extract']
    soup = BeautifulSoup(info, 'html.parser')
    paragraphs = []
    for p in soup.find_all('p'):
        paragraphs.append(p.get_text().encode("utf-8"))
    return paragraphs[0]

'''NO LONGER IN USE'''
def getPlaces(query):
    """Returns a list of dicts each with info on a different place that matches the query
    DEPRECATED"""
    placesKey = "AIzaSyCX2pUzMG4Es5RjILnPwBQ8RG1kn0855BI"
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s"%(query,placesKey)
    result = json.loads(urllib2.urlopen(url).read())
    return result['results']

def coordinates(query):
    """Gets coords for query using bing maps"""
    key = "Aj1X2oDWw6lKh5Y5Roy_uyou-ySwIiBhRzBVQMKMG9KVYoWXtw7XczdppkOnXe3L"
    url = "http://dev.virtualearth.net/REST/v1/Locations?query=%s&maxResults=1&key=%s"
    url = url%(query,key)
    print url
    result = json.loads(urllib2.urlopen(url).read())
    if result['resourceSets'][0]['estimatedTotal'] == 0:
        return None
    coord =  result['resourceSets'][0]['resources'][0]['point']['coordinates']
    coord = {'lat':coord[0], 'lng':coord[1]}
    return coord
    

