# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if not k:
            return [target.val]
        
        queue = deque([root])
        graph = defaultdict(list)
        while queue:
            node = queue.popleft()
            if node.left:
                graph[node].append(node.left)
                graph[node.left].append(node)
                queue.append(node.left)
            if node.right:
                graph[node].append(node.right)
                graph[node.right].append(node)
                queue.append(node.right)
        res = []
        visited = set([target])
        queue = deque([(target, 0)])
        while queue:
            node, dist = queue.popleft()
            if dist == k:
                res.append(node.val)
            else:
                for edge in graph[node]:
                    if edge not in visited:
                        visited.add(edge)
                        queue.append((edge, dist+1))
        
        return res
        