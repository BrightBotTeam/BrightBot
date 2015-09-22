import ctypes
import pickle
import sys
def dialogprompt(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)
class TwitterBot(object):
    quotes =  {}
    def loadQuotes(self, saveFile):
        print("Attempting to load quotes...")
        self.quotesNumber = 0;
        try:
            f = open(saveFile, "rb")
            self.quotes = pickle.load(f)
            print("Loaded quotes from " + str(len(self.quotes)) + " different people!")
        except FileNotFoundError:
            answer = dialogprompt("BrightBot Error", "Brightbox could not load a quotes file!\nWould you like to create a new quotes file?", 1)
            if 'yes':
                f = open(saveFile, "wb")
                print("New save file created.")
            else:
                f.close()
                sys.exit()
        print("loadQuotes module finished.")
    #End of loadQuotes
    def saveQuotes(self):
        pass
    #End of saveQuotes
    
    def __init__(self): 
        print("BrightBot V:0.1")
        print("Created by Matthew Weidenhamer")
        print("Last updated 9/21/2015")
    #End of __init__
BrightBot = TwitterBot()
BrightBot.loadQuotes("quotes.txt")
