
def Swap(input, a, b):
	tmp = input[a]
	input[a] = input[b]
	input[b] = tmp

def StrPermulation(input, start, end):
	if start > end:
		return

	if start == end:
		print input

	for i in range(start, end + 1):
		Swap(input, start, i)
		StrPermulation(input, start + 1, end)
		Swap(input, start, i)

if __name__ == "__main__":
	strInput = ["a","b",'c',"d", "e", "f"]
	StrPermulation(strInput, 0, len(strInput) - 1)


	