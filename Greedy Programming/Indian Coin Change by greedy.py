# Please note that greedy should not be used as it may FAIL!
# Use dyanamic programming to solve coin change as greedy fails for some test cases
def binarySearch(left,right,coinList,currAmount,ans):
    if left <= right:
        mid =(left + right) // 2

        if coinList[mid] <= currAmount:
            ans[0] = coinList[mid]
            # moving right to maximize it
            return binarySearch(mid+1,right,coinList,currAmount,ans) 
        else:
            return binarySearch(left,mid-1,coinList,currAmount,ans) # agar mid bada h currAmount se to move left

def coinChange(coinList,amount):

    n = 0
    coinList = sorted(coinList)
    while amount != 0:
        left = 0
        right = len(coinList) - 1
        ans = [0]
        binarySearch(left,right,coinList,amount,ans)
        coin = ans[0]
        amount -= coin
        n += 1


    return n
        
coinList = [20,10,5,2]
a = 39
print(coinChange(coinList,a))
# left = 0; right = len(coinList)-1; currAmount=39; ans = [0]
# binarySearch(left,right,coinList,currAmount,ans)
# print(ans[0])