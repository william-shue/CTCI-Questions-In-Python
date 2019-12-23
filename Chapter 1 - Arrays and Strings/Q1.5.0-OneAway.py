"""There are three types of eddits that can be performed on a string:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away."""

#Examples:
#Pale, Pie -> false
#Pales, Pale -> true
#Pales, Bale -> true
#Pale, Bake -> false


def strCompare(w1, w2):

	lw1 = len(w1)
	lw2 = len(w2)

	if w1 == w2: print ("true")
	

w1 = "Apple"
w2 = "appleee"

strCompare(w1.lower(), w2.lower())






