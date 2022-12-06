def play(health, armour):

    count = 1
    air = (3,2)
    water = (-5,-10)
    fire = (-20,5)
    level = 0

    while health > 0 and armour > 0:

        
        if count % 2 != 0:
            health += air[0]
            armour += air[1]
           
        else:
            if health > 5 and armour > 10:
                health += water[0]
                armour += water[1]
                
            else:
                health += fire[0]
                armour += fire[1]
            
        if armour > 0  and health > 0:
            level += 1
            count += 1
        
    return level


test_cases = int(input())
for _ in range(test_cases):

    health, armour = map(int,input().split())
    print(play(health,armour))