"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/description/
"""
from typing import List
from pathlib import Path

from anytree import Node

from utils.plot_tree import TreePlotter
from utils.time_it import time_it

REPO_ROOT_DIR = Path(__file__).parent.parent

"""
Time complexity:

Thinking from a graph perspective, we build up potential solutions using every combination of
candidates until we have a solution or exceed the target. At each level, there are N possible
candidates, and there are at max T levels (if min(candidates)=1). So the time complexity is
O(N^T) or O(N^T/min(candidate)).

See here for an example with a target of 7 and candidates [2,3,6,7]: 
https://github.com/NickCheney/ds-algo-practice/blob/main/src/assets/images/combination_sum.png

Notice the duplicate solutions [2,2,3] and [3,2,2]. To eliminate redundancy, we can bound the 
candidates at each level of backtracking to only include values >= the last candidate added to the
set.

E.g., if the current working combination is [3], the only possibilities to explore would be [3,3,...],
[3,6,...] etc. Checking [3,2,...] would not be necessary as we had checked [2,3,...] already.
"""
class Solution:
    @time_it
    def combinationSumV1(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        No nonlocal variables or extra args, recursive calls to get sub solutions to extend.
        LC runtime: 52 ms
        """
        def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
            res = []
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                elif candidates[i] == target:
                    res.append([candidates[i]])
                else:
                    sub_solutions = combinationSum(candidates[i:], target - candidates[i])
                    for sol in sub_solutions:
                        res.append(sol+[candidates[i]])
            return res
                
        res = combinationSum(candidates, target)
        return res

    @time_it
    def combinationSumV2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Use nonlocal variables for partial solution stack and found solutions.
        LC Runtime: 40ms.
        """
        currentCombo = []
        res = []

        def combinationSumHelper(candidates: List[int], target: int):
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                elif candidates[i] == target:
                    res.append(currentCombo + [candidates[i]])
                else:
                    currentCombo.append(candidates[i])
                    combinationSumHelper(candidates[i:], target - candidates[i])
                    currentCombo.pop()

        combinationSumHelper(candidates, target)
        return res
    
    @time_it
    def combinationSumV3(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Keep partial and complete solutions as helper function args.
        LC Runtime: 44ms.
        """
        def combinationSumHelper(candidates: List[int], target: int, res: List[List[int]] = [], currentCombo: List[int] = []):
            for i in range(len(candidates)):
                if candidates[i] > target:
                    continue
                elif candidates[i] == target:
                    res.append(currentCombo + [candidates[i]])
                else:
                    res = combinationSumHelper(candidates[i:], target - candidates[i], res, currentCombo+[candidates[i]])
            return res

        res = combinationSumHelper(candidates, target)
        return res
    
    def combinationGraph(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Generate a tree representing the backtracking search.
        """
        currentCombo = []
        root = Node("[]")
        curr = root

        def combinationGraphHelper(candidates: List[int], target: int):
            nonlocal curr
            for i in range(len(candidates)):
                if candidates[i] > target:
                    Node(f"{currentCombo+[candidates[i]]} x", parent=curr)
                elif candidates[i] == target:
                    Node(f"{currentCombo+[candidates[i]]} S", parent=curr)
                else:
                    currentCombo.append(candidates[i])
                    new_node = Node(str(currentCombo), parent=curr)
                    curr_copy = curr
                    curr = new_node
                    combinationGraphHelper(candidates, target - candidates[i])
                    curr = curr_copy
                    currentCombo.pop()

        combinationGraphHelper(candidates, target)
        return root        



if __name__ == '__main__':
    s = Solution()

    cases = [
        (1, [2,3,6,7], 7),
        (2, [2,3,5], 8),
        (3, [2], 1)
    ]

    for case, candidates, target in cases:
        print("\nCase",case)
        print("------")
        print(f"candidates = {candidates}")
        print(f"target = {target}")
        print("Result:", s.combinationSumV1(candidates,target))
        print("Result:", s.combinationSumV2(candidates,target))
        print("Result:", s.combinationSumV3(candidates,target))

    print("\nCase 4")
    print("-------")
    candidates = list(range(1,31))
    target = 45
    print(f"candidates = {candidates}")
    print(f"target = {target}")
    s.combinationSumV1(candidates,target)
    s.combinationSumV2(candidates,target)
    s.combinationSumV3(candidates,target)

    # Uncomment to plot a tree of the back
    # tp = TreePlotter(s.combinationGraph([2,3,6,7],7))
    # tp.print_tree()
    # tp.plot_tree(REPO_ROOT_DIR / 'assets/images/combination_sum.png')
    