# sudoku4.py CS2028 2016 Cheng
# uses collections.Counter, a subclass of dict, from Python 3.5.2
# tries to solve sudoku puzzles using rule1 and rule2 repeatedly

from collections import *

def readPuzzle():
	matrix = []
	filename = input("Please enter a Sudoku puzzle file name: ")
	file = open(filename, "r")
	for line in file:
		row = []
		for i in range(9):
			s = line[i * 2]
			if s == 'x':
				row.append(set(['1','2','3','4','5','6','7','8','9']))
			else:
				row.append(set([s]))
		matrix.append(row)
	file.close()
	return matrix

def getGroups(matrix):
	groups = []
	for i in range(9):
		group = []
		for j in range(9):
			group.append(matrix[i][j])
		groups.append(group)
	for i in range(9):
		group = []
		for j in range(9):
			group.append(matrix[j][i])
		groups.append(group)
	for i in range(3):
		for j in range(3):
			group = []
			for k in range(3):
				for l in range(3):
					group.append(matrix[i * 3 + k][j * 3 + l])
			groups.append(group)
	return groups

def rule1(group):
	changed = False
	for cell in group:
		count = 1
		for cell2 in group:
			# Changed (is subset of) to "cell2.issubset(cell)"
			if cell2 != cell and cell2.issubset(cell):
				count += 1
		if count == len(cell):
			for cell2 in group:
				if not cell2.issubset(cell) and not cell2.isdisjoint(cell):
					cell2.difference_update(cell)
					changed = True
	return changed

def rule2(group):
	changed = False
	cnt = Counter()
	for cell in group:
		cnt += Counter(cell)
	for item in cnt:
		if cnt[item] == 1:
			for cell in group:
				if item in cell and len(cell) > 1:
					cell.clear()
					cell.add(item)
					changed = True
	return changed

def reduceGroup(group):
	changed = False
	if rule1(group):
		changed = True
	if rule2(group) and not changed:
		changed = True
	return changed

def showMatrix(matrix):
	for i in range(9):
		for j in range(9):
			if len(matrix[i][j]) > 1:
				print('x', end=' ')
			else:
				item = matrix[i][j].pop()
				matrix[i][j].add(item)
				print(item, end=' ')
		print()
	print()		

def reduceGroups(groups):
	changed = False
	for group in groups:
		if reduceGroup(group):
			changed = True
	return changed

def reduce(groups, matrix):
	while reduceGroups(groups):
		showMatrix(matrix)
		
def main():
	matrix = readPuzzle()
	groups = getGroups(matrix)
	showMatrix(matrix)
	reduce(groups, matrix)

if __name__ == "__main__":
	main()
