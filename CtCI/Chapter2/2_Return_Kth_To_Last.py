# Question. 뒤에서 k번째 원소 구하기
# 단방향 연결리스트가 주어졌을 때 뒤에서 k번째 원소를 찾는 알고리즘을 구현하라.

def kth_last_recursive(ll, k):
  head = ll.head
  cnt = 0
  
  def recursive(head, k):
    nonlocal cnt 
    
    if not head:
      return None
    current = recursive(head.next)
    cnt += 1

    if cnt == k:
      return head
    return current
  return recursive(head,k)
