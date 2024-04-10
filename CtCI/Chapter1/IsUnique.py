# QUESTION. 중복이 없는가
# 문자열이 주어졌을 때, 이  문자열 에같은 문자가 중복되어 등장하는지 확인하는 알고리즘을 작성하라. 자료구조를 추가로 사용하지 않고 풀 수 있는 알고리즘 또한 고민하라.

# O(N)
def unique(string):
  if len(string) > 128:
    return False

  char_set = [False for _ in range(len(string))]
  for s in string:
    val = ord(s)
    if char_set[val] :
      return False
    char_set[val] = True 

  return True


# O(N^2)
def unique2(string):
  if len(string) > 128:
    return False

  for i in range(len(string)):
    for j in range(i+1, len(string)):
      if string[i] == string[j]:
        return False

  return True

