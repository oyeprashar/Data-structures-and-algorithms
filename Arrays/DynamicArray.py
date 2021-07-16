# Dynamic array implemention
import ctypes
# this is being imported for making a raw array

class DynamicArray():
	# defining the arributes of this class
	def __init__(self):
		self.n = 0 # this is no of elements in our array
		self.capacity = 1 # default capacity of our array
		self.A = self.make_array(self.capacity) # a default array is created

	def __len__(self):
		return self.n

	def __getitem__(self,k):
		if not  0<= k < self.n:
			return IndexError("K is out of bounds")
		return self.A[k]

	def append(self,element):
		# this if statement would will increase the size in the array if there is 
		# no capacity and then lines after the if block will be executed that would
		# append the element at the last
		if self.n == self.capacity:
			self.resize(2*self.capacity)

		self.A[self.n] = element 
		self.n = self.n + 1

	def resize(self,new_capacity):
		# this function is used to copy all the new elements from old array to new aray
		B = self.make_array(new_capacity) # new array created with double capacity
		for k in range(self.n): # copying old elements to our new aray
			B[k] = self.A[k]
		self.A = B # finally size of array A is increased
		self.capacity = new_capacity # capacity is updated

	def make_array(self,new_capacity):
		# this function used ctypes to create a new array
		return (new_capacity * ctypes.py_object)()

arr = DynamicArray()
arr.append(1)
arr.append(2)
arr.append(2)
print(len(arr))
print(arr[0]) # we are able to fetch element of this array becuase we defined __getitem__ class