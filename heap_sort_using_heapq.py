import heapq

# The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)
    heapq.heapify(arr)
    res = []
    for _ in range(n):
      res.append(heapq.heappop(arr))
    return res


# Driver code
arr = [12, 11, 13, 5, 6, 7]
print(heapSort(arr))
