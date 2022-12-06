
def generate(currIndex,curr,arr,ans):

    if currIndex == len(arr):
        ans.append(curr)
        return

    generate(currIndex+1,curr+arr[currIndex],arr,ans)

    generate(currIndex+1,curr,arr,ans)



def countSubsets(arr,A,B):
    
    subsets = []
    generate(0,0,arr,subsets)
    count = 0
    
    for subset in subsets:
        if subset >= A and subset <= B:
            count += 1

    return count

arr = [1,-2,3]  # OUTPUT : 5
A = -1
B = 2

print(countSubsets(arr,A,B))

