class BinarySearchTree:
	class Node:
		def __init__(self,val,left=None,right=None):
			self.val = val
			self.left = left
			self.right = right

		def getVal(self):
			return self.val

		def setVal(self,newval):
			self.val = newval

		def getLeft(self):
			return self.left

		def getRight(self):
			return self.right

		def setLeft(self,newleft):
			self.left = newleft

		def setRight(self,newright):
			self.right = newright
            
		def __iter__(self):
			if self.left != None:
				for elem in self.left:
					yield elem
			yield self.val
			if self.right != None:
				for elem in self.right:
					yield elem

		def dfs(self,depth):
			if self.right != None:
				self.right.dfs(depth+1)
			for i in range(depth):
				print(' ', end=' ')
			print(self.val)
			if self.left != None:
				self.left.dfs(depth+1)

		def __repr__(self):
			return "BinarySearchTree.Node(" + repr(self.val) + "," + repr(self.left) + "," + repr(self.right) + ")"            
            
    # Below are the methods of the BinarySearchTree class. 
	def __init__(self, root=None):
		self.root = root

	def isEmpty(self):
		return self.root == None

	def insert(self,val):
		self.root = BinarySearchTree.__insert(self.root,val)

	def __insert(root,val):
		if root == None:
			return BinarySearchTree.Node(val)
		if val < root.getVal():
			root.setLeft(BinarySearchTree.__insert(root.getLeft(),val))
		else:
			root.setRight(BinarySearchTree.__insert(root.getRight(),val))
		return root

	def getRightmost(self):
		# !!!Changed parameter from professor's self.root to just self, might be wrong!!!
		return BinarySearchTree.__getRightmost(self.root)

	def __getRightmost(root):
		if root.getRight() == None:
			return root.getVal()
		else:
			# Original had no "BinarySearchTree.", made this change yourself
			return BinarySearchTree.__getRightmost(root.getRight())

	def delete(self,val):
		self.root = BinarySearchTree.__delete(self.root,val)

	def __delete(root,val):
		# tree is empty
		if root == None:
			return root
		# val smaller than root value
		if val < root.getVal():
			# !!!your code similar to that in __insert!!!
			root.setLeft(BinarySearchTree.__delete(root.getLeft(),val))
		# val larger than root value
		elif val > root.getVal():
			# !!!your code!!!
			root.setRight(BinarySearchTree.__delete(root.getRight(),val))
		# val == root value
		else:
			# no left child
			if root.getLeft() == None:
				# also no right child
				if root.getRight() == None:
					return None
				# has right child
				else:
					return root.getRight()
			# has left child but no right one
			elif root.getRight() == None:
				return root.getLeft()
			# has both children
			else:
				# !!!your code: find rightmost of left, assign it to root, delete it!!!
				left_val = root.getLeft()
				left_val_subtree = BinarySearchTree(left_val)
				rightmost_val_left = left_val_subtree.getRightmost()
				root.setVal(rightmost_val_left)

				# This statement was added due to flaw in Professor's suggested logic. Any
				# value on the left is assumed to be smaller than the root, but if you set
				# the root equal to the rightmost value on the left, then it will not delete
				# it. This flaw is counteracted by finding a value that is less than the
				# the root that isn't already in the tree, so that the __delete method
				# will work properly.
				if left_val.getLeft() == None and left_val.getRight() == None \
						and root.getLeft().getVal() == root.getVal():
					count = root.getLeft().getVal() - 1;
					while count in root:
						count -= 1
					root.setLeft(BinarySearchTree.Node(count))
					BinarySearchTree.__delete(root, count)
				else:
					BinarySearchTree.__delete(left_val_subtree.root, rightmost_val_left)

				return root
		return root		
        
	def __iter__(self):
		if self.root != None:
			return iter(self.root)
		else:
			return iter([])

	def showTree(self):
		if BinarySearchTree.isEmpty(self):
			print('The tree is empty.')
		else:
			self.root.dfs(0)

	def __contains__(self, val):
		return BinarySearchTree.__contains(self.root, val)

	def __contains(root, val):
		if root == None:
			return False
		if val < root.getVal():
			return BinarySearchTree.__contains(root.getLeft(),val)
		elif val > root.getVal():
			return BinarySearchTree.__contains(root.getRight(),val)
		else:
			return True
		

	def __str__(self):
		return "BinarySearchTree(" + repr(self.root) + ")"

def main():
	tree = BinarySearchTree()
	print('Binary Search Tree Program')
	print('--------------------------')
	while True:
		print('Make a choice...')
		print('1. Insert into tree.')
		print('2. Delete from tree.')
		print('3. Lookup value.')
		choice = input('Choice? ')
		if len(choice) == 0:
			break
		if choice == '1':
			while True:
				value = input('insert? ')
				if len(value) == 0:
					break
				tree.insert(int(value))
			tree.showTree()
		elif choice == '2':
			while True:
				value = input('delete? ')
				if len(value) == 0:
					break
				tree.delete(int(value))
			tree.showTree()
		elif choice == '3':
			while True:
				value = input('value? ')
				if len(value) == 0:
					break
				if int(value) in tree:
					print('Yes,', value, 'is in the tree')
				else:
					print('No,', value, 'was not in the tree')
		else:
			break
	tree.showTree()
if __name__ == "__main__":
	main()