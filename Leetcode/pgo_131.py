# 131. palindrome partitioning
s = "aabaaabcba"

# output =
#  [
#    ["aa","b"],
#    ["a","a","b"]
#  ]
def partition(s):
        if not s:
            return [[]]
        
        result = []
        
        for i in range(len(s)):
            if isPalindrome(s[ : i+1]):
                print(partition(s[i+1 : ]))
                for r in partition(s[i+1 : ]):
#                     print(r)
                    result.append([s[ : i+1]] + r)
        return result

def isPalindrome(s):
        return s == s[::-1]