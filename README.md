# BrightBot
An IRCBot infrastructure, the current project is meant to recreate an IRCBot in a Twitter Chat Room. **UNDER DEVELOPMENT**

NOTE: All files here must be placed in the same folder. Additionally, the Python Twitter Tools API folder is required, found here: https://github.com/sixohsix/twitter/tree/master/twitter

# Features:
##BestOf
Usage: !bestof (get/add/delete) [(person/random if get) (person if add/delete)] [(number if get/delete) ("Quote" if add)]

Ex. !bestof add Tom I like my men like I like my beer. Not trying to sleep with me!

The BestOf module enables a persistant "quotes" feature that loads a dictionary of quotes from a file. These quotes are stored in  a dictionary called "quotes", each dictionary key symbolizes quotes from "Person". and each key corresponds to a list of the added quotes.

Visual disambaguation: Quotes{"PersonName(key)" : ["Quote one", "Quote two"]}. Directly, it prints Quotes["PersonName(key)"][x - 1]. Calling Quotes PersonName 1 would return "Quote one", for example.

The minus 1 is added because Python stores lists at values one less than displayed. Since this is intended for people who may not be computer savvy, this was added for simplicity's sake.

##Lenny
Usage: !lenny

Ex. !lenny

Return a different "lenny" based on the current day of the month. It's that simple

## Outcome
Usage: !outcome x, y, ("Event String" or flag)

Essentially a glorified dice roll command, rolls y number of x sided dice, and prints out '"Event String" + total + highest possible total. TL:DR; generates y numbers between 0 and x, adds them together, and appends them to  "Event String"

Replacing "Event String" with the -r flag will instead **return** only total.
Replacing "Event String" with the -p flag will instead **print** only total.

## Poll
Usage: !poll (hard/soft), (Question)?[If hard then add: , (answer 1). (answer 2). (etc)]

!answer (poll id) (Answer string if soft poll, answer number if hard poll)

!stopPoll (poll id)

A quick and dirty way of polling a group chat. SoftPoll takes any string as an answer, while HardPoll takes a number
corresponding to a predetermined set of answers. After completion, the results are returned, which can be linked to 
by the bot, for example. 

Set to be anonymous, may be edited to add an option to make it possible to get direct user replies. You can only stop a poll
if you created it.

There are 2 restrictions to this due to the formatting of the file. You may only have one question mark in your poll 
question for hard polls, and may not have 3 Number signs (###) consecutively at any place in the  file.

Polls are not persistant, restarting the bot will delete any active polls, and their data.

## Moods
Usage: 

!mood (mood)

!reset

Changes the name of the chat to an appropriate mood setting. !reset can also be called to return it to whatever the default
Chat name was. 

## Who Am I
Usage: !whoami

Returns a quick little message about your version of brightbot

# Rules 
Usage: !rules OR !jokerules

Returns a little list of rules that you can set in the rules.txt file. !fakerules returns a list of joke rules (or regular rules, whatever you want) that )you can set in the fakerules.txt file. 

## WhoIs
Usage: 

!whois (name)

!remember (name) (define)

!forget

Similar to the quotes command, but essentially provides a "universal quote" for each individual. Once again, this is stored by default in "whois.p", but can be changed by modifying the code. 

## OMightyConch

Usage: !OMightyConch (question)

A magic 8 ball.

## Help

Usage: !help

Shows all possible commands that can be run by BrightBot.

## Reboot

Usage: !reboot

Restarts the bot. Can only be run by the specified admin account.

# What is  planned for this bot:

Make the robot multi-file, divide up into commands list, config, command functions, etc

Add a configuration file to change the the name of the files loaded by the robot.

# Objectives to be added before next release:

Bugtesting

# Version history:

0.1: The initial robot. Simple and stupid.

0.2: The first working version. Takes a preordered list of commands and runs them one at a time. 

1.0: The first version that can be run as an actual bot from Twitter. It's probably terribly broken

1.1: Fixed crashing if you passed the wrong length command for a command. Will now return the proper command after crashing
