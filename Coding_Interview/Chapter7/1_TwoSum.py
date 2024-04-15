# Qestion. 두수의 합
# 덧셈하여 타겟읆 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라.

nums = [2,7,11,15]
target = 9

# 첫번째 수를 뺀 결과 키 조회 
# O(n)
def twoSum(nums, target):
  nums_map = {}

  for i, num in enumerate(nums):
    nums_map[num] = i

  for i, num in enumerate(nums):
    if target-num in nums_map and i != nums_map[target-num]:
      return [i, nums_map[target-num]]
