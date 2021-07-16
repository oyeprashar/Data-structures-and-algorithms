def isValid(totalStudents,currNumOfStudents,totalCoupons,neededCoupons,couponsTaken):
	return currNumOfStudents * neededCoupons <= totalCoupons + ((totalStudents - currNumOfStudents) * couponsTaken)


def binarySearch(left,right,ans,totalStudents,totalCoupons,neededCoupons,couponsTaken):
	if left <= right:
		mid = (left + right) // 2

		if isValid(totalStudents,mid,totalCoupons,neededCoupons,couponsTaken) is True:
			#save this ans and move to right
			ans[0] = mid
			binarySearch(mid+1,right,ans,totalStudents,totalCoupons,neededCoupons,couponsTaken)

		else:
			binarySearch(left,mid-1,ans,totalStudents,totalCoupons,neededCoupons,couponsTaken)

def getMaxStudents(totalStudents,totalCoupons,neededCoupons,couponsTaken):
	left = 0
	right = NumOfStudents
	ans = [0]
	binarySearch(left,right,ans,totalStudents,totalCoupons,neededCoupons,couponsTaken)
	return ans[0]

NumOfStudents = 5
totalCoupons = 4
neededCoupons = 2
couponsTaken = 1
print(getMaxStudents(NumOfStudents,totalCoupons,neededCoupons,couponsTaken))
