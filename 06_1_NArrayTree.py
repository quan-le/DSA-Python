from collections import deque

class Node:
    # For N-ary tree, we use a list to store all child nodes
    def __init__(self, data):
        self.data = data
        self.children = []  # List of children


class NaryTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_data, new_data):
        # Time Complexity: O(n) in the worst case (BFS to find parent)
        new_node = Node(new_data)
        if self.root is None:
            self.root = new_node
            return

        # Use BFS to find parent node
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.data == parent_data:
                current.children.append(new_node)
                return
            for child in current.children:
                queue.append(child)

    def search(self, target):
        # Time Complexity: O(n)
        if not self.root:
            return False

        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            if current.data == target:
                print(current.data)
                return True
            for child in current.children:
                queue.append(child)
        return False

    def preorder(self):
        # Time Complexity: O(n)
        #Root -> Child
        def _preorder(node):
            if node:
                print(node.data, end=' ')
                for child in node.children:
                    _preorder(child)
        _preorder(self.root)

    def postorder(self):
        # Time Complexity: O(n)
        #Child -> Root
        def _postorder(node):
            if node:
                for child in node.children:
                    _postorder(child)
                print(node.data, end=' ')
        _postorder(self.root)

    def bfs(self):
        # Breadth-First Search (level-order traversal)
        # Time Complexity: O(n)
        if not self.root:
            return

        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            print(node.data, end=" ")
            for child in node.children:
                queue.append(child)

    def dfs(self):
        # Depth-First Search (Preorder)
        # Time Complexity: O(n)
        def _dfs(node):
            if node:
                print(node.data, end=' ')
                for child in node.children:
                    _dfs(child)
        _dfs(self.root)


# Driver code for demonstration
if __name__ == '__main__':
    tree = NaryTree()
    tree.insert(None, 1)      # Root
    tree.insert(1, 2)
    tree.insert(1, 3)
    tree.insert(1, 4)
    tree.insert(2, 5)
    tree.insert(2, 6)
    tree.insert(4, 7)

    print("\n\nSearch for 6:", tree.search(6))
    print("Search for 10:", tree.search(10))

    print("\nPreorder traversal:")
    tree.preorder()

    print("\n\nPostorder traversal:")
    tree.postorder()

    print("\n\nDepth-First Search:")
    tree.dfs()

    print("\n\nBreadth-First Search:")
    tree.bfs()
