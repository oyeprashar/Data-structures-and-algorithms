def knightTravels(i,j,count,n,mat,found):
   if found[0] == True:
      return 

   if i < 0 or j < 0 or i >= n or j >= n or mat[i][j] != 0:
      return 

   if count == n**2:
      found[0] = True
      mat[i][j] = count
      for list1 in mat:
         print(list1)
      return 


   mat[i][j] = count
   knightTravels(i-2,j-1,count+1,n,mat,found)
   knightTravels(i-2,j+1,count+1,n,mat,found)
   knightTravels(i-1,j-2,count+1,n,mat,found)
   knightTravels(i+1,j-2,count+1,n,mat,found) 
   knightTravels(i+2,j-1,count+1,n,mat,found) 
   knightTravels(i+2,j+1,count+1,n,mat,found)
   knightTravels(i-1,j+2,count+1,n,mat,found) 
   knightTravels(i+1,j+2,count+1,n,mat,found) 
   mat[i][j] = 0

def knightTour(n):

   found = [False]
   mat = []
   for x in range(n):
      list1 = []
      for y in range(n):
         list1.append(0)
      mat.append(list1)
   i = j  = 0
   knightTravels(i,j,1,n,mat,found)

knightTour(7) 

 