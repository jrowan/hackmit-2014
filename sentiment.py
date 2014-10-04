import urllib2
##param textQuery the (unformmated) string you want to analyze the sentiment of
##returns the json containing the sentiment anaylsis as performed by the
##HP IDOL on Demand API
def text_sentiment_in_json(textQuery):
    textQuery = raw_input()
    formmatedTextQuery = urllib2.quote(textQuery)
    req = urllib2.urlopen("https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text=" \
                          + formmatedTextQuery + "&apikey=46d5fbfc-c772-4e3d-84a1-06ca992a6c80")
    response = req.read()
    return response
