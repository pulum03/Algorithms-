# 백준 4344
scores = int(input())

ans = []

for i in range(scores):
  stu = list(map(int, input().split()))
  avg = sum(stu[1:]) / stu[0]
  
  tmp = []
  
  for i in stu[1:]:
    if i > avg:
      tmp.append(i)
  
  ans.append('%0.3f'%round(len(tmp)/stu[0]*100), 3)

for i in ans:
  print('%s%%'%i)