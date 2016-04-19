"""
"""

def coin_sum(target):
    index = 0
    summ = 0
    res = []
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    curr_combo = []
    traverse(coins, target, index, summ, res, curr_combo)
    return res


def traverse(coins, target, index, summ, res, curr_combo):
    if summ == target:
        res.append(list(curr_combo))
        return
    else:
        for i in range(index, len(coins)):
            if summ + coins[i] > target:
                break
            else:
                curr_combo.append(coins[i])
                traverse(coins, target, i, summ+coins[i], res, curr_combo)
                curr_combo.pop()

print coin_sum(5)
