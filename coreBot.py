import ctypes
import pickle
import sys
import datetime
import random
def dialogprompt(title, text, style):
    ctypes.windll.user32.MessageBoxW(0, text, title, style)
class TwitterBot(object):
    quotes =  {}
    commands = ["!bestof", "lenny", "!outcome", "!poll", "!answer"]
    def toDo(self, command, sender):
        doThis, data = commandGet.split(" ", 1)
        if doThis == BrightBot.commands[0]: #Best Of
            action, person, response = data.split(" ", 3)
            action = action.lower()
            person = person.lower()
            response = response.lower()
            if action == "get":
                return self.getQuote(person, response)
            elif action == "add":
                return self.addQuote(person, response)
            elif action == "delete:
                return self.delQuote(person, response)
            else:
                return "Unrecognized action, please check spelling."
        elif doThis == BrightBot.commands[1]: #Lenny
            return self.lenny()
        elif doThis == BrightBot.commands[2]: #Outcome
            x, y, event = data.split(" ", 2)
            return self.outcome(x, y, event)
        elif doThis == BrightBot.commands[3]: #Poll
            pass
        elif doThis == BrightBot.commands[4]: #Answer
            pass
        elif doThis == BrightBot.commands[5]: #Stop Poll
            pass
        elif doThis == BrightBot.commands[6]: #Moods
            return self.mood(data)
        elif doThis == BrightBot.commands[7]: #WhoAmI
            pass
        else:
            return "Unknown command."
    #End of toDo
    def loadQuotes(self, saveFile):
        print("Attempting to load quotes from " + saveFile)
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
            print("Could not find person " + person + "! Returning False...")
            return False
        except IndexError:
            print("Could not find quote number " + number + " for " + person + "! Returning False...")
            return False
    #End of getQuote
    def addQuote(self, person, quote):
        try:
            self.quotes{person}
            self.quotes{person}.append(quote):
            return True
        except KeyError:
            self.quotes{person} = [quote]
            return True
    #End of addQuote
    def delQuote(self, person, quote):
        try:
            del self.quotes{person}[quote]
            return True
        except KeyError:
            return False
        except IndexError:
            return False
    #End of delQuote
    def lenny(self):
        todaysDate = date.today()
        lennyRepo = {1 : "( ͡° ͜ʖ ͡,°)" 2 : "( ͠° ͟ʖ ͡°)", 3 : "ᕦ( ͡° ͜ʖ ͡°)ᕤ", 4 : "( ͡~ ͜ʖ ͡°)", 5 : 6 : 7 : 8 : 9 : 10 : 11 : 12 : 13 : 14 : 15 : 16 : 17 : 18 : 19 : 20 : 21 : 2 2: 23 : 24 : 25 : 26 : 27 : 28 : 29 : 30 : 31 : }
        try:
            print lennyRepo[todaysDate.day]
            return lennyRepo[todaysDate.day]
    #End of lenny
    def outcome(self, dice, sides, eventString):
        pseudorandom = 0
        total = 0
        maximumNumber = sides * dice
        while pseudorandom < sides:
            total = total + random.randint(0, sides)
            pseudorandom = pseudorandom + 1
        if eventString == "-r":
            return total
        elif eventString == "-p":
            print(total)
            return True
        else:
            print(eventString + ":" + str(total) +  " out of " + str(maximumNumber) + ".")
            return eventString + ":" + str(total) +  " out of " + str(maximumNumber) + "."
    #End of outcome
    def __init__(self): 
        print("BrightBot V:0.1")
        print("Created by Matthew Weidenhamer")
        print("Last updated 9/21/2015")
    #End of __init__
BrightBot = TwitterBot()
BrightBot.loadQuotes("quotes.p")
while true: #Once the Twitter library is added, this will be where things actually happen.
    commandGet = "!outcome x, y, This is just a test."
    commandSender = "Ne Zha"
    commandGet = commandGet.lower()
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
    if commandOut == false:
        print("Oops! Something went wrong!")
    

