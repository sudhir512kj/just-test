# def printfractions(n):

#     for i in range(1, n):
#         for j in range(i + 1, n + 1):

#             # If the numerator and
#             # denominator are coprime
#             if __gcd(i, j) == 1:
#                 a = str(i)
#                 b = str(j)
#                 print(a + '/' + b, end=", ")


# def __gcd(a, b):

#     if b == 0:
#         return a
#     else:
#         return __gcd(b, a % b)


# # Driver code
# if __name__ == '__main__':

#     n = 5
#     printfractions(n)

# # This code is contributed by virusbuddah_

def printFractions(n):
  Fractions_set = set()
  res = []
  for i in range(n,0,-1):
    for j in range(1,i+1):
      if j/i not in Fractions_set:
        Fractions_set.add(j/i)
        res.append("{}/{}".format(j,i))
      else:
        res.remove("{}/{}".format(j+1,i+1))
        res.append("{}/{}".format(j,i))
  res = sorted(key= lambda i,j: res[i].split("/")[0]/ res[i].split("/")[1] < res[j].split("/")[0]/ res[j].split("/")[1])
  return res

print(printFractions(3))