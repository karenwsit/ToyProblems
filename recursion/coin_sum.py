"""
"""

def coin_sum(target):
    summ = 0
    res = []
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    curr_combo = []
    traverse(coins, target, summ, res, curr_combo)
    return res


def traverse(coins, target, summ, res, curr_combo):
    if summ == target:
        res.append(curr_combo)
    else:
        for i in range(len(coins)):
            if summ + coins[i] > target:
                break
            else:
                summ += coins[i]
                curr_combo.append(coins[i])
                traverse(coins, target, summ, res, curr_combo)
    return res

print coin_sum(5)
