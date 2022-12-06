"""
              B(10,30)
                / \
               /   \
              /     \
             /   P   \      P'
            /         \
     A(0,0) ----------- C(20,0) 

area of triangle = abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2
"""

def check(triangleArray,P) -> bool:

  x1 = triangleArray[0][0]
  y1 = triangleArray[0][1]

  x2 = triangleArray[1][0]
  y2 = triangleArray[1][1]

  x3 = triangleArray[2][0]
  y3 = triangleArray[2][1]

  areaOfTriangle = abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))/2

  x = p[0]
  y = p[1]

  s1 = abs(x*(y2-y3)+x2*(y3-y)+x3*(y-y2))/2
  s2 = abs(x*(y2-y1)+x2*(y1-y)+x1*(y1-y))/2
  s3 = abs(x*(y3-y1)+x3*(y1-y)+x1*(y-y3))/2

  print(s1+s2+s3,areaOfTriangle)
  if s1+s2+s3 == areaOfTriangle:
    return "Inside"

  else:
    return "Outside"

triangle = [[0, 0], [20, 0], [10, 30]]
p = [10, 25]
print(check(triangle,p))



