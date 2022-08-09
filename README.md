Ok what is the Lietner system and how does it improove memorization skills?

1. create a deck of flashcards (array of question/answer linked)
2. create 3 boxes (variable number of boxes?)
3. start each card in Box 1

4. Each box carries with it a time-weight value, which determines the frequency of times a card will be shown to the user.
	e.g (Box1: EveryDay, Box2: everyOtherDay, Box3: onceAWeek)

5. Move cards to LOWER Box catagory if answered incorrectly, Move cards to HIGHER Box catagory if answered correctly.

6. variables to play around with - numBoxes: int, timePerBox: list 
	timePerBox could be a values array where len(values) == numBoxes or a generator function?  


----


Lets store the data in its simplist form, and then build the Class out based on the dict key, value pairs.
store with metadata that can be used to sort/filter the questions (subject, uuid, boxNum, last_asked)

Dump from class where class structure looks something like -- pool: remaining questions unused for this study session, boxes: list of all boxes with list of question/answer pairs in each box)


FIRST DATASET TO MAKE:
	make a list of all the built-in data types and all the valid functions that can be called on them e.g. (str.replace(), list.append())
	make every possible combination of valid and invalid pairings.


	maybe some sort of gui to show a code snippet and ask if valid or invalid?
	maybe some way of having {arg1}.{arg2} = {arg3} and having the card show us 2/3 and ask for the 3rd?
	
	break down into TYPES (int, str, float), FUNCTIONS (reverse(), upper(), zip()), METHODS (.isupper(), .sort(), .append())
	try combinations of these and store the results, randomize which 2/3 that will be displayed and which will be the answer, 
	format and display, user answers, and result (corrent or incorrect) will move that concept card into the appropriate next box.

	FUNCTION(TYPE) = ANS or TYPE.METHOD = ANS

	then do this for other libraries (os, re, itertools, collections, numpy, and more)

How hard could that be right?

