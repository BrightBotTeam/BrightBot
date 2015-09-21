import Tweepy
class TwitterBot(object)://Creating the first bot
    
    def __init__(self, consumer_key  consumer_secret): // You need to supply your own  consumer key and consumer secret key. 
        print "BrightBot V:0.1"
        print "Created by Matthew Weidenhamer"
        print "Last updated 9/21/2015"
        self.auth = tweepy.0AuthHander(consumer_key, consumer_secret)
        try:
            redirect_url = auth.get_authorization_url
        except tweety.TweepError:
            print "Could not obtain Authorization! This is an error."
        
