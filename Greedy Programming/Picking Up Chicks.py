def pick_chicks(pos,speed,time,barn_dist,target):

    obs = 0
    index = len(pos)-1
    ans = 0
    picked = 0

    while index >= 0:

        canCover = speed[index] * time 
        req = barn_dist - pos[index]

        if canCover >= req:
            ans += obs 
        else:
            obs += 1
        
        index -= 1
    
    if picked < target:
        return "Impossible"
    return ans 

test_cases = int(input())
for t in range(test_cases):

    N, target, barn_dist, time = map(int,input().split())
    pos = [int(num) for num in input().split()]
    speed = [int(num) for num in input().split()]

    ans = pick_chicks(pos,speed,barn_dist,time,target)
    print("Case #" + str(t+1) + ":" + " " + str(ans)) 