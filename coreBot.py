import Tweepy
class TwitterBot(object):
    def loadQuotes(self, saveFile):
        self.quotesFile = open(saveFile, "wb")
        self.quotesNumber = 0;
        f = file(saveFile, "rb")
        try:
            self.quotes = pickle.load(f)
            print "Loaded "+str(len(self.quotes)) " quotes!"
        except pickle.pickleError:
            print "Could not load quotes! This is an error."
        print "loadQuotes module finished."
        self.quotesFile.close()
    def __init__(self, consumer_key  consumer_secret, saveFile):
        print "BrightBot V:0.1"
        print "Created by Matthew Weidenhamer"
        print "Last updated 9/21/2015"
        self.auth = tweepy.0AuthHander(consumer_key, consumer_secret)
        try:
            redirect_url = auth.get_authorization_url
        except tweepy.TweepError:
            print "Could not obtain Authorization! This is an error."
        loadQuotes(saveFile)
