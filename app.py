original = "abaa aab aaanbbb"
# original = "abaaaabaaanbbb"
# original = input("Ingresa texto original: ")

# regex = "aba* + bbb*"
regex = "aba"
# regex = input("Ingresa regex: ")

replace = "ccc"
# replace = input("Ingresa texto por remplazar: ")

def cleanRegex(regex):
    regex = regex.split("+")
    regex = [i.replace(" ", "") for i in regex if "*" in i]
    # regex = [i.replace(" ", "") for i in regex ]
    # print(regex)

    regexClean = []
    for i in regex:
        tmp = []
        index = i.index("*") - 1 
        tmp.append(i[:index]) #RegexStr without "*"
        tmp.append(i[index]) #Char to operate
        tmp.append(len(tmp[0]))
        regexClean.append(tmp) #Len of RegexStr
    # print("RegexClean: ",regexClean)
    return regexClean

def sed(original, regex, replace):
    regex = cleanRegex(regex)
    # print(regex)
    # print("Original:", original)
    for i in range(len(regex)):
        while True: # While there are patterns that match
            start = original.find(regex[i][0]) 
            if start == -1:
                break
            current = start+regex[0][2]
    
            while original[current] == regex[i][1] and current: #While there are more characters to replace
                current += 1
                if current == len(original) :
                    break
            original = original.replace(original[start:current],replace)
    return original

print(sed(original,regex,replace))