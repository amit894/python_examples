# Python3 program to find positions
# of zeroes flipping which produces
# maximum number of xonsecutive 1's

# m is maximum of number zeroes allowed
# to flip, n is size of array
def findZeroes(arr, n, m) :

	# Left and right indexes of current window
	wL = wR = 0

	# Left index and size of the widest window
	bestL = bestWindow = 0

	# Count of zeroes in current window
	zeroCount = 0

	# While right boundary of current
	# window doesn't cross right end
	while wR < n:

		# If zero count of current window is less than m,
		# widen the window toward right
		if zeroCount <= m :
			if arr[wR] == 0 :
				zeroCount += 1
			wR += 1

		# If zero count of current window is more than m,
		# reduce the window from left
		if zeroCount > m :
			if arr[wL] == 0 :
				zeroCount -= 1
			wL += 1

		# Updqate widest window if
		# this window size is more
		if (wR-wL > bestWindow) and (zeroCount<=m) :
			bestWindow = wR - wL
			bestL = wL

	# Print positions of zeroes
	# in the widest window
	for i in range(0, bestWindow):
		if arr[bestL + i] == 0:
			print (bestL + i, end = " ")

# Driver program
arr = [1, 0, 0, 1, 1, 0, 1, 0, 1, 1]
m = 2
n = len(arr)
print ("Indexes of zeroes to be flipped are", end = " ")
findZeroes(arr, n, m)

# This code is contributed by Shreyanshi Arun.
