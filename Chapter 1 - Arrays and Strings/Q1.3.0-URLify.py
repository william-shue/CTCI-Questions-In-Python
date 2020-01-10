"""Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end
to hold the additional characters, and that you are given the 
"true" length of the string."""

#Example:
# Input: 'Mr John Smith     ". 13
# Output: 'Mr%20John%20Smith"

def URLify(str):

	res = []
	counter = 0; i = 0; j = 1

	while len(str) > counter:

        	if str[i:j] == " ": res.append("%20")
        	else: res.append(str[i:j])
        	i+=1; j+=1; counter+=1

	str = ""
	for x in res:
        	str = str + x
	return (str)

#Test cases
example = [
	"He knows very well how to deceive people.",
	"It's one of my favorite books.",
	"I never thought I'd be busy.",
	"He took his way to the country."]

for x in example:
	print (URLify(x))
