# 581. Shortest Unsorted Continuous Subarray
#num = [2, 6, 4, 8, 10, 9, 15]
# output = 5
snums = sorted(nums)
idx = []
if nums == snums:
    return 0
for i in range(len(nums)):
    if snums[i] != nums[i]: # sorted nums 와 nums 비교
        idx.append(i)
return idx[-1]-idx[0]+1  # idx list중에서 최소인덱스에서 최대인덱스까지