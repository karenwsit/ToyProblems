#GeeksforGeeks: http://www.geeksforgeeks.org/submatrix-sum-queries/
#Given a matrix of size M x N, there are large number of queries to find submatrix sums.
#Inputs to queries are left top and right bottom indexes of submatrix whose sum is to find out.
#How to preprocess the matrix so that submatrix sum queries can be performed in O(1) time.


matrix = [[1, 2, 3, 4, 6],
            [5, 3, 8, 1, 2],
            [4, 6, 7, 5, 5],
            [2, 4, 8, 9, 4]]

#Runtime for Submatrix Sum Queries = O(1)

def build_aux_matrix(matrix):
    aux_matrix = [[0] * len(matrix[0]) for i in range(len(matrix))]

    #copy first row
    for i in range(len(matrix[0])):
        aux_matrix[0][i] = matrix[0][i]

    #sum the columns
    for i in range(1, len(matrix)):
        for j in range(len(matrix[0])):
            aux_matrix[i][j] = matrix[i][j] + aux_matrix[i-1][j]
            
    #sum the rows
    for i in range(len(matrix)):
        for j in range(1, len(matrix[0])):
            aux_matrix[i][j] += aux_matrix[i][j-1]

    return aux_matrix

def find_submatrix_sum1(matrix, tli=None, tlj=None, rbi=None, rbj=None):
    """
    matrix = [[1, 2, 3, 4, 6],
        [5, 3, 8, 1, 2],
        [4, 6, 7, 5, 5],
        [2, 4, 8, 9, 4]]
    >>> find_submatrix_sum1(matrix, tli = 0, tlj = 0, rbi = 1, rbj = 1)
    11
    >>> find_submatrix_sum1(matrix, tli = 2, tlj = 2, rbi = 3, rbj = 4)
    38
    >>> find_submatrix_sum1(matrix, tli = 1, tlj = 2, rbi = 3, rbj = 3)
    38
    """
    aux_matrix = build_aux_matrix(matrix)

    result = aux_matrix[rbi][rbj]

    if tli > 0:
        result -= aux_matrix[tli-1][rbj]

    if tlj > 0:
        result -= aux_matrix[rbi][tlj-1]

    if tli > 0 and tlj > 0:
        result += aux_matrix[tli-1][tlj-1]

    return result
    
#Runtime = O(n^2)

# def find_submatrix_sum(matrix, tli=None, tlj=None, rbi=None, rbj=None):
#     """
#     matrix = [[1, 2, 3, 4, 6],
#             [5, 3, 8, 1, 2],
#             [4, 6, 7, 5, 5],
#             [2, 4, 8, 9, 4]]
#     >>> find_submatrix_sum(matrix, tli = 0, tlj = 0, rbi = 1, rbj = 1)
#     11
#     >>> find_submatrix_sum(matrix, tli = 2, tlj = 2, rbi = 3, rbj = 4)
#     38
#     >>> find_submatrix_sum(matrix, tli = 1, tlj = 2, rbi = 3, rbj = 3)
#     38
#     """

#     submatrix_sum = 0

#     for i in range(tli, rbi+1):
#         for j in range(tlj, rbj+1):
#             submatrix_sum += matrix[i][j]

#     return submatrix_sum

if __name__ == '__main__':
    import doctest
    doctest.testmod()


