
def findArea(vert,hori,m,n):

    vert.sort()
    hori.sort()

    distV = -3**38
    for i in range(len(vert)-1):
        distV = max(distV, vert[i+1]-vert[i]-1)
        
    distV = max(distV,vert[0]-1)
    distV = max(distV,m-vert[-1])

    distH = -3**38
    for i in range(len(hori)-1):
        distH = max(distH, hori[i+1]-hori[i]-1)
    
    
    distH = max(distH, hori[0]-1)
    distH = max(distH, n-hori[-1])

        
    return  distH * distV

test_cases = int(input())
for _ in range(test_cases):

    m,n,x = map(int,input().split())
    vert = []
    hori = []

    for p in range(x):
        a,b = map(int,input().split())
        vert.append(a)
        hori.append(b)
    
    print(findArea(vert,hori,m,n))


