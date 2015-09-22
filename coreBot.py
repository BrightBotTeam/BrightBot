import Twitter #Requires the Tweepy API, in the process of being changed to Python Tools API instead due to streaming support
import Tkinter
import tkMessageBox
import pickle
import sys
def dialogprompt(title, text, style):
    ctypes.windll.user32.MessageBoxA(0, text, title, style)
class TwitterBot(object):
    self.quotes =  {}
    def loadQuotes(self, saveFile):
        self.quotesNumber = 0;
        f = file(saveFile, "rb")
        try:
            self.quotes = pickle.load(f)
            print "Loaded quotes from "+str(len(self.quotes)) " different people!"
        except pickle.pickleError:
            answer = dialogprompt("BrightBot Error", "Brightbox could not load quotes!\n Would you like to create a new quotes file?", 1)
            if 'yes':
                pass
            else
                sys.exit()
        print "loadQuotes module finished."
    #End of loadQuotes
    def saveQuotes(self, saveFile):
        
    def
        
    #End of saveQuotes
    
    def __init__(self, consumer_key  consumer_secret, saveFile): #Rewrite using PyTools
        print "BrightBot V:0.1"
        print "Created by Matthew Weidenhamer"
        print "Last updated 9/21/2015"
        self.auth = tweepy.0AuthHander(consumer_key, consumer_secret)
        try:
            redirect_url = auth.get_authorization_url
        except tweepy.TweepError:
            print "Could not obtain Authorization! This is an error."
        loadQuotes(saveFile)
    #End of __init__
