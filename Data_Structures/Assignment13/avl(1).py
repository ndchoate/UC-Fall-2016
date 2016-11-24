# avl.py CS2028 2016 cheng
# implementing AVL tree with search and insert
# and insert random integers to the tree and display the tree

import linkedliststackqueue2, random

class AVLNode:
	def __init__(self, item, balance = 0):
		self.item = item
		self.left = None
		self.right = None
		self.balance = balance

	def rotateLeft(self):  # precondition: right child exists
		print('rotateLeft', self.item)
		child = self.right
		self.right = child.left
		self.balance = 0
		child.left = self
		child.balance = 0
		return child

	# Your code
	def rotateRight(self):  # precondition: left child exists
		print('rotateRight', self.item)
		child = self.left
		self.left = child.right
		self.balance = 0
		child.right = self
		child.balance = 0
		return child

	def rotateLeftThenRight(self): # precondition: left child and its right child exist
		print('rotateLeftThenRight', self.item)
		CBalance = self.left.right.balance
		self.left = self.left.rotateLeft()
		newTree = self.rotateRight()
		if CBalance == -1:
			newTree.right.balance = 1
		elif CBalance == 1:
			newTree.left.balance = -1
		return newTree

	# Your code
	def rotateRightThenLeft(self): # precondition: right child and its left child exist
		print('rotateRightThenLeft', self.item)
		CBalance = self.right.left.balance
		self.right = self.right.rotateRight()
		newTree = self.rotateLeft()
		if CBalance == -1:
			newTree.right.balance = 1
		elif CBalance == 1:
			newTree.left.balance = -1
		return newTree

	def dfs(self,depth):  # dfs in binarysearchtree.py but we also print the balance
		if self.right != None:
			self.right.dfs(depth+1)
		for i in range(depth):
			print(' ', end=' ')
		print(self.item, self.balance)
		if self.left != None:
			self.left.dfs(depth+1)


class AVLTree:
	def __init__(self):
		self.root = None

	def insert(self, newItem):
		print('inserting', newItem)

		# Step 1. call search and get the path in theStack
		pivot, theStack, found = self.search(newItem)
		if pivot == None:  # print out the pivot = closest ancester with a balance
			print('no pivot')
		else:
			print('pivot is', pivot.item)

		# Step 2: if found, no insertion and return
		if found: 
			print('found and no insertion')
			return

		# Step 3: make a node holding newItem and call it the child
		child = AVLNode(newItem)  
		grandchild = child  # for future use

		# Step 4: if stack is empty, then the tree is empty, set the root and return
		if theStack.isEmpty():
			self.root = child
			return

		# Step 5: pop the parent out of the stack and 
		# make the child either the left child or the right child of the parent.
		parent = theStack.pop()
		if newItem < parent.item:
			parent.left = child
		else:
			parent.right = child

		# Step 6: while parent is not the pivot (its balance is 0) do the following.
		while parent != pivot:

			# Step 6.1: parent�s balance is assigned with -1 or 1, 
			# depending on whether the child is its left or right child
			if parent.left == child:
				parent.balance = -1
			else:
				parent.balance = 1

			# Step 6.2: if stack is empty, there is no pivot and this is case 1 and return
			# Your code
			if theStack.isEmpty():
				return

			# Step 6.3: call child grandchild, parent child, 
			# and pop the new parent from the stack
			### your code for Step 6.3

			# !!!Issues most likely here!!!
			grandchild = child
			child = parent
			parent = theStack.pop()


		# if the child is the left child of the parent and
		if parent.left == child:

		# Step 7: parent�s balance is 1, it is case 2, make parent�s balance zero and return
			if parent.balance == 1: # case 2
				print('case 2')				
				### Your code for Step 7
				parent.balance = 0
				return
			else:  # case 3

				# Step 8: if grandchild is the left child of the child, it is case 3A,
				#  do a right rotation on the parent and call the result newTree
				if child.left == grandchild:  # case 3A
					print('case 3A')
					newTree = parent.rotateRight()

				# Step 9: if grandchild is the right child of the child, it is case 3B,
				#  rotate left and then right on the parent and call the result newTree

				else: # case 3B
					print('case 3B')
					### Your code for Step 9
					newTree = parent.rotateLeftThenRight()

		else:  # the mirror image
			### Your code for Steps 7, 8, and 9
			if parent.balance == -1:
				print('case 2')
				parent.balance = 0
				return
			else:
				if child.right == grandchild:
					print('case 3A')
					newTree = parent.rotateLeft()

				else:
					print('case 3B')
					newTree = parent.rotateRightThenLeft()

		# Step 10: if stack is empty, then the pivot is the root and 
		# make newTree the new root and return

		if theStack.isEmpty():
			self.root = newTree
		else:
	
			# Step 11: get grandparent out of the stack and check to see 
			# if the left or right child needs to be replaced with newTree
			### Your code for Step 11
			grandparent = theStack.pop()
			grandparent_item = grandparent.item
			if newTree.item < grandparent_item:
				grandparent.left = newTree
			elif newTree.item > grandparent_item:
				grandparent.right = newTree


	def search(self, newItem):  # essentially binary search
		theStack = linkedliststackqueue2.Stack()  # contains the path
		current = self.root
		pivot = None
		while current != None:
			theStack.push(current)
			if current.balance != 0:
				pivot = current
			if newItem == current.item:
				return (pivot, theStack, True)
			elif newItem < current.item:
				current = current.left
			else:
				current = current.right
		return (pivot, theStack, False)  

	def showTree(self):  # the same as in binarysearchtree.py
		if self.root == None:
			print('The tree is empty.')
		else:
			self.root.dfs(0)
		print()


def main():
	tree = AVLTree()
	for i in range(100):  # randomly generate 100 integers and insert them into the tree
		newItem = random.randint(0, 99)
		tree.insert(newItem)
		tree.showTree()

if __name__ == "__main__":
	main()

