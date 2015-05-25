num_array = list()
n = int(raw_input("Enter the number of elements : "))

for i in range(n):
	num_array.append(int(raw_input("num :")))

print "Array :" , num_array

num = int(raw_input("Enter the number to be searched  : "))
first = 0
last = n -1
mid = (first+last)/2

while first <= last :
	if num < num_array[mid]:
		last = mid - 1
	elif num > num_array[mid]:
		first =	mid + 1
	else:
		print "Number found at Position " , mid+1, ",  " , num_array[mid]
		break
	mid = (first+last)/2

if(first>last):
	print "Number not in the list"