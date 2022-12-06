"""
Input
One integer in the first line, stating the number of test cases, followed by a blank line. There will be not more than 20 tests.

For each test case, at the first line there are two positive integers m and n separated by a single space, 2 <= m,n <= 1000.
In the successive m-1 lines there are numbers x1, x2, ..., xm-1, one per line, 1 <= xi <= 1000. In the successive n-1 lines 
there are numbers y1, y2, ..., yn-1, one per line, 1 <= yi <= 1000.

The test cases will be separated by a single blank line.

Output
For each test case : write one integer - the minimal cost of breaking the whole chocolate into single squares.

Example
Input:
1

6 4
2
1
3
1
4
4
1
2

Output:
42
"""

def minCost(vertical,horizontal):

    vertical.sort(reverse = True)
    horizontal.sort(reverse = True)


    print("vertical :",vertical)
    print("horizontal :",horizontal)

    horiCount = 1
    vertiCount = 1

    i = 0
    j = 0

    cost = 0

    while i < len(vertical) and j < len(horizontal):

        if vertical[i] > horizontal[j]:
            cost += vertiCount * vertical[i]
            horiCount += 1
            i += 1
        
        else:
            cost += horiCount * horizontal[j]
            vertiCount += 1
            j += 1
        
    while i < len(vertical):
        cost += vertiCount * vertical[i]
        i += 1
    
    while j < len(horizontal):
        cost += horiCount * horizontal[j]
        j += 1
    
    return cost




test_cases = int(input())
for _ in range(test_cases):

    blank_line = input()
    m,n = map(int,input().split())

    vertical = []
    for i in range(m-1):
        vertical.append(int(input()))
    
    horizontal = []
    for j in range(n-1):
        horizontal.append(int(input()))
    
    print(minCost(vertical,horizontal))
