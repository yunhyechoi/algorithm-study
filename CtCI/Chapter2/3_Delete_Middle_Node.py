
def delete_middle(node):
  node.value = node.next.value
  node.next = node.next.next
  return node
