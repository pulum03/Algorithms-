#10보다 작은 자연수 중에서 3 또는 5의 배수는 3, 5, 6, 9 이고,
#이것을 모두 더하면 23입니다.
#1000보다 작은 자연수 중에서 3 또는 5의 배수를 모두 더하면 얼마일까요?

def sumMultiOf3And5(n):
    result = 0  #Ini
    i = 1
    while i < n:
        if i % 3 == 0 or i % 5 == 0:
            result += i
        i += 1
    return result

print(sumMultiOf3And5(1000))
