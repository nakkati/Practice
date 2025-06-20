# Binary search tree implementation in Python
"""
Have a class for nodes with rules for two child nodes at most.
Have methods for insertion, deletion and search. 
Delete method is hard and needs to be done carefully and will be implemented during self balanced trees.
"""
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
"""
"""
segment tree - binary tree to answer range queries in o(log n) with o(n) build time and o(n) space
useful incase where we need to do range queries on large datasets. overly complex and need to know the input size at start
builds a segment array
"""

class SegmentTree_min():
    def __init__(self, data:list):
        self.size = len(data)
        self.seg_tree = [float('inf')] * 4 * self.size
        self.lazy_tree = [0] * 4 * self.size
        self.build(data, 0, 0, self.size - 1)
    
    def build(self, data, seg_pos, start_index, last_index):
        if (start_index == last_index):
            self.seg_tree[seg_pos] = data[start_index]
            return
        mid = (start_index + last_index)// 2
        self.build(data, 2*seg_pos+1, start_index, mid)
        self.build(data, 2*seg_pos+2, mid+1, last_index)
        self.seg_tree[seg_pos] = min(self.seg_tree[2*seg_pos+1], self.seg_tree[2*seg_pos+2])

    def propagate(self, lazy_root, l, r):
        if self.lazy_tree[lazy_root] != 0:
            self.seg_tree[lazy_root] += self.lazy_tree[lazy_root]

            if l != r:
                self.lazy_tree[2 * lazy_root + 1] += self.lazy_tree[lazy_root]
                self.lazy_tree[2 * lazy_root + 2] += self.lazy_tree[lazy_root]
            
            self.lazy_tree[lazy_root] = 0
    
    def update(self, ql, qr, val, seg_root = 0, l = 0, r = None):
        if r is None:
            r = self.size - 1
        
        self.propagate(seg_root, l , r)
        # no overlap
        if (ql > r or qr < l):
            return 
        # total overlap
        if (ql <= l and qr >=r):
            self.lazy_tree[seg_root] += val
            self.propagate(seg_root, l, r)
        
        mid = (l + r) // 2
        self.update(ql, qr, val, 2 * seg_root + 1, l, mid)
        self.update(ql, qr, val, 2 * seg_root + 2, mid + 1, r)
        self.seg_tree[seg_root] = min(self.seg_tree[2 * seg_root + 1], self.seg_tree[2 * seg_root + 2])


    def query(self, q_start_pos, q_last_pos, seg_pos_root = 0, data_l_pos = 0, data_r_pos = None):
        if data_r_pos is None:
            data_r_pos = self.size - 1

        self.propagate(seg_pos_root, data_l_pos, data_r_pos)
        
        # to check no overlap
        if (q_start_pos > data_r_pos or q_last_pos < data_l_pos):
            return float('inf')
        # total overlap
        if (q_start_pos <= data_l_pos and  q_last_pos >= data_r_pos):
            return self.seg_tree[seg_pos_root]
        mid = (data_l_pos + data_r_pos) // 2
        left_min = self.query(q_start_pos, q_last_pos, 2*seg_pos_root+1, data_l_pos, mid)
        right_min = self.query(q_start_pos, q_last_pos, 2*seg_pos_root+2, mid+1, data_r_pos)
        return min(left_min, right_min)
    
    


arr_input = [-1, 0, 4, 3, 6]
s_tree = SegmentTree_min(arr_input)
print("minimum from index 1 to 3: ",s_tree.query(1,3))
s_tree.update(1,3,5)
print("minimum from index 1 to 3: ",s_tree.query(1,3))




"""
segment tree lazy propogation - binary tree to answer range queries in o(log n) with o(n) build time and o(n) space
this is an optimization when updates need to be done over a range.
We need to implemet a new lazy tree using an array which keeps track of unupdated notes. 
"""

"""
sparse table algorithm
"""

"""
Fenwick tree
"""

"""
red black trees - balanced binary search trees - no need to implement but allows o(log n) insertion/deletion and search
fewer rotations than AVL and useful when there are lot of insertions and deletions. 
"""


"""
splay trees - self organizing binary search trees - frequently used
self balancing trees provide o(log n) time complexity but what if we know search queries before hand? in splay trees we can
have those most searched nodes at the top.
"""


"""
b-trees - For large datasets - but how large
Search space is more shallow and is helpful because each memory fetch will now fetch multiple keys, will have more comparisons to make
in most systems CPUs are faster than memory bw
"""


"""
How does NCCL use trees or other libraries use them? double binary tree
"""

""" Test code for BST """
"""
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