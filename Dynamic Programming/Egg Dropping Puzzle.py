def eggDropping(eggs,totalFloor):

     """
     Base Cases 
     >> if floor == 0, attempts == 0
     >> if eggs == 0, attempts == 0
     >> if floor == 1, attempts == 1
     >> if eggs == 1, attempts == number of floors
     """

     memory = []
     for x in range(eggs+1):
          list1 = []
          for y in range(totalFloor+1):
               list1.append(0)
          memory.append(list1)
     
     # filling col 1 with 1
     for row in range(len(memory)):
          memory[row][1] = 1
     
     # filling the first row i.e. eggs == 1
     for x in range(len(memory[0])):
          memory[1][x] = x 
     
     for i in range(2,len(memory)):
          for j in range(2,len(memory[0])):

               # we need to find all possible ways from floor 1 till current floor j and take min of all the posibilities
               minRes = 3**38
               for currFloor in range(1,j+1):
                    op1 = memory[i-1][currFloor-1]
                    op2 = memory[i][j-currFloor]
                    minRes = min(minRes,max(op1,op2))
               
               memory[i][j] = 1 + minRes

     return memory[eggs][totalFloor]

