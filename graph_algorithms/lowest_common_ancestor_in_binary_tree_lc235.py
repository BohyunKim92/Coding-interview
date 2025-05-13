# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # what do you mean by lowest node further down in the descendant?
        # node.left = p and node.right = q -> node is lowest. 
        # (node.left).left = p, 
        # bfs is maybe reasonable. 
        # dumb solution. from root find the p, from the root find q. iterate the list of parents and find the lowest common parents. 
        # took longer bc got flustered..
        # know the definition of a binary tree where every node in the left subtree has a value less than the root, and every node in the right subtree has a value greater than the root 
        
        while root:
            # while root is not None
            if max(p.val, q.val) < root.val:
                # in the left hand of the root
                root = root.left
            elif min(p.val, q.val) > root.val:
                #in the right hand of the root 
                root = root.right
            else:
                return root 