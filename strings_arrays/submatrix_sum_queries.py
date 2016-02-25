#GeeksforGeeks: http://www.geeksforgeeks.org/submatrix-sum-queries/
#Given a matrix of size M x N, there are large number of queries to find submatrix sums.
#Inputs to queries are left top and right bottom indexes of submatrix whose sum is to find out.
#How to preprocess the matrix so that submatrix sum queries can be performed in O(1) time.



matrix = [[1, 2, 3, 4, 6],
            [5, 3, 8, 1, 2],
            [4, 6, 7, 5, 5],
            [2, 4, 8, 9, 4]]

def build_aux_matrix(matrix):
    aux_matrix = [[]]

    #copy first row
    for i in range(len(matrix[0])):
        aux_matrix[0].append(matrix[0][i])

    #sum the columns


build_aux_matrix(matrix)


def find_submatrix_sum1(matrix, tli=None, tlj=None, rbi=None, rbj=None):
    aux_matrix = build_aux_matrix(matrix)


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

# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()


