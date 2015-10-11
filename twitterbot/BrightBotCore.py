import pickle
import datetime
import random
from twitter import *
def importString(textFile):
    f = open(textFile, "r")
    returnme = f.read()
    f.close()
    return returnme
auth = OAuth(
    consumer_key=importString("consumerkey.txt"),
    consumer_secret=importString("consumersecret.txt"),
    token=importString("consumertoken.txt"),
    token_secret=importString("tokensecret.txt"),
)
token = importString("consumertoken.txt")
token_key = importString("tokensecret.txt")
con_secret = importString("consumersecret.txt")
con_secret_key = importString("consumerkey.txt")
class BrightBot(object):
    
    quotes =  {}
    polls = {}
    whois = {"Brightbot" : "is our lord and savior, the Brightest star of the heavens and the earth. Those who worship him shall find peace, and those who reject him, destruction."}
    rules = ""
    fakerules = ""
    whoisSaveFile = "whois.p"
    quotesSaveFile = "quotes.p"
    rulesSaveFile = "rules.txt"
    fakeRulesSaveFile = "fakerules.txt"
    eightBallSaveFile = "8ballquotes.txt"
    roomName = "Twitter Of The Gods"
    eightBallResponses = []
    currExp = {}
    iAm = "I am Brightbot, master of the chatroom, a bot framework originally created by Matthew Weidenhamer.\nCurrent version is 1.2 'It's Congealed' "
    commands = ["!bestof", "!lenny", "!outcome", "!poll", "!answer", "!stoppoll", "!mood", "!whoami", "!currentpolls", "!rules", "!fakerules", "!whois", "!rem", "!forget", "!reset", "!help", "!omagicconch", "!quote", "!forgetq"]
    def emptyDictionary(self, dictionary, key):
        dictionary.pop(key, None)
    def toDo(self, command, sender):
        try:
            doThis, data = command.split(" ", 1)
            doThis = doThis.lower()
        except ValueError:
            doThis = command
            data = False
            doThis = doThis.lower()
        if doThis == BrightBot.commands[0]: #Best Of
            try:
                return self.getQuote(data)
            except ValueError:
                return "Unrecognized action! Usage: bestof (person) #Quotenumber. "
        elif doThis == BrightBot.commands[1]: #Lenny
            return self.lenny()
        elif doThis == BrightBot.commands[2]: #Outcome
            try:
                x, y, event = data.split(" ", 2)
                return self.outcome(x, y, event)
            except UnboundLocalError or TypeError:
                return "Incorrect format! Usage: !outcome (number of sides), (number of dice), (Event String)"
        elif doThis == BrightBot.commands[3]: #Poll
            try:
                if data[0].lower() == "h":
                    try:
                        question, answers = data.split("? ", 1)
                        return self.hardPoll(question, answers, sender)
                    except ValueError or TypeError or ValueError:
                        return "Could not create poll! make sure you have at least one question mark at the end of your question!"
                elif data[0].lower == "s":
                    placeHolder, actual = data.split("? ", 1)
                    return self.softPoll(actual, sender)
            except UnboundLocalError or TypeError or ValueError:
                'Incorrect format! Usage: !poll (h/s), (Question)? [If h then add: , (answer 1). (answer 2). (etc)]'
        elif doThis == BrightBot.commands[4]: #Answer
            try:
                pollID, pollAns = data.split(" ", 1)
                return self.answer(pollID, pollAns)
            except UnboundLocalError or ValueError or TypeError:
                return "Incorrect format! Usage: !answer (pollID) (answer/answer identifier)"
        elif doThis == BrightBot.commands[5]: #Stop Poll
            try:
                return self.stopPolling(data, sender)
            except UnboundLocalError or ValueError:
                return "Incorrect format! Usage: !stoppoll (pollID)"
        elif doThis == BrightBot.commands[6]: #Moods
            try:
                return self.mood(data)
            except UnboundLocalError or ValueError:
                return "Incorrect Format! Usage: !mood (mood)"
        elif doThis == BrightBot.commands[7]: #WhoAmI
            return self.iAm
        elif doThis == BrightBot.commands[8]: #Current Polls
            return "Current polls: " + str(self.polls)
        elif doThis == BrightBot.commands[9]: #Rules
            return BrightBot.rules
        elif doThis == BrightBot.commands[10]: #Fake Rules
            return BrightBot.fakeRules
        elif doThis == BrightBot.commands[11]: #Whois
            try:
                return self.whoIs(data)
            except UnboundLocalError or ValueError or TypeError:
                return "Incorrect format! Usage: !whois (name)"
        elif doThis == BrightBot.commands[12]: #Remember
            try:
                remWho, remWhat = data.split(" ", 1)
                return  self.remember(remWho, remWhat)
            except UnboundLocalError or TypeError or ValueError or AttributeError:
                return "Incorrect Format! Usage: !rem (name) (what)"
        elif doThis == BrightBot.commands[13]: #Forget
            try:
                return self.forget(data)
            except UnboundLocalError or ValueError or TypeError:
                return "Incorrect format! Usage: !forget (who). See "
        elif doThis == BrightBot.commands[14]: #Reset
            return self.mood(roomName)
        elif doThis == BrightBot.commands[15]: #Help
            if data:
                if data.lower() == BrightBot.commands[0]:
                    return "Bestof is the command for getting quotes from people. Usage: !bestof [who] #Quotenumber. The # is required."
                elif data.lower() == BrightBot.commands[1]:
                    return "[UNDER CONSTRUCTION] !lenny is a command for getting a lenny face. Typing !lenny returns a lenny. Nuff said."
                elif data.lower() == BrightBot.commands[2]:
                    return "Outcome is a basic dicerolling application. Usage: !outcome (number of sides), (number of dice), (an additional string it will add on to the end)"
                elif data.lower() == BrightBot.commands[3]:
                    return "Poll is a polling command that can be used to ask a group a question and get anonymous responses. Use h to have a list of preset answers, or s to take anything as an answer. Usage: 'Incorrect format! Usage: !poll (h/s), (Question)?[If hard then add: , (answer 1). (answer 2). (etc)]'"
                elif data.lower() == BrightBot.commands[4]:
                    return "Answer is used to register your answer to a poll. Make sure to include a written answer for a soft poll (s), or the answer ID for a hard poll (h). Usage: !answer (pollID) (answer/answer identifier)"
                elif data.lower() == BrightBot.commands[5]:
                    return "StopPoll is used to stop polling. The poll is deleted from BrightBot's memory, and the results are given to you. PLEASE NOTE: You can only stop a poll if you started it. Usage: !stoppoll [pollid]"
                elif data.lower() == BrightBot.commands[6]:
                    return "[NOT AVAILABLE WITH CURRENT TWITTER DISTRIBUTION] !mood changes the name of the twitter conversation to the requested name."
                elif data.lower() == BrightBot.commands[7]:
                    return "!whoami lets me brag about myself a little bit."
                elif data.lower() == BrightBot.commands[8]:
                    return "CurrentPolls tells you about all the polls currently open."
                elif data.lower() == BrightBot.commands[9]:
                    return "Rules tells you about a provided list of rules."
                elif data.lower() == BrightBot.commands[10]:
                    return "FakeRules tells you about a preprovided list of fake rules."
                elif data.lower() == BrightBot.commands[11]:
                    return "Whois tells you what it knows about a person. To modify these, try !rem or !forget. Usage: !whois (name)"
                elif data.lower() == BrightBot.commands[12]:
                    return "Remember defines what BrightBot will remember about a person. Unlike quotes, if there is already an entry for !rem, it will be overwritten. Usage: !rem person *What to remember. The * is required."
                elif data.lower() == BrightBot.commands[13]:
                    return "Forget forgets about a person. Do note this affects !whois, and not quotes. Usage: !forget (person)"
                elif data.lower() == BrightBot.commands[14]:
                    return "[UNDER CONSTRUCTION] !reset returns the mood to what it originally was."
                elif data.lower() == BrightBot.commands[15]:
                    return "!help helps. Whodathunkit."
                elif data.lower() == BrightBot.commands[16]:
                    return "OMagicConch is a magic 8 ball, and returns as such. Usage: !omagicconch (question)"
                elif data.lower() == BrightBot.commands[17]:
                    return "Quote adds a quote for a person to the dictionary of quotes. Usage: !quote (person} *Quote. The star is required."
                elif data.lower() == BrightBot.commands[18]:
                    return "ForgetQuote forgets a certain quote from a person. Usage: !forgetq (who) #QuoteNumber"
            else:
                return "Available commands: " + str(self.commands)
                
        elif doThis == BrightBot.commands[16]: #OMagicConch
            try:
                return self.eightBall(data)
            except UnboundLocalError:
                return "Incorrect Format! Usage: !OMightConch (question)"
        elif doThis == BrightBot.commands[17]: #Quote
            try:
                self.addQuote(data)
            except ValueError or TypeError or UnboundLocalError:
                return "Incorrect format! Usage: !quote (who) #(quote number)"
        elif doThis == BrightBot.commands[18]: #ForgetQuote
            try:
                self.delQuote(data)
            except ValueError or TypeError or UnboundLocalError:
                return "Incorrect format! Usage: !forgetq (who) #(quote number)"
        else:
            return "Unknown command. Type !help for a list of commands, or !help (command) for a detailed look at a command."
    def loadFiles(self):
        print("Attempting to load quotes from " + self.quotesSaveFile)
        try:
            f = open(self.quotesSaveFile, "rb")
            self.quotes = pickle.load(f)
            print("Loaded quotes from " + str(len(self.quotes)) + " different people!")
        except FileNotFoundError:
                print("Could not find quotes file! Making one instead...")
                f = open(self.quotesSaveFile, "wb")
                print("New save file created.")
                f.close()
        except EOFError:
            print("The quotes file is empty, no quotes loaded :(")
        print("loadQuotes module finished.")
        print("Attempting to load whois from " + self.whoisSaveFile)
        try:
            f = open(self.whoisSaveFile, "rb")
            self.whois = pickle.load(f)
            print("Loaded whois info from " + str(len(self.whois.keys())) + " different people!")
        except FileNotFoundError:
                print("Could not find a whois file! Making one instead...")
                f = open(self.whoisSaveFile, "wb")
                print("New save file created.")
                f.close()
        except EOFError:
            print("The whois file is empty, no info loaded :(")
        print("loadwhois module finished.")
        print("Attempting to load rules from " + self.rulesSaveFile)
        try:
            with open(self.rulesSaveFile, "r") as myFile:
                self.rules = myFile.read()
        except FileNotFoundError:
                print("Could not find rules file! Calling !rules will crash the program now.")
        except EOFError:
            print("The rules file is empty, no rules loaded :(")
        print("loadRules module finished.")
        print("Attempting to load fake rules from " + self.fakeRulesSaveFile)
        try:
            with open(self.fakeRulesSaveFile, "r") as myFile:
                self.fakeRules = myFile.read()
        except FileNotFoundError:
                print("Could not find fake rules file! Calling !rules will crash the program now.")
        except EOFError:
            print("The fake rules file is empty, no fake rules loaded :(")
        print("loadFakeRules module finished.")
        print("Attempting to load 8ball quotes from " + self.eightBallSaveFile)
        try:
            with open(self.eightBallSaveFile, "r") as myFile:
                for i in myFile:
                    self.eightBallResponses.append(i);
        except FileNotFoundError:
                print("Could not find 8ball quotes file! Making one instead...")
                f = open(self.eightBallSaveFile, "w")
                print("New rules save file created.")
                f.close()
        except EOFError:
            print("The 8ball file is empty, no fake rules loaded :(")
        print("load8ball module finished.")
    def saveQuotes(self):
        print("Attempting to save quotes to " + self.quotesSaveFile)
        f = open(self.quotesSaveFile, "wb")
        pickle.dump(self.quotes, f)
        f.close()
        print("Saved Successfuly.")
    def getQuote(self, data):
        person, number = data.split("#", 1)
        try:
            print("Requested quote number " + str(number) + " of " + person + ".")
            currentQuote = self.quotes[person][int(number) - 1]
            print(currentQuote)
            return "Quote " + str(number) + " of " + str(len(self.quotes[person])) + ": " + currentQuote
        except KeyError:
            return "I don't know who " + person + " is!"
        except IndexError:
            return "Could not find quote number " + str(number) + " for " + person + "!"
    def addQuote(self, data):
        person, quote = data.split("*", 1)
        try:
            self.quotes[person].append(quote)
            self.saveQuotes()
            return "Quote saved successfully."
        except KeyError:
            print("Creating new quote dictionary for " + person)
            self.quotes[person] = [quote]
            self.saveQuotes()
            return "Quote saved successfully."
    def delQuote(self, data):
        person, quote = data.split("#", 1)
        try:
            del self.quotes[person][int(quote)]
            self.saveQuotes()
            return "Quote forgotten."
        except KeyError:
            return "Could not find the person!"
        except IndexError:
            return "Could not find that quote!"
    def lenny(self):
        return "!Lenny is still in development! Try again later."
        #todaysDate = date.today() #Figure out why this line is breaking.
    def outcome(self, sides, dice, eventString):
        diceCounter = 0
        total = 0
        sideNo = int(sides)
        diceNo = int(dice)
        maximumNumber = sideNo * diceNo
        while diceCounter < diceNo:
            total = total + int(random.randint(1, sideNo))
            diceCounter = diceCounter + 1
        else:
            return eventString + ": " + str(total) +  " out of " + str(maximumNumber) + "."
    def answer(self, pollID, pollAns):
        print(self.polls)
        pollNames = list(self.polls.keys())
        print(pollNames)
        repeatNo = 0
        repeatNoAns = 0
        for i in pollNames:
            print(i)
            repeatNo = repeatNo + 1
            if repeatNo == int(pollID):
                pushAnsTo = i
                if i[4].lower() == "h":
                    for j in self.polls[i]:
                        repeatNoAns = repeatNoAns + 1
                        if repeatNoAns == int(pollAns):
                            self.polls[pushAnsTo][j] = self.polls[pushAnsTo][j]+ 1
                            return "Answer Recorded Successfully."
                    return "Failed!"
                elif i[4].lower() == "s":
                    self.polls[pushAnsTo].append(pollAns)
                    return "Answer Recorded Successfully."
                else:
                    return "Something went wrong"
        return "Could not find a poll with that ID!"
    def softPoll(self, ques, sender):
        if data[0] == "S":
            oldData, newPollStuff = ques.split("S", 1)
        elif data[0] == "s":
            oldData, newPollStuff = ques.split("s", 1)
        else:
            return "Something went wrong!"
        newPollName = str(len(self.polls)+1) + ". (S) " + ques + "###" + sender
        self.polls[newPollName] = []
        self.decNewPoll(newPollName)
        return "Poll created successfully."
    def hardPoll(self, ques, ans, sender):
        if ques[0] == "H":
            oldData, newPollStuff = ques.split("H ", 1)
        elif ques[0] == "h":
            oldData, newPollStuff = ques.split("h ", 1)
        else:
            return "Something went wrong!"
        newPollName = str(len(self.polls)+1) + ". (H) " + newPollStuff + "###" + sender
        self.polls[newPollName] = {}
        ansRepo = ans
        while len(ansRepo) > 1:
            try:
                curAns, ansRepo = ansRepo.split(". ", 1)
                self.polls[newPollName][curAns] = 0
            except ValueError:
                curAns, ansRepo = ansRepo.split(".", 1)
                self.polls[newPollName][curAns] = 0
        self.decNewPoll(newPollName)
        return "Poll created successfully."
    def decNewPoll(self, pollKey):
        pID, pollRest = pollKey.split(". ", 1)
        pQues, pAsker = pollKey.split("###", 1)
        ansLength = 1
        if pQues[4] == "H":
            print(pAsker + " has created a new hard poll (ID " + pID + "): " + pQues + "?")
            for i in self.polls[pollKey]:
                print("Answer " + str(ansLength) + ": " + i )
                ansLength = ansLength + 1
        else:
            print(pAsker + " has created a new poll (ID " + pID + "): " + pQues + "?")

        print("Type !answer, followed by your answer or answer ID to reply!")
    def mood(self, moodType):
        return "Mood functionality is currently not available, due to Twitter API constraints."
        #print("Chatroom name is now " + moodType)
        #return "The room has been renamed successfully."
    def stopPolling(self, pollID, sender):
        for i in self.polls:
            if i[0] == pollID:
                pollName, pollUser = i.split("###")
                if pollUser == sender:
                    for j in self.currExp:
                        del j
                    print("Authenticated. Stopping poll and returning information...")
                    for j in self.polls[i]:
                        self.currExp[j] = j
                        if i[4].lower() == "h":
                            self.currExp[j] = self.polls[i][j]
                    del self.polls[i]
                    return "Final results: " + str(self.currExp)
                else:
                    return "You did not create that poll!"
    def saveWhois(self):
        print("Attempting to save whois to " + self.whoisSaveFile)
        f = open(self.whoisSaveFile, "wb")
        pickle.dump(self.whois, f)
        f.close()
        print("Saved Successfuly.")

    def forget(self, who):
        try:
            del self.whois[who]
            return who + " has been forgotten."
        except KeyError:
            try: 
                dummyKey, dummySplit = who.split(" ", 1)
                del self.whois[dummyKey]
                return who + " has been forgotten."
            except KeyError:
                return "I don't know who " + who + " is!"
    def remember(self, who, what):
        self.whois[who] = what
        self.saveWhois()
        return "I'll remember that"

        
    def whoIs(self, who):
        try:
            return who + " " + self.whois[who]
        except KeyError:
            try:
                dummyKey, dummySplit = who.split(" ", 1)
                return dummyKey + " " + self.whois[dummyKey]
            except KeyError:
                return "I don't know either. (Make sure they are submitted via !rem first!)"
            except ValueError:
                return "I don't know either. (Make sure they are submitted via !rem first!)"
    def eightBall(self, question):
        result = random.randint(1, len(self.eightBallResponses))
        return self.eightBallResponses[result]
    def __init__(self): 
        print("BrightBot V:1.2")
        print("Created by Matthew Weidenhamer")
        print("Last updated 10/5/2015")
        self.loadFiles()
Maelyn = BrightBot()
t = Twitter(
    auth=auth, retry = True)
print("Finished starting bot.")
testFunctionality()
twitter_userstream = TwitterStream(auth=auth, domain='userstream.twitter.com')
while(True):
    for msg in twitter_userstream.user():
        if 'direct_message' in msg:
            if(msg['direct_message']['sender']['screen_name'] != "BrightOfTheSCP" and msg['direct_message']["text"][0] == "!"):
                print("Message recieved from " + msg['direct_message']['sender']['screen_name'] + ": " + msg['direct_message']["text"])
                t.direct_messages.new(screen_name = msg['direct_message']['sender']['screen_name'], user_id = msg['direct_message']['sender']['id'], text = Maelyn.toDo(msg['direct_message']["text"], msg['direct_message']['sender']['name']))
