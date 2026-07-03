"""
A graph is at tree if
    1. No disconnected component
    2. No loop
"""

def checkUndirectedLoop(currV, visited, adj, parent):

    visited.add(currV)

    for nbr in adj[currV]:
        if nbr in visited:

            # is nbr is visited and we did not come from nbr to current node
            # if i came from nbr to curr node then parent of curr node will be nbr
            if parent[currV] != nbr:
                return True

        else:
            parent[nbr] = currV
            if checkUndirectedLoop(nbr, visited, adj, parent):
                return True

    return False

def isTree(adj, V):

    parent = [-1] * V
    visited = set()

    if checkUndirectedLoop(0, visited, adj, parent):
        return False

    for currV in range(V):
        if currV not in visited:
            return False

    return True
  
