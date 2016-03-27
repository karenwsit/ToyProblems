"""
Write a program that outputs all combinations of (2 and 3 pointers) of a given basketball score.
"""

def get_bball_combo(score, combo_list=None):
    """
    >>> get_bball_combo(6)
    [2, 2, 2]
    [3, 3]
    >>> get_bball_combo(3)
    [3]
    """

    if combo_list is None:
        combo_list = []
    if score == 0:
        print combo_list
        return
    if score == 1:
        return

    if score >= 2:
        combo_list.append(2)
        get_bball_combo(score-2, combo_list)
        combo_list.pop(-1)
    if score >= 3:
        combo_list.append(3)
        get_bball_combo(score-3, combo_list)
        combo_list.pop(-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()