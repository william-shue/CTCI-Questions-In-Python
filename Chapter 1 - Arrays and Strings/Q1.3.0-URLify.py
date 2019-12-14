
str = input("Enter String: ")

res = []
counter = 0; i = 0; j = 1

while (len(str) > counter):

        if (str[i:j] == " "): res.append("%20")
        else: res.append(str[i:j])
        i+=1; j+=1; counter+=1

str = ""
for x in res:
        str = str + x
print (str)


