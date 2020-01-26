def quick_selection(arr, kth):
    pivot = arr[(len(arr)+1)//2 - 1] # choose middle value in array
    print('pivot: ',pivot)
    left, mid, right = [], [], []
    for i in range(len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
            print('left: ', left)
        elif arr[i] > pivot:
            right.append(arr[i])
            print('right: ', right)
        else:
            mid.append(arr[i])
            print('mid: ', mid)
    
    if kth < len(left):
        return quick_selection(left, kth)

    elif kth < len(left) + len(mid):
        return mid[0]
        
    else:
        return quick_selection(right, kth - len(left) - len(mid))


def getMedian(a):
  a_len = len(a)                # 배열 요소들의 전체 개수 구하기
  if (a_len == 0): return None  # 빈 배열은 에러 반환
  a_center = int(a_len / 2)     # 요소 개수의 절반값 구하기

  if (a_len % 2 == 1):   # 요소 개수가 홀수면
    return a[a_center]   # 홀수 개수인 배열에서는 중간 요소를 그대로 반환
  else:
    return (a[a_center - 1] + a[a_center]) / 2.0 # 짝수 개 요소는, 중간 두 수의 평균 반환

   
arr = [3, 5, 1, 2, 9, 6, 4, 7, 5, 6, 1, 5, 6, 7, 8, 9,12,22,1,2,3,4,5,33,44,55,66,77]
print(quick_selection(arr, len(arr)/2))

arr.sort()
print(getMedian(arr))