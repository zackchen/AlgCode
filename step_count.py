
def count(step_size):
	if step_size <= 0:
		return 0

	if step_size == 1:
		return 1

	if step_size == 2:
		return 2

	if step_size == 3:
		return 4

	return count(step_size - 1) + count(step_size - 2) + count(step_size -3)


cnts = count(4)
print cnts