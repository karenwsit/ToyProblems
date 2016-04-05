"""
Given a set of candidate numbers & target number, find all unique combinations.
The same repeated number may be chosen from candidate numbers unlimited number of times.
Note:
All numbers (including target) will be positive integers.
Elements in a combination (a1, a2, a3, ..., ak) must be in non-descending order.
The solution set must not contain duplicate combinations.
"""

def combinationSum(candidates, target):
    """
    >>> combinationSum([2,3,6,7], 7)
    [[2, 2, 3], [7]]
    """
    res = []
    cand = []
    candidates.sort()
    combination_sum(candidates, [], target, 0, 0, res)
    return res

def combination_sum(candidates, cand, target, index, summ, res):
    if summ == target:
        res.append(list(cand))
    else:
        for i in range(index, len(candidates)):
            if summ + candidates[i] > target:
                break
            cand.append(candidates[i])
            combination_sum(candidates, cand, target, i, summ+candidates[i], res)
            cand.pop()

#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
