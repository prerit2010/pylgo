num_array = list()
n = int(raw_input("Enter the number of elements :"))

for i in range(n):
	num_array.append(int(raw_input("Number : ")))

print "Unsorted array : ", num_array, "\n"

#Selection Sort
for i in range(n-1):
	small = num_array[i]
	flag = 0				
	for j in range(i+1,n):
		if num_array[j] < small :
			small = num_array[j]
			index = j
			flag = 1 		# smaller element found
	if flag == 1 :
		temp = num_array[i]
		num_array[i] = num_array[index]
		num_array[index] = temp
	print "Iteration " , i+1, " : ",num_array

print "\nSorter array : " , num_array