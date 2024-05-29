from time_it import time_it
from typing import List
from collections import deque
from anytree import Node
from images.plot_tree import TreePlotter

"""
Time complexity:

Thinking from a graph perspective, we build up potential solutions using every combination of
candidates until we have a solution or exceed the target. At each level, there are N possible
candidates, and there are at max T levels (if min(candidates)=1). So the time complexity is
O(N^T) or O(N^T/min(candidate)).
"""
class Solution:
    """
    No helper function, recursive calls to get sub solutions to extend.
    LC runtime: 52 ms
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        for i in range(len(candidates)-1,-1,-1):
            if candidates[i] > target:
                continue
            elif candidates[i] == target:
                res.append([candidates[i]])
            else:
                sub_solutions = self.combinationSum(candidates[:i+1], target - candidates[i])
                for sol in sub_solutions:
                    res.append(sol+[candidates[i]])
        
        return res

    def combinationSumV2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Use nonlocal variables for partial solution stack and found solutions.
        Runtime: 40ms.
        """
        currentCombo = []
        res = []

        def combinationSumHelper(candidates: List[int], target: int):
            for i in range(len(candidates)-1,-1,-1):
                if candidates[i] > target:
                    continue
                elif candidates[i] == target:
                    res.append(currentCombo + [candidates[i]])
                else:
                    currentCombo.append(candidates[i])
                    combinationSumHelper(candidates[:i+1], target - candidates[i])
                    currentCombo.pop()

        combinationSumHelper(candidates, target)
        return res
    
    def combinationSumV3(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Keep partial and complete solutions as helper function args.
        Runtime: 44ms.
        """
        def combinationSumHelper(candidates: List[int], target: int, res: List[List[int]] = [], currentCombo: List[int] = []):
            for i in range(len(candidates)-1,-1,-1):
                if candidates[i] > target:
                    continue
                elif candidates[i] == target:
                    res.append(currentCombo + [candidates[i]])
                else:
                    res = combinationSumHelper(candidates[:i+1], target - candidates[i], res, currentCombo+[candidates[i]])
            return res

        res = combinationSumHelper(candidates, target)
        return res
    
    def combinationGraph(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Use nonlocal variables for partial solution stack and found solutions.
        Runtime: 40ms.
        """
        currentCombo = []
        root = Node("[]")
        curr = root

        def combinationGraphHelper(candidates: List[int], target: int):
            nonlocal curr
            for i in range(len(candidates)):
                if candidates[i] > target:
                    Node(f"{currentCombo+[candidates[i]]} X", parent=curr)
                elif candidates[i] == target:
                    Node(f"{currentCombo+[candidates[i]]} S", parent=curr)
                else:
                    currentCombo.append(candidates[i])
                    new_node = Node(str(currentCombo), parent=curr)
                    curr_copy = curr
                    curr = new_node
                    combinationGraphHelper(candidates[:i+1], target - candidates[i])
                    curr = curr_copy
                    currentCombo.pop()

        combinationGraphHelper(candidates, target)
        return root        



if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum([2,3,6,7],7))
    print(s.combinationSum([2,3,5],8))
    print(s.combinationSum([2],1))

    print(s.combinationSumV2([2,3,6,7],7))
    print(s.combinationSumV2([2,3,5],8))
    print(s.combinationSumV2([2],1))

    print(s.combinationSumV3([2,3,6,7],7))
    print(s.combinationSumV3([2,3,5],8))
    print(s.combinationSumV3([2],1))

    tp = TreePlotter(s.combinationGraph([2,3,6,7],7))
    tp.print_tree()
    tp.plot_tree('images/combination_sum.png')
    