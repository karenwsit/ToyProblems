"""
The thief has found himself a new place for his thievery again. 
There is only one entrance to this area, called the "root." 
Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that "all houses in this place forms a binary tree". 
It will automatically contact the police if two directly-linked houses were broken into on the same night.
Determine the maximum amount of money the thief can rob tonight without alerting the police.
https://leetcode.com/problems/house-robber-iii/
"""

# Runtime: O(n)

class Solution(object):
    def rob(self, root):
        rob_root, not_rob_root = self.dfs(root)
        return max(rob_root, not_rob_root)

    def dfs(self, node):
        if node is None:
            return (0, 0)
        rob_left, not_rob_left = self.dfs(node.left)
        rob_right, not_rob_right = self.dfs(node.right)

        rob_node = node.val + not_rob_left + not_rob_right
        not_rob_node = max(rob_left, not_rob_left) + max(rob_right, not_rob_right)
        # Think about it: Why not "not_rob_node = rob_left + rob_right"?

        return (rob_node, not_rob_node)
