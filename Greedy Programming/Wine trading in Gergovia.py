def wines(arr):

    buyer = []
    seller = []

    for index,num in enumerate(arr):

        if num < 0:
            seller.append([abs(num),index])
        
        elif num > 0:
            buyer.append([num,index])
    
    cost = 0
    i = 0
    j = 0

    while i < len(buyer) and j < len(seller):

        if buyer[i][0] >= seller[j][0]:
            taken = seller[j][0]
            dist = abs(buyer[i][1] - seller[j][1])

            cost += taken*dist

            buyer[i][0] -= seller[j][0]
            seller[j][0] = 0
            j += 1
        
        elif seller[j][0] > buyer[i][0]:
            
            taken = buyer[i][0]
            dist = abs(buyer[i][1] - seller[j][1])

            cost += taken * dist

            seller[j][0] -= buyer[i][0]
            buyer[i][0] = 0
            i += 1
        
    return cost
        
while True:
    n = int(input())

    if n == 0:
        break

    arr = [int(num) for num in input().split()]
    print(wines(arr))

    