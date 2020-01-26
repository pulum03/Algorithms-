from collections import Counter

T = int(input())

res = []

for _ in range(T):
  N = input()
  
  num = [s for s in n]
  
  notebook = Counter(num)
  
  count = 0

  for n,c in notebook.items():
    if c%2==1: 
      count+=1
  
  res.append(count)

for i in range(1,T+1):
    print(res[i-1])