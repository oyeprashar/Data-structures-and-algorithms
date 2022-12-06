# First Missing Positive

def find(arr):

    arr.sort()
    missing = 1

    for num in arr:
        if num == missing:
            missing += 1
        
    return missing