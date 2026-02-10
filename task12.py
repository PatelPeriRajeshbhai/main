#Best Search Alogorithm
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
      self.root = self._insert(self.root, value)

    def _insert(self, node, value):  
      if node is None:
        return Node(value)

      if value < node.value:
        node.left = self._insert(node.left, value)
      else:
        node.right = self._insert(node.right, value)

      return node

        
    def search(self, value):
      return self._search(self.root, value)

    def _search(self, node, value):
     if node is None:
        return False
     if node.value == value:
        return True
     elif value < node.value:
        return self._search(node.left, value)
     else:
        return self._search(node.right, value)

            
    def delete(self, value):
      self.root = self._delete(self.root, value)

    def _delete(self, node, value):
      if node is None:
        return None

      if value < node.value:
        node.left = self._delete(node.left, value)

      elif value > node.value:
        node.right = self._delete(node.right, value)

      else:  
        if node.left is None:
            return node.right
        if node.right is None:
            return node.left

        min_node = self._min(node.right)
        node.value = min_node.value
        node.right = self._delete(node.right, min_node.value)

      return node

          
    def inorder(self):
      self._inorder(self.root)
    print()

    def _inorder(self, node): #(Left, Root, Right)
     if node:
        self._inorder(node.left)
        print(node.value, end=" ")
        self._inorder(node.right)

        
    def preorder(self): #(Root, Left, Right)
        self._preorder(self.root)
        print()

    def _preorder(self, node):
     if node:
        print(node.value, end=" ")
        self._preorder(node.left)
        self._preorder(node.right)

            
    def postorder(self): #(Left, Right, Root)
     self._postorder(self.root)
    print()

    def _postorder(self, node):
     if node:
        self._postorder(node.left)
        self._postorder(node.right)
        print(node.value, end=" ")

            
tree = BST()
tree.insert(10)
tree.insert(4)
tree.insert(13)
tree.insert(2)
tree.insert(11)
tree.insert(5)
tree.insert(12)

print("Inorder:")
tree.inorder()

print("Preorder:")
tree.preorder()

print("Postorder:")
tree.postorder()



        
        
            
    
            
          
       