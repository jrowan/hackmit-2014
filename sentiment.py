###HACKMIT 2014 - James Rowan, Milan Savani, Adam Rawot, and Noah Yonack
## orve
## helper functions for sentiment analysis

import json
import urllib2
##param textQuery the (unformmated) string you want to analyze the sentiment of
##returns the json containing the sentiment anaylsis as performed by the
##HP IDOL on Demand API
def text_sentiment_in_json(text_query):
    formmated_text_query = urllib2.quote(text_query)
    req = urllib2.urlopen("https://api.idolondemand.com/1/api/sync/analyzesentiment/v1?text=" \
                          + formmated_text_query + "&apikey=46d5fbfc-c772-4e3d-84a1-06ca992a6c80")
    response = req.read()
    return response

##param sentimentJson a string representing a json that is the result of sentiment analysis returned
##by the HP IDOL on Demand API
##returns a tuple of dictionaries, the dictionary of positive elements,
##the dictionary of negative elements, and the dictionary of aggregate info
##dictionaries for positive and negative elements contain list of dictionaries,
##one for each positive/negative sentiment, which contain information about the
##sentiment
def parse_json_sentiment(sentiment_json):
    loaded_json = json.loads(sentiment_json)
    raise Exception("not yet implemented")

## param sentimentJson a string representing a json that is the result of
## sentiment analysis by the HP IDOL on Demand API
##returns a float representing the aggregate score
def total_sentiment_score(sentiment_json):
    last_chunk = sentiment_json[sentiment_json.find("aggregate"):]
    score_site = last_chunk.find("score")+8
    real_last_chunk = last_chunk[score_site:]
    end_site = real_last_chunk.find("\n")
    score_string = real_last_chunk[:end_site]
    return float(score_string)
    
