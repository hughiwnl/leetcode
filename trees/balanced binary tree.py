# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root:
                return 0
            
            left = height(root.left)
            right = height(root.right)

            if abs(left - right) > 1:
                balanced[0] = False
                return 0
            
            return 1 + max(left,right)
        height(root)
        return balanced[0]
    
# A list is mutable in Python. By using balanced = [True], the nested height function can modify the value of balanced (e.g., balanced[0] = False), and this change will persist outside the height function. This is because the height function modifies the contents of the same list object, not the reference itself.
# Since balanced is a list (balanced = [True]), its elements are accessed using index notation. The only element in the list, at index 0, stores the boolean value (True or False) that determines whether the binary tree is balanced.