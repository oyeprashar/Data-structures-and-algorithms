"""
runCustomerSimulation (2, “ABBAJJKZKZ”) should return 0
runCustomerSimulation (3, “GACCBDDBAGEE”) should return 1 as ‘D’ was not able to get any computer
runCustomerSimulation (3, “GACCBGDDBAEE”) should return 0
runCustomerSimulation (1, “ABCBCA”) should return 2 as ‘B’ and ‘C’ were not able to get any computer.
runCustomerSimulation(1, “ABCBCADEED”) should return 3 as ‘B’, ‘C’ and ‘E’ were not able to get any computer.
"""
def runCustomerSimulation(n,str1):
    
    visited = set()
    ansSet = set()

    for char in str1:

        if n == 0 and char not in visited:
            ansSet.add(char)

        elif char not in visited:
            n -= 1
            visited.add(char)

        elif char in visited:
            n += 1
        
    if len(ansSet) == 0:
        return 0    
    
    return " ".join(ansSet)


print(runCustomerSimulation(2, "ABBAJJKZKZ"))
print(runCustomerSimulation (3, "GACCBDDBAGEE"))

print(runCustomerSimulation (3, "GACCBGDDBAEE"))
print(runCustomerSimulation (1, "ABCBCA"))
print(runCustomerSimulation(1, "ABCBCADEED"))