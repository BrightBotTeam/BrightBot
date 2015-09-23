import ctypes
import pickle
import sys
def dialogprompt(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)
class TwitterBot(object):
    quotes =  {}
    def loadQuotes(self, saveFile):
        print("Attempting to load quotes from " + saveFile)
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
                f.close()
            else:
                f.close()
                sys.exit()
        print("loadQuotes module finished.")
    #End of loadQuotes
    def saveQuotes(self, saveFile):
        print("Attempting to save quotes to " + saveFile)
        f = open(saveFile, "wb")
        pickle.dump(self.quotes, f)
        f.close()
        print("Saved Successfuly.")
    #End of saveQuotes
    def getQuote(self, person, number, sentRequest):
        print(sentRequest + " has requested quote number " + number " of " + person + ".")
        currentQuote = ""
        try:
            currentQuote = Quotes{person}[number - 1]
            print(currentQuote)
            return currentQuote
        except KeyError:
            print("Could not find key " + person + "! Returning False...")
            return False
        except IndexError:
            print("Could not find quote number " + number + " for " + person + "! Returning False...")
            return False
    #End of getQuote
    def __init__(self): 
        print("BrightBot V:0.1")
        print("Created by Matthew Weidenhamer")
        print("Last updated 9/21/2015")
    #End of __init__
BrightBot = TwitterBot()
BrightBot.loadQuotes("quotes.p")
while true:
    pass
