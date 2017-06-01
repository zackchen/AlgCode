def mergeSort(input, begin, mid, end):
	outputA = mergeSort(input, begin, (mid-begin/2), mid)
	outputB = mergeSort(input, mid, (end-mid/2), end)

def merge(inputA, input):
	output = [0 for x in range(0, end - begin + 1)]
	index = 0
	indexA = begin
	indexB = mid
	while indexA < mid and indexB <= end:
		if input[indexA] <= input[indexB]:
			output[index] = input[indexA]
			indexA += 1
		else:
			output[index] = input[indexB]
			indexB += 1
		index += 1
	while indexA < mid:
		output[index] = input[indexA]
		index += 1
		indexA += 1
	while indexB <= end:
		output[index] = input[indexB]
		index += 1
		indexB += 1

	return output




if __name__ == "__main__":
	input = [1,3,5,7,9,2,4,6,8,10]
	# print input
	mergeSort(input)
	print input

