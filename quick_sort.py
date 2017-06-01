def QuickSort(input, start, end):
	mid = Partition(input, start, end)
	if mid != -1:
		QuickSort(input, start, mid -1)
		QuickSort(input, mid + 1, end)

	

def Partition(input, start, end):

	if start >= end:
		return -1

	flag = input[start]
	i = start
	j = end

	while j > i:
		while input[j] >= flag and j > i:
			j -= 1
		if j > i:
			input[i] = input[j]
			i += 1
		while input[i] <= flag and j > i:
			i += 1
		if j > i:
			input[j] = input[i]
			j -= 1
	input[j] = flag
	return j

if __name__ == "__main__":
	input = [10,9,8,7,6,5,4,3,2,1]
	QuickSort(input, 0, len(input) - 1)
	print input


