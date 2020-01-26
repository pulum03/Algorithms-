# 171. Excel Sheet Column Number
#s = "A"
#output = 1

#s = "AB"
#output = 28

s = "ZY"
#output = 701

# for i in s:
#     print(ord(i)-64)
    
sum = 0

for i in s:
    sum = sum*26 + ord(i)-64
    print(sum)
    
    
