#Exercise 1.7 of Cracking the Coding Interview
#Given NxN matrix, write a method to rotate matrix by 90 degrees.
#################################################################################

#Time = O(n^2)
#Space = O(n^2)

def rotate_matrix(m):
    """
    >>> rotate_matrix([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
    """
    layers = len(m) / 2
    length = len(m) - 1
    for layer in range(layers):
        for i in range(layer, length - layer):
            #saving the top layer
            temp = m[layer][i]
            #left to top
            m[layer][i] = m[length - i][layer]
            #bottom to left
            m[length-i][layer] = m[length-layer][length-i]
            #right to bottom
            m[length-layer][length-i] = m[i][length-layer]
            #top to right
            m[i][length-layer] = temp

    return m


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
