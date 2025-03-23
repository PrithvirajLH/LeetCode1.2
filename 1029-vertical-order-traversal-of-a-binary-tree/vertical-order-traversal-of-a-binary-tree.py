# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([(root, 0, 0)])
        level_map = defaultdict(list)

        while queue:
            node, row, col = queue.popleft()
            level_map[col].append((node.val, row))
            if node.left:
                queue.append((node.left, row+1, col-1))
            if node.right:
                queue.append((node.right, row+1, col+1))
        res = []
        
        for _, items in sorted(level_map.items()):
            items.sort(key= lambda x: (x[1], x[0]))

            items = [val for val, _ in items]
            res.append(items)
        return res

        