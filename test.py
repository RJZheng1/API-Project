import urllib2, json
from flask import Flask, render_template, request
from bs4 import BeautifulSoup

app = Flask(__name__)

placesKey = "AIzaSyCX2pUzMG4Es5RjILnPwBQ8RG1kn0855BI"

@app.route("/")
def main():
    query = "gemsny"
    url = "https://en.wikipedia.org/w/api.php?action=query&titles=%s&prop=revisions&rvprop=content&format=json"
   
    url = url%query

    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?query=%s&key=%s"%(query,placesKey)

    request = urllib2.urlopen(url)

    result = request.read()

    print type(result)
    print result

    return json.load(request.read())

if __name__ == "__main__":
    app.debug = True
    app.run()

