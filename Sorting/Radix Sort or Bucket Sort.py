"""
==== ALGORITHM FOR RADIX SORT ====   
-> Radix sort uses counting sort 
-> Find the max element in the input array
-> jitne digits hai in the max element hum utne baar counting sort karengye aur array ko change kr dengye
-> now harr baar count sort happens for a digit place (left se we move to right after each interation in radix func)

Time Complexity: Worst case => O(n)| Average case => O(n) |Best case => O(n) |Space Complexity = O(n) |Inplace Sorting = NO | Stable = YES 
"""
def countingSort(arr,exp):
    count = [0] * 10 # since each digit can range from 0 to 9

    # generate count array
    for num in arr:
        index = num / exp
        count[int(index % 10)] +=1 

    # change count into cummulative sum array and it will contain the positions of each element (not index, index is pos - 1)
    prev  = count[0]
    for i in range(1,len(count)):
        count[i] += prev
        prev = count[i]

    output = [0] * (len(arr))

    # now use the cummulative count array to place number at their correct postion according to there current digit place

    curr = len(arr) - 1
    
    while curr != -1:
        element = arr[curr]
        index = element / exp
        count[int(index % 10)] -= 1
        j = count[int(index % 10)] 
        output[j] = element
        curr -= 1

    # copy this output array to the given input array
    for i in range(len(output)):
        arr[i] = output[i]


def radixSort(arr):
    """
    we have to sort according to the digit place going from left digit place to the right
    """

    maxElement = max(arr)
    exp = 1

    while maxElement // exp > 0: # jitne digits hai max element me utne baar chalega ga yeh while loop
        """
        yeha par floor div issliye kiya h because maan lo num = 981 and exp 1
        981/1 = 981.0
        981/10 = 98.1
        981/100 = 9.81
        981/1000 = 0.981 # this is useless so we did floor division and when the floor is zero its means we dont have any digit place left
        """
        countingSort(arr,exp)
        exp *= 10

arr = [178, 45, 75, 90,802, 24, 2, 66]
arr = [99,88,77,66,11]
radixSort(arr)
print(arr)






















