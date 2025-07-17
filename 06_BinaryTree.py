from collections import deque
class Node:
    #Because this is the binary tree we use left, right to keep track of child node
    #If we want to implement generic tree we use array
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, node: Node):
        #Time Complexity: O(log n) on average, O(n) on worst case (unbalanced tree)
        if self.root is None:
            self.root = node
            return
        current = self.root
        while True:
            if node.data < current.data:
                #handle left child
                if current.left is None:
                    current.left = node
                    return
                else:
                    current = current.left
            else:
                #handle right child
                if current.right is None:
                    current.right = node
                    return
                else:
                    current = current.right
    
    def search(self, data):
        #Time complexity: O(log n) on average, O(n) worst case
        current = self.root
        while current:
            if data == current.data:
                print(current.data)
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
    
    def min_value_node(self):
        #Time complexity: O(log n)
        current = self.root
        while current.left:
            current = current.left
        return current
    def max_value_node(self):
        #Time complexity: O(log n)
        current = self.root
        while current.right:
            current = current.right
        return current
    
    def inorder(self):
        # Time Complexity: O(n)
        #left -> root -> right
        def _inorder(node):
            if node:
                _inorder(node.left)
                print(node.data, end=' ')
                _inorder(node.right)
        _inorder(self.root)

    def preorder(self):
        # Time Complexity: O(n)
        # Root -> left -> right
        def _preorder(node):
            if node:
                print(node.data, end=' ')
                _preorder(node.left)
                _preorder(node.right)
        _preorder(self.root)

    def postorder(self):
        # Time Complexity: O(n)
        # Left -> Right -> Root
        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                print(node.data, end=' ')
        _postorder(self.root)
    
    def bfs(self):
        #Breadth-First Search (level order traversal)
        # Focus on exploring the each level fully before going to the deeper level
        # Time Complexity: O(n)
        if not self.root:
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()              #remove the left element
            print(node.data, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def dfs(self):
        # Depth-First Search (Preorder traversal)
        # DFS visits the root , then recursively tranverse all the left and right subtrees
        # Time Complexity: O(n) 
        def _dfs(node):
            if node:
                print(node.data, end=' ')
                _dfs(node.left)
                _dfs(node.right)
            _dfs(self.root)

# Driver code for demonstration
if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(Node(50))
    bt.insert(Node(30))
    bt.insert(Node(70))
    bt.insert(Node(20))
    bt.insert(Node(40))
    bt.insert(Node(60))
    bt.insert(Node(80))

    print("Inorder traversal:")
    bt.inorder()

    print("\n\nSearch for 60:", bt.search(60))
    print("Search for 25:", bt.search(25))

    print("\nDelete 20")
    #bt.delete(20)
    print("\n\nInorder traversal:")
    bt.inorder()

    print("\n\nPreorder traversal:")
    bt.preorder()

    print("\n\nPostorder traversal:")
    bt.postorder()

    print("\n\nDepth-First Search:")
    bt.dfs()

    print("\n\nBreadth-First Search (Level-order):")
    bt.bfs()