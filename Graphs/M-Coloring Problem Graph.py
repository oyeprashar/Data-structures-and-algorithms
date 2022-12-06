def isPossible(currV, k, colored, V, graph):
    
    if currV == V:
        return True 
    
    for color in range(k):
        avail = True
        for nbr in range(V):
            if graph[currV][nbr] == 1 and colored[nbr] == color:
                avail = False
                break 
        
        if avail:
            colored[currV] = color 
            if isPossible(currV + 1, k, colored, V, graph):
                return True 
            colored[currV] = -1
    
    return False


def graphColoring(graph, k, V):
    
    colored = [-1] * (V+1)
    return isPossible(0, k, colored, V, graph)
