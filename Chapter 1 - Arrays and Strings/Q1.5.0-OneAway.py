"""There are three types of edits that can be performed on a string:
insert a character, remove a character, or replace a character.
Given two strings, write a function to check if they are one edit
(or zero edits) away."""

#Edit Distance (Levenahtein Distance)

#Examples:
#Pale, Pie -> false
#Pales, Pale -> true
#Pale, Bale -> true
#Pale, Bake -> false

def levenshtein(w1, w2):
	if len(w1) == 0: return len(w2)
	if len(w2) == 0: return len(w1)
	if w1[-1] == w2[-1]:
		cost = 0
	else:
		cost = 1

	return min([
		levenshtein(w1[0:len(w1)-1], w2) + 1,
		levenshtein(w1, w2[0:len(w2)-1]) + 1,
		levenshtein(w1[0:len(w1)-1], w2[0:len(w2)-1]) + cost
		])

