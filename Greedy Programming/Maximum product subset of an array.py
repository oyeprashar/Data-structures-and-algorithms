def maxProduct(arr):

    neg_count = 0
    zero_count = 0
    product = 1
    max_neg = -3**38

    for num in arr:

        if num < 0:
            max_neg = max(num,max_neg)
            product *= num
            neg_count += 1

        elif num == 0:
            zero_count += 1

        else:
            product *= num 


    if zero_count == len(arr):
        return 0

    if zero_count == len(arr)-1 and neg_count == 1:
        return 0

    if neg_count % 2 != 0:
        product /= max_neg

    return product
    
    
arr = [-1, -1, -2, 4, 3]
# arr = [ -1, 0]
# arr = [0,0,0]
print(maxProduct(arr))