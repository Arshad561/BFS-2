# Time Complexity: O(N), N is the number of nodes in the tree
# Space Complexity: O(N)
# Did this code successfully run on Leetcode: Yes


from typing import List, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        queue = deque()

        queue.append(root)

        while len(queue):
            size = len(queue)
            x_found = False
            y_found = False
            
            for _ in range(size):
                popped = queue.popleft()

                if popped.val == x:
                    x_found = True
                
                if popped.val == y:
                    y_found = True
                
                if popped.left is not None and popped.right is not None:
                    if popped.left.val == x and popped.right.val == y:
                        return False
                    if popped.left.val == y and popped.right.val == x:
                        return False
                
                if popped.left is not None:
                    queue.append(popped.left)
                
                if popped.right is not None:
                    queue.append(popped.right)
            
            if x_found and y_found:
                return True
            
            if x_found or y_found:
                return False
        
        return False
