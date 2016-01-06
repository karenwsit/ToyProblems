#Exercise 1.8 of Cracking the Coding Interview
#Write an alogrithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0.
#################################################################################

from random import randint

#Time = O(M*N)
#Space = O(M*N)


def get_zeros(matrix):
    """
    >>> get_zeros([[1, 0, 3, 6],[4, 8, 6, 2],[7, 8, 9, 0]])
    ([0, 2], [1, 3])
    """
    # matrix = [[0]*n for i in range(m)]

    # matrix = []
    # for i in range(m):
    #     new = []
    #     for j in range(n):
    #         element = randint(0,9)
    #         new.append(element)
    #     matrix.append(new)

    row_list = []
    column_list = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row_list.append(i)
                column_list.append(j)
    return row_list, column_list

def set_zeros(matrix, row_list, column_list):
    """
    >>> set_zeros([[1, 0, 3, 6],[4, 8, 6, 2],[7, 8, 9, 0]], [0, 2], [1, 3])
    [[0, 0, 0, 0], [4, 0, 6, 0], [0, 0, 0, 0]]
    """
    for row in row_list:
        for integer in matrix[row]:
            integer == 0
        # matrix[row] = [0]*len(matrix[row])

    for row in matrix:
        for col in column_list:
            row[col] = 0

    return matrix


##################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

