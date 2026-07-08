"""
Approach :

for num in arr:
    1. If the current number is neg, multiple it with product, keep track of count of negatives and the max of these negs
    2. If the number is zero, DO NOT MULTIPLE and keep a count
    3. Positives are always helpful and simply multiple them with the product

Approach to generate the final answer :
    1. if all elements were zero return 0
    2. if n - 1 elements were zero and one was neg, return zero
    3. if there were odd number of neg, that means we need to remove the max neg to maximise the product

    

"""



class Solution:
    def findMaxProduct(self, arr):
        
        if len(arr) == 1:
            return arr[0]

        # positive numbers are always useful in maximising the product
        product = 1
        maxNeg = -3**38
        negCount = 0
        zeroCount = 0

        for num in arr:

            # handling the negative numbers
            if num < 0:
                maxNeg = max(maxNeg, num)
                negCount += 1
                product *= num
                
            # handling zeroes
            elif num == 0:
                zeroCount += 1

            # handling positives
            else:
                product *= num
                
        if zeroCount == len(arr):
            return 0
        
        if zeroCount == len(arr) - 1 and negCount == 1:
            return 0
        
        if negCount % 2 == 1:
            product = product // maxNeg

        return product
        
