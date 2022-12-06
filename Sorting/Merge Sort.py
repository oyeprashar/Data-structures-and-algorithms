"""
==== ALGORITHM FOR MERGE SORT ====
-> Divide the array into two halves, leftHalf and rightHalf
-> when they cannot be divided then we merge them overwriting the array jisske liye left and right was called
-> aise hi main array ka left and right hum break akrengye ge aur jaise hi len 1 aagye toh merge kr dengye 
- > iss tareese se main array ka left and right part mill jayega and we merge them and overwrite the main array

Time Complexity: Worst case => O(nlogn)| Average case => O(nlogn)|Best case => O(nlogn)|Space complexity = O(n)| Inplace Sorting = NO | Stable = YES 


"""
def mergeSort(arr):
	if len(arr) == 1:
		return # isska aage smaller arrays me break nhi ho sakta

	mid = len(arr) // 2

	leftHalf = arr[:mid]
	rightHalf = arr[mid:]

	mergeSort(leftHalf)  # this modifies the leftHalf array
	mergeSort(rightHalf) # this modifies the rightHalf array

	i = j = k = 0  # yeha pr confuse hone ki baat nhi hai, jo array call me aai h usse manupulate kr rhe h

	while i < len(leftHalf) and j < len(rightHalf):
		if leftHalf[i] < rightHalf[j]:
			arr[k] = leftHalf[i]
			i += 1
		else: 
			arr[k] = rightHalf[j]
			j += 1

		k += 1

	# iss while ke niche aane ka matab h isski koi ek condition ya dono condition False hui hogi
	# isska matlab hai ki ya toh left waali array khatam hai ya fir right waali aaray khatam hai
	# dono ko ek baar check kr lete h aur jissme kuch mill jaye usse daal dene merged waale array me

	while i < len(leftHalf):
		arr[k] = leftHalf[i]

		i += 1
		k += 1

	while j < len(rightHalf):
		arr[k] = rightHalf[j]
		j += 1
		k += 1

arr = [99,88,77,66,11]
mergeSort(arr)
print(arr)







































