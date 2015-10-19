#print numbers in a Z within a NxN matrix

def printz(n):
  num = 1
  matrix = [[0]*n for i in xrange(n)]

  for i in xrange(n):
    for j in xrange(n):
      if i == 0 or i == n-1 or j == (n-i-1):
        if num > 9:
          for d in str(num):
            num = int(d[-1]) 
        matrix[i][j] = num
        num += 1

  for row in matrix:
    print row

printz(5)
