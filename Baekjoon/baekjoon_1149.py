#3          집 수
#26 40 83   빨강 비용
#49 60 57   초록 비용
#13 89 99   파랑 비용

# 96

n = int(input())

hc = []

for i in range(n):
    hc.append(list(map(int,input().split())))

    dp = [hc[0]]

print(hc)
print(dp)

for i in range(1, n):
    cc = []

    red = min(dp[i-1][1], dp[i-1][2]) # 0
    cc.append(red + hc[i][0])
    
    green = min(dp[i-1][0], dp[i-1][2]) # 1 
    cc.append(green + hc[i][1])
    
    blue = min(dp[i-1][0], dp[i-1][1]) # 2
    cc.append(blue + hc[i][2])

    dp.append(cc)

print(min(dp[n-1]))