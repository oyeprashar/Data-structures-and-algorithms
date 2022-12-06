def minTime(a,t,e,x):

     time1 = [0] * len(a[0])
     time2 = [0] * len(a[1])

     time1[0] = a[0][0] + e[0]
     time2[0] = a[1][0] + e[1]

     for i in range(1,len(a[0])):

          time1[i] = min(time1[i-1] + a[0][i], time2[i-1] + t[1][i] + a[0][i])
          time2[i] = min(time2[i-1] + a[1][i], time1[i-1] + t[0][i] + a[1][i])

     time1[-1] += x[0]
     time2[-1] += x[1]

     return min(time1[-1],time2[-1])

a = [[4, 5, 3, 2],
     [2, 10, 1, 4]]
t = [[0, 7, 4, 5],
     [0, 9, 2, 8]]
e = [10, 12]
x = [18, 7]

print(minTime(a,t,e,x))




