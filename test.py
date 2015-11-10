import urllib2, json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    url = "https://en.wikipedia.org/w/api.php?action=query&titles=%s&prop=revisions&rvprop=content&format=json"
    url = url%"Germany"
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    print r['query']['pages']['11867']['title']
    return result

if __name__ == "__main__":
    app.debug = True
    app.run()
