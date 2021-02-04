# Question3
# Q3.Write a python function to the number of maximum consecutive  one’s present in the array?
# Ans:
def getMaxLength(arr, n): 
    count = 0 
    result = 0 
  
    for i in range(0, n): 
        if (arr[i] == 0): 
            count = 0
        else: 
            count+= 1 
            result = max(result, count)  
    return result  
  
arr = [0,0,0,1,1,1,0,0,0,1,1,0,1,1,1,1,0,0,1,1]  
n = len(arr)  
  
print(getMaxLength(arr, n))