# Question. 빗물 트래핑
# 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

height = [0,1,0,2,1,0,1,3,2,1,2,1]

# 투포인터 이용
# O(n)
def trap(height):
  left, right = 0, len(height)-1
  left_max, right_max = height[left], height[right]
  volume = 0
  while left <= right:
    left_max, right_max = max(left_max, height[left]), max(right_max, height[right])
    if left_max <= right_max:
      volume += left_max-height[left]
      left += 1
    else:
      volume += right_max-height[right]
      right -= 1
  return volume
