
a = [1,4, 5, 8, 8, 8]
b = [2, 8, 9, 9, 9]

# find the maximum balls that we can collect
# we can switch the array at the common element

i = j = 0
sum1 = sum2 = res = 0

# WRITE THIS DOWN IN THE NOTES <- IMPORTANT ->
# why are we adding the smaller element to our sum1 or sum2, because common element ke phele saare element usse small hi rahengye and iss tareeke se we can maintain sum1
# and sum2 for element till the common element also pointers i,j can be maintained on these arrays

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        sum1 += a[i]
        i += 1

    elif b[j] < a[i]:
        sum2 += b[j]
        j += 1

    elif a[i] == b[j]:
        res = max(sum1,sum2) + a[i]
        i += 1; j += 1;
        p = a[i]

        # check if the last common element is repeating in both arrays
        # if it repeats then add it to our ans and increment i and j accordingly

        while i < len(a) and a[i] == p:
            res += a[i]
            i += 1

        while j < len(b) and b[j] == p:
            res += b[j]
            j += 1

        sum1 = sum2 = 0


# check for ending elements and left elements
while i < len(a):
    sum1 += a[i]
    i += 1

while j < len(b):
    sum2 += b[j]
    j += 1

res += max(sum1,sum2)

print(res)


