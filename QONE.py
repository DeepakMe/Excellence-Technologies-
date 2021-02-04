# Question1
# Q1.Write a function which returns sum of the list of numbers?
# Ans:
list1 = [1,2,3,4]
def Sumlist(list,size):
    if (size==0):
        return 0
    else:
        return list[size-1]+Sumlist(list,size-1)
total = Sumlist(list1,len(list1))
print("Sum of given elements in List: ",total)