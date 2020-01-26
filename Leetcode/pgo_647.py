# 647. Palindromic Substrings

# Input: 
#s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".

# Input:
#s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

# Input:
#s = "fdsklf"
# Output: 6

# Input:
#s = "aba"
# Output: 4

# input :
#s= "leetcode"
# output: 9

s = list(s)
sl = len(s)
centre = 2*sl -1
ans = 0

for c in range(centre):
    l = int(c /2) 
    r = int(l + c %2)
    while l >= 0 and r < sl and s[l] == s[r]:
        ans += 1
        l -= 1
        r += 1

print(ans)
