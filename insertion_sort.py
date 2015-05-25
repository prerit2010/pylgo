num_array = list()
n = int(raw_input("Enter the number of elements :"))

for i in range(n):
	num_array.append(int(raw_input("Number : ")))

print "Unsorted array : ", num_array, "\n"

#Insertion Sort
for i in range(1,n):
	j=i
	while j > 0 and num_array[j-1] > num_array[j]:
		temp = num_array[j]
		num_array[j] = num_array[j-1]
		num_array[j-1] = temp
		j = j-1
	print "Iteration " , i+1, " : ",num_array

print "\nSorter array : " , num_array