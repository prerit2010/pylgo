num_array = list()
n = int(raw_input("Enter the number of elements :"))

for i in range(n):
	num_array.append(int(raw_input("Number : ")))

print "Unsorted array : ", num_array, "\n"

#Bubble Sort
for i in range(n):
	flag = 0
	for j in range(1,n):
		if num_array[j] < num_array[j-1]:
			temp = num_array[j]
			num_array[j] = num_array[j-1]
			num_array[j-1] = temp
			flag = 1
			print num_array
	if flag == 0 :
		break
	else:	
		print "Iteration " , i+1, " : ",num_array

print "\nSorter array : " , num_array