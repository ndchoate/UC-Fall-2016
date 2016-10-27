class Trie:
	def __insert(node,item):
	# This is the recursive insert function.
	# 1. If the key is empty (i.e. no units are left in the key), 
	# return None as the empty node.
		if len(item) == 0:
			return None
	# 2. If the node is None then a new node is created with the next unit of the key 
	# and the rest of the key is inserted and added to the follows link.
		if node == None:
			return Trie.TrieNode(item[0], follows=Trie.__insert(None, item[1:])) 
	# 3. If the first unit of the key matches the unit of the current node, 
	# then the rest of the key is inserted into the follows link of the node.
		if item[0] == node.item:
			node.follows = Trie.__insert(node.follows, item[1:])
			return node
	# 4. Otherwise, the key is inserted into the next link of the node.
		node.next = Trie.__insert(node.next, item)
		return node

	def __contains(node,item):
	# This is the recursive membership test.
	# 1. If the length of the key is 0, then report success by returning True.
		if len(item) == 0:
			return True
	# 2. If the node we are looking at is None then report failure by returning False.
		if node == None:
			return False
	# 3. If the first unit of the key matches the unit in the current node, 
	#  then check membership of the rest of the key starting with the follows node.
		if item[0] == node.item:
			return Trie.__contains(node.follows, item[1:])
	# 4. Otherwise, check membership of the key starting with the next node in the trie.
		if item[0] != node.item:
			return Trie.__contains(node.next, item)

	class TrieNode:
		def __init__(self, item, next = None, follows = None):
			self.item = item
			self.next = next
			self.follows = follows

	def __init__(self):
		self.start = None

	def insert(self,item):
		self.start = Trie.__insert(self.start,item)

	def __contains__(self,item):
		return Trie.__contains(self.start,item)
