class Node:
  
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def post_order_traversal(root):

  if root:
    post_order_traversal(root.left)
    post_order_traversal(root.right)
    print(root.data, end=" ")


root = Node("Siblings")
root.left = Node("Wanja")
root.right = Node("Akama")
root.left.left = Node("Valerie")
root.left.right = Node("Moraa")
root.right.right = Node("Tom")
root.right.left = Node("Okeya")

post_order_traversal(root)
