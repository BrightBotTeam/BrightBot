# BrightBot
The Bright Bot Twitter Bot, meant to recreate an IRCBot in a Twitter Chat Room. **UNDER DEVELOPMENT**
## Modules
# BestOf Module
Usage: !bestof (get/add/delete) [(person/random if get) (person if add/delete)] [(number if get/delete) ("Quote" if add)]\n
Ex. !bestof add Tom I like my men  like I like my beer. Not trying to sleep with me!
The BestOf module enables a persistant "quotes" feature that loads a dictionary of quotes from a file. These quotes are stored in  a dictionary called "quotes", each dictionary key symbolizes quotes from "Person". and each key corresponds to a list of the added quotes  
Visual: Quotes{"PersonName(key)" : ["Quote one", "Quote two"]}
Directly, it prints Quotes["PersonName(key)"][x - 1]
Calling Quotes PersonName 1 would return "Quote one", for example
The minus 1 is added because Python stores lists at values one less than displayed. Since this is intended for people who may not be computer savvy, this was addded for simplicity.
Calling a nonexistant person will create a file for that person. When a person has no more quotes, their key is deleted from the file and can no longer be called

# Lenny Module
Usage: !lenny
Ex. !lenny
Return a different "lenny" based on the current day of the month. 

# Outcome Module
Usage: !outcome x y ("Event String" or flag)
Essentially a glorified dice roll command, rolls x number of y sided dice, and prints out '"Event String" + total + highest possible total. TL:DR; generates x numbers between 0 and y, adds them together, and appends them to  "Event String"
Replacing "Event String" with the -r flag will instead **return** only total.
Replacing "Event String" with the -p flag will instead **print** only total.
