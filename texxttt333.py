def index_equals_value_search(arr):
  
  
  lo=0
  hi=len(arr)-1
  
  while lo<=hi:
    mid=(lo+hi)//2
    
    value=arr[mid]
    
    if value==mid:
      return mid
    elif value<mid:
      lo=mid+1
    else:
      hi=mid-1
  return -1

print(index_equals_value_search([-8,0,2,5]))
print(index_equals_value_search([-1,0,3,6]))