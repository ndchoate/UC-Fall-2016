# sudoku5.py CS2028 2016 Cheng
# tries to solve sudoku puzzles using rule1 and rule2 repeatedly
# then depth-first search is used
from collections import *
import copy

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
	changed = 0
	for cell in group:
		count = 1
		for cell2 in group:
			if cell2 != cell and cell2 <= cell:
				count += 1
		if count == len(cell):
			for cell2 in group:
				if not cell2 <= cell and not cell2.isdisjoint(cell):
					cell2 -= cell
					changed = 1
		elif count > len(cell):
			return -1
		else:
			pass
	return changed

def rule2(group):
	changed = 0
	cnt = Counter()
	for cell in group:
		cnt += Counter(cell)
	for item in cnt:
		if cnt[item] == 1:
			for cell in group:
				if item in cell and len(cell) > 1:
					cell.clear()
					cell.add(item)
					changed = 1
	return changed

def reduceGroup(group):
	changed = 0
	ret = rule1(group) 
	if ret == 1:
		changed = 1
	elif ret == -1:
		return -1
	if rule2(group) == 1 and changed == 0:
		changed = 1
	return changed

def showMatrix(matrix, depth):
	for i in range(9):
		for d in range(depth):
			print(' ', end=' ')
		for j in range(9):
			if len(matrix[i][j]) > 1:
				print('x', end=' ')
			elif len(matrix[i][j]) == 0:
				print(' ', end=' ')
			else:
				item = matrix[i][j].pop()
				matrix[i][j].add(item)
				print(item, end=' ')
		print()
	print()		

def reduceGroups(groups):
	changed = 0
	for group in groups:
		ret = reduceGroup(group)
		if ret == 1:
			changed = 1
		elif ret == -1:
			return -1
	return changed

def reduce(matrix):
	changed = 1
	groups = getGroups(matrix)
	while changed == 1:
		changed = reduceGroups(groups)
	if changed == -1:
		return -1
	else:
		return 0

def solutionViable(matrix):
	for i in range(9):
		for j in range(9):
			if len(matrix[i][j]) == 0:
				return False
	return True

def solutionOK(matrix):
	for i in range(9):
		for j in range(9):
			if len(matrix[i][j]) > 1:
				return False
	return True

def solve(matrix, depth):
	ret = reduce(matrix)
	if ret == -1:
		return None
	showMatrix(matrix, depth)
	if not solutionViable(matrix):
		return None
	if solutionOK(matrix):
		return matrix
	print("Searching...")
	found = False
	for i in range(9):
		for j in range(9):
			if len(matrix[i][j]) > 1:
				found = True
				break
		if found:
			break
	if not found:
		return None
	for k in matrix[i][j]:
		mcopy = copy.deepcopy(matrix)
		mcopy[i][j] = set([k])
		result = solve(mcopy, depth + 1)
		if result != None:
			return result
	return None
		
def main():
	matrix = readPuzzle()
	showMatrix(matrix, 0)
	print("Begin Solving")
	matrix = solve(matrix, 0)
	if matrix == None:
		print("No Solution Found!!!")
		return
	showMatrix(matrix, 0)

if __name__ == "__main__":
	main()
