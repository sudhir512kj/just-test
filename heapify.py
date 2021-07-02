import heapq

def sort_k_messed_array(arr, k):
   
  
  if len(arr)>2*k:
    H=heapq.heapify(arr[:2*k])
    
    List=[]
    for i in range(2*k,len(arr)):
    
      List.append(heapq.heappushpop(H,arr[i]))
    List+=H  
    return List 
  
  arr.sort()
  return arr