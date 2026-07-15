left = [-1]
right = [100]

def push1(a,x):
    
    if left[0] + 1 < right[0]:
        left[0] += 1
        a[left[0]] = x
    
def push2(a,x):
    
    if left[0] < right[0] - 1:
        right[0] -= 1
        a[right[0]] = x
    
def pop1(a):
    
    if left[0] > -1:
        removed = a[left[0]]
        left[0] -= 1
        return removed
    
    else:
        return -1
        
def pop2(a):
    
    if right[0] < 100:
        removed = a[right[0]]
        right[0] += 1
        return removed
    
    else:
        return -1
