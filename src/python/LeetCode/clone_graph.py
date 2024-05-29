
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        to_visit = []
        to_visit.append(node)
        node_copy = {}
        while len(to_visit) > 0:
            curr_node = to_visit.pop()
            if curr_node not in node_copy:
                node_copy[curr_node] = Node(**vars(curr_node))
            curr_node = node_copy[curr_node]

            for index, nbr_node in enumerate(curr_node.neighbors):
                if nbr_node not in node_copy:
                    node_copy[nbr_node] = Node(**vars(nbr_node))
                    to_visit.append(nbr_node)

                curr_node.neighbors[index] = node_copy[nbr_node]

        return node_copy[node]
    

if __name__=='__main__':
    sol = Solution()
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    nodes = [Node(val=i) for i in range(1,5)]
    for i in range(4):
        for nb in adjList[i]:
            nodes[i].neighbors.append(nodes[nb-1])
    print(nodes)
    new_node0 = sol.cloneGraph(nodes[0])
    print(new_node0)