# QUESTION. 순열 확인
# 문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라. 

# O(N)
from collections import Counter
def is_permutation(string1, string2):
  if len(string1) != len(string2):
    return False

  char_cnt = Counter()
  for s in string1:
    char_cnt[s] += 1

  for s in string2:
    if char_cnt[s] == 0:
      return False
    char_cnt[s] -= 1
  return True
    
