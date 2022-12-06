def isPossible(start,currSum,k,targetSum,visited,arr):

   if k == 1:      # main function checked that sum(arr) % k == 0, hence if all subsets are formed and just one is left, it will obviously be formed
      return True  # rest by of the elements
      
   if currSum > targetSum:
      return 

   if currSum == targetSum: 
      # we found one  subset, let us find  other subsets too
      return isPossible(0,0,k-1,targetSum,visited,arr)

   for i in range(start,len(arr)):
      if visited[i] == False:
         visited[i] = True # mark true when we include the element in the currSum
         if isPossible(i+1,currSum+arr[i],k,targetSum,visited,arr) == True: # if we end up k == 1, return True immediately,
            return True                                                     # we have found all the subsets                                          

         visited[i] =  False # unmark if we hit some return statement which was not True

   return False

def kpartitions(arr,k):
   if sum(arr) % k != 0:
      return False
   if k == 0:
      return False
   if len(arr) == 0:
      return False

   start = currSum = 0
   targetSum = sum(arr) / k 

   visited = [False] * len(arr)

   return isPossible(start,currSum,k,targetSum,visited,arr)
arr1 = [2,1,4,5,6]
k1 = 3

arr2 = [2,1,5,5,6]
k2 = 3

print(kpartitions(arr1,k1))
print(kpartitions(arr2,k2))
