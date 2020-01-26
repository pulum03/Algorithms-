#451. Sort Characters By Frequency

# Given a string, sort it in decreasing order based on the frequency of characters.
#Input:
#s = "tree"

#Output:
#"eert"

#Input:
#s = "cccaaa"

#Output:
#"cccaaa"

#Input:
#s = "Aabb"

#Output:
#"bbAa"

#Input:
#s= "raaeaedere"

#Output:
#eeeeaaarrd"
import operator
sl = list(s)
sd = dict()

for i in sl:
    if i in sd:
        sd[i] = sd[i] + 1
    else:
        sd[i] = 1

sortedSd = sorted(sd.items(), key=operator.itemgetter(1), reverse = True)
result = ''

for item in sortedSd:
    result += item[0]*item[1]
    
print(result)