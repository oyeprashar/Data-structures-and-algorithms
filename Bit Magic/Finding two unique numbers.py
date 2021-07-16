class Solution:
    def singleNumber(self, arr):

        # Finding XOR of all numbers
        xorALL = arr[0]
        for i in range(1, len(arr)):
            xorALL ^= arr[i]

        # find the right most set bit in XORall

        check = xorALL
        i = 1

        while check > 0:
            if check & 1 == 1:
                break
            i += 1
            check = check >> 1

        # generate the mask
        mask = 1 << (i - 1)

        # now seperating num based on our mask and doinf their XOR
        num1 = 0
        num2 = 0

        for num in arr:
            if num & mask > 0:
                num1 ^= num
            else:
                num2 ^= num

        ans = []
        if num1 < num2:
            ans.append(num1)
            ans.append(num2)
        else:
            ans.append(num2)
            ans.append(num1)

        return ans


