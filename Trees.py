# Binary search tree implementation in Python
"""
Have a class for nodes with rules for two child nodes at most.
Have methods for insertion, deletion and search. 
Delete method is hard and needs to be done carefully and will be implemented during self balanced trees.
"""
class Node:
    def __init__(self, value:int):
        self.value = value
        self.left_child = None
        self.right_child = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value:int):
        # function to insert items into BST
        def _insert(node, value:int):
            if node is None:
                return Node(value)
            if value < node.value:
                node.left_child = _insert(node.left_child, value)
            elif value >= node.value:
                node.right_child = _insert(node.right_child, value)
            return node
        self.root = _insert(self.root, value)
        

    def dfs_search(self, node):
        # dfs - o(h) space complexity and o(n) time complexity
        if not node:
            return []
        return [node.value] + self.dfs_search(node.left_child) + self.dfs_search(node.right_child)
    
    def bfs_search(self, node):
        if not node:
            return []
        result = []
        queue = [node]

        while len(queue) > 0:
            curr_node = queue.pop(0)
            result.append(curr_node.value)
            
            if curr_node.left_child is not None:
                queue.append(curr_node.left_child)
            
            if curr_node.right_child is not None:
                queue.append(curr_node.right_child)
        
        return result
    
    def read_tree(self, order):
        "code to traverse a tree"
        pass


""" Test code for BST """

def test_bst():
    tree_obj = BST()
    tmp_list = [3,4,1,6, 2, 10, 20]
    for i in tmp_list:
        tree_obj.insert(i)
    result = tree_obj.dfs_search(tree_obj.root)
    result_bfs = tree_obj.bfs_search(tree_obj.root)
    for i in result:
        print("dfs:", i)

    for j in result_bfs:
        print("bfs:", j)

test_bst()


"""
Space and time complexity
pros and cons
real world usecases 
typical corner cases
other alternatives
"""
    
# Inorder, preorder, postorder
# Depth first search
# Breadth first search
# Self balancing trees
# Priority Queue 
