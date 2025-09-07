# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(curr):
            if not curr:
                return 0

            left = dfs(curr.left)
            right = dfs(curr.right)

            self.res = max(self.res, left + right)
            return 1 + max(left, right)
        dfs(root)
        return self.res 

'''
Why use self.res in this case?
Global to the Instance of the Class:
By declaring self.res, the variable becomes an instance variable, meaning it is accessible throughout the lifetime of the instance of the class. This allows the dfs (depth-first search) function to update and share the res variable across recursive calls without needing to pass it explicitly as an argument.
Stores the Result:
The self.res variable stores the maximum diameter encountered during the recursive traversal of the tree. Since it needs to be updated globally during the recursion, it is defined as an instance variable.
Encapsulation:
Using self.res ensures that the variable is encapsulated within the instance of the Solution class, which is cleaner than using a global variable.
'''