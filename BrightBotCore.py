import pickle
import sys
import datetime
import random
class TwitterBot(object):
    quotes =  {}
    polls = {}
    whois = {}
    rules = ""
    fakerules = ""
    whoisSaveFile = "/data/whois.p"
    quotesSaveFile = "/data/quotes.p"
    rulesSaveFile = "/config/rules.txt"
    fakeRulesSaveFile = "/config/fakerules.txt"
    currExp = {}
    iAm = "I am Brightbot. I am a chatroom robot framework originally created by Matthew Weidenhamer.\nCurrent version is 0.1 'It's Broken.' "
    commands = ["!bestof", "!lenny", "!outcome", "!poll", "!answer", "!stoppoll", "!mood", "!whoami", "!currentpolls", "!rules", "!fakerules", "!whois", "!remember", "!forget"]
    def emptyDictionary(self, dictionary, key):
        dictionary.pop(key, None)
    def toDo(self, command, sender):
        try:
            doThis, data = command.split(" ", 1)
            doThis = doThis.lower()
        except ValueError:
            doThis = command
            doThis = doThis.lower()
        if doThis == BrightBot.commands[0]: #Best Of
            action, person, response = data.split(" ", 2)
            action = action.lower()
            person = person.lower()
            response = response.lower()
            if action == "get":
                response = int(response)
                return self.getQuote(person, response, sender)
            elif action == "add":
                return self.addQuote(person, response)
            elif action == "delete":
                return self.delQuote(person, response)
            else:
                return "Unrecognized action, please check spelling."
        elif doThis == BrightBot.commands[1]: #Lenny
            return self.lenny()
        elif doThis == BrightBot.commands[2]: #Outcome
            x, y, event = data.split(" ", 2)
            return self.outcome(x, y, event)
        elif doThis == BrightBot.commands[3]: #Poll
            if data[0].lower() == "h":
                try:
                    question, answers = data.split("? ", 1)
                    return self.hardPoll(question, answers, sender)
                except ValueError:
                    return "Could not create poll! make sure you have at least one question mark at the end of your question!"
            elif data[0].lower == "s":
                placeHolder, actual = data.split("? ", 1)
                return self.softPoll(actual, sender)
            else:
                return False
        elif doThis == BrightBot.commands[4]: #Answer
            pollID, pollAns = data.split(" ", 1)
            return self.answer(pollID, pollAns)
        elif doThis == BrightBot.commands[5]: #Stop Poll
            return self.stopPolling(data, sender)
        elif doThis == BrightBot.commands[6]: #Moods
            return self.mood(data)
        elif doThis == BrightBot.commands[7]: #WhoAmI
            return self.iAm
        elif doThis == BrightBot.commands[8]: #Current Polls
            return "Current Polls:" + polls
        elif doThis == BrightBot.commands[9]: #Rules
            return BrightBot.rules()
        elif doThis == BrightBot.commands[10]: #Fake Rules
            return BrightBot.fakeRules()
        elif doThis == BrightBot.commands[11]: #Whois
            return self.whoIs()
        elif doThis == BrightBot.commands[12]: #Remember
            remWho, remWhat = data.split(" ", 1)
            return self.remember(remWho, remWhat)
        elif doThis == BrightBot.commands[13]: #Forget
            return self.forget(data)
        else:
            return "Unknown command."
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
                print("Could not find rules file! Making one instead...")
                f = open(self.rulesSaveFule, "w")
                print("New rules save file created.")
                f.close()
        except EOFError:
            print("The rules file is empty, no rules loaded :(")
        print("loadRules module finished.")
        print("Attempting to load rules from " + self.fakeRulesSaveFile)
        try:
            with open(self.fakeRulesSaveFile, "r") as myFile:
                self.fakeRules = myFile.read()
        except FileNotFoundError:
                print("Could not find fake rules file! Making one instead...")
                f = open(self.fakeRulesSaveFule, "w")
                print("New rules save file created.")
                f.close()
        except EOFError:
            print("The fake rules file is empty, no fake rules loaded :(")
        print("loadFakeRules module finished.")
    def saveQuotes(self):
        print("Attempting to save quotes to " + self.quotesSaveFile)
        f = open(self.quotesSaveFile, "wb")
        pickle.dump(self.quotes, f)
        f.close()
        print("Saved Successfuly.")
    def getQuote(self, person, number, sentRequest):
        print(sentRequest + " has requested quote number " + str(number) + " of " + person + ".")
        currentQuote = ""
        try:
            currentQuote = self.quotes[person][number - 1]
            print(currentQuote)
            return currentQuote
        except KeyError:
            print("Could not find person " + person + "! Returning False...")
            return False
        except IndexError:
            print("Could not find quote number " + number + " for " + person + "! Returning False...")
            return False
    def addQuote(self, person, quote):
        try:
            self.quotes[person].append(quote)
            self.saveQuotes()
            return True
        except KeyError:
            self.quotes[person] = [quote]
            self.saveQuotes()
            return True
    def delQuote(self, person, quote):
        try:
            del self.quotes[person][quote]
            self.saveQuotes()
            return True
        except KeyError:
            return False
        except IndexError:
            return False
    def lenny(self):
        return "!Lenny is still being tested! Cannot do this."
        #todaysDate = date.today() #Figure out why this line is breaking.
        #lennyRepo = {1 : "( ͡° ͜ʖ ͡,°)", 2 : "( ͠° ͟ʖ ͡°)", 3 : "ᕦ( ͡° ͜ʖ ͡°)ᕤ", 4 : "( ͡~ ͜ʖ ͡°)"}
        #print(lennyRepo[todaysDate.day])
        #return lennyRepo[todaysDate.day]
    def outcome(self, dice, sides, eventString):
        pseudorandom = 0
        total = 0
        sideNo = int(sides)
        diceNo = int(dice)
        maximumNumber = sideNo * diceNo
        while pseudorandom < diceNo:
            total = total + random.randint(1, sideNo)
            pseudorandom = pseudorandom + 1
        if eventString == "-r":
            return total
        elif eventString == "-p":
            print(total)
            return True
        else:
            print(eventString + ":" + str(total) +  " out of " + str(maximumNumber) + ".")
            return eventString + ":" + str(total) +  " out of " + str(maximumNumber) + "."
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
                        print("repeatNoAns: " + str(repeatNoAns))
                        if repeatNoAns == int(pollAns):
                            print("Success 2!")
                            self.polls[pushAnsTo][j] = self.polls[pushAnsTo][j]+ 1
                            return "Answer Recorded Successfully."
                    return "Failed!"
                elif i[4].lower() == "s":
                    self.polls[pushAnsTo].append(pollAns)
                    return "Answer Recorded Successfully."
                else:
                    return "Hi there"
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
        print("Chatroom name is now " + moodType)
        return "The room has been renamed successfully."
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
            del self.whois(who)
            return who + " has been forgotten."
        except KeyError:
            try: 
                dummyKey, dummySplit = who.split(" ", 1)
                del self.whois(dummyKey)
                return who + " has been forgotten."
            except KeyError:
                return "I don't know who " + who + " is!"
    def remember(self, who, what):
        self.whois[who] = what
        return "I'll remember that"
    def whoIs(self, who):
        try:
            return who + self.whois[who]
        except KeyError:
            try:
                dummyKey, dummySplit = who.split(" ", 1)
                return dummyKey + self.whois[dummyKey]
            except KeyError:
                return "I don't know either."
    def __init__(self): 
        print("BrightBot V:0.1")
        print("Created by Matthew Weidenhamer")
        print("Last updated 9/21/2015")
        self.loadFiles()
BrightBot = TwitterBot()
def testFunctionality(): #Once the Twitter library is added, this will be where things actually happen. Most print statements will be replaced with 
    commandGet = "!outcome 7 5 This is just a test."
    commandSender = "Ne Zha"
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
    #commandGet = "!bestOf add NeZha This is how I like to test my code!"
    #commandGet = commandGet.lower()
    #commandOut = BrightBot.toDo(commandGet, commandSender)
    #print(commandOut)
    commandGet = "!bestOf get NeZha 1"
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
    commandOut = BrightBot.toDo("!lenny", commandSender)
    print(commandOut)
    commandGet = "!poll H What's my favorite letter of the alphabet? Purple. Pink. Yellow."
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
    commandGet = "!answer 1 2"
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
    commandGet = "!stoppoll 1"
    commandSender = "Ne Zha"
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
    commandGet = "!currentpolls"
    commandOut = BrightBot.toDo(commandGet, commandSender)
    print(commandOut)
#Note to self: Possibly add a number value to the Dictionary Key to indicate the order in  which it was added?
testFunctionality()
