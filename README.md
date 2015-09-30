# BrightBot
The Bright Bot Twitter Bot, meant to recreate an IRCBot in a Twitter Chat Room. **UNDER DEVELOPMENT**

# Modules
##BestOf Module
Usage: !bestof (get/add/delete) [(person/random if get) (person if add/delete)] [(number if get/delete) ("Quote" if add)]

Ex. !bestof add Tom I like my men like I like my beer. Not trying to sleep with me!

The BestOf module enables a persistant "quotes" feature that loads a dictionary of quotes from a file. These quotes are stored in  a dictionary called "quotes", each dictionary key symbolizes quotes from "Person". and each key corresponds to a list of the added quotes.

Visual disambaguation: Quotes{"PersonName(key)" : ["Quote one", "Quote two"]}. Directly, it prints Quotes["PersonName(key)"][x - 1]. Calling Quotes PersonName 1 would return "Quote one", for example.

The minus 1 is added because Python stores lists at values one less than displayed. Since this is intended for people who may not be computer savvy, this was added for simplicity's sake.

When a person has no more quotes, their key is deleted from the file and can no longer be called until it is recreated by adding more quotes to them.

# Lenny Module
Usage: !lenny
Ex. !lenny
Return a different "lenny" based on the current day of the month. It's that simple

# Outcome Module
Usage: !outcome x, y, ("Event String" or flag),
Essentially a glorified dice roll command, rolls x number of y sided dice, and prints out '"Event String" + total + highest possible total. TL:DR; generates x numbers between 0 and y, adds them together, and appends them to  "Event String"
Replacing "Event String" with the -r flag will instead **return** only total.
Replacing "Event String" with the -p flag will instead **print** only total.

# Poll module
Create usage: !poll (hard/soft), (Question)[If hard then, (answer 1), (answer 2), (etc)]
Reply usage: !answer (poll id) (Answer string if soft poll, answer number if hard poll)
Stop usage: !stopPoll (poll id)
A quick and dirty way of polling a group chat. SoftPoll takes any string as an answer, while HardPoll takes a number corresponding to a predetermined set of answers. After completion, the results can be exported to a .txt document, which can be linked to by the bot, or can be returned. Set to be anonymous, may be edited to add an option to make it possible to get direct user replies.

You can only stop a poll if you created it.

# Moods module
Usage: !mood (mood)

Changes the name of the chat to an appropriate mood setting. !reset can also be called to return it to whatever the default Chat setting was. 

# Who Am I module
Usage: !whoami

Returns a quick little message about the history of brightbot

# Rules Module
Usage: !rules OR !fakerules

Returns a little list of rules that you can set in the rules.txt file. !fakerules returns a list of rules you can set in the fakerules.txt file. 
