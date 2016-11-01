import heap2

names = []
counts = []
pctwhite = []
pctblack = []
pctapi = []

def readData():
	file = open('names.csv', 'r')
	file.readline()
	line = file.readline().strip()
	while line != "":
		cols = line.split(",")
		names.append(cols[0])
		counts.append(int(cols[1]))
		if (cols[2] == '(S)'):
			pctwhite.append(float(0))
		else:
			pctwhite.append(float(cols[2]))
		if (cols[3] == '(S)'):
			pctblack.append(float(0))
		else:
			pctblack.append(float(cols[3]))
		if (cols[4] == '(S)'):
			pctapi.append(float(0))
		else:
			pctapi.append(float(cols[4]))
		line = file.readline().strip()
	file.close()	

# Will find the top 20 most common names in general
def findMostPopular():
	heap = heap2.Heap(counts)
	heap.build()
	for i in range(20):
		top = heap.removeTop()
		print(names[top], counts[top])

# Will find the top 20 most common names for White Americans
def findMostPopularWhitePeople():
	print("\nWhite People: \n")
	values = []
	selected = []

	# Finds all names that are used among White Americans and
	# stores its "names" list index in "selected" list, then
	# finds how many White Americans have that name and
	# appends it to "values" list.
	for i in range(len(names)):
		if pctwhite[i] > 0:
			selected.append(i)
			values.append(counts[i] * pctwhite[i] // 100)

	# Create sorted heap with White American names and
	# print top 20.
	heap = heap2.Heap(values)
	heap.build()
	for i in range(20):
		top = heap.removeTop()
		print(names[selected[top]], values[top])

# Will find the top 20 most common names for Asian Pacific Islanders
def findMostPopularAPIPeople():
	print("\nAsian Pacific Islanders: \n")
	values = []
	selected = []

	# Finds all names that are used among Asian Pacific Islanders and
	# stores its "names" list index in "selected" list, then
	# finds how many Asian Pacific Islanders have that name and
	# appends it to "values" list.
	for i in range(len(names)):
		if pctapi[i] > 0:
			selected.append(i)
			values.append(counts[i] * pctapi[i] // 100)

	# Create sorted heap with Asian Pacific Islander names and
	# print top 20.
	heap = heap2.Heap(values)
	heap.build()
	for i in range(20):
		top = heap.removeTop()
		print(names[selected[top]], values[top])

def main():
	readData()
	findMostPopular()
	findMostPopularWhitePeople()
	findMostPopularAPIPeople()

if __name__ == '__main__':
	main()