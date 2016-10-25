import trie

trie = trie.Trie()

def makeTrie():
	file = open('wordsEn.txt', 'r')
	for word in file:
		word = word[:len(word) - 1] + '$'
		trie.insert(word)
	file.close()

def useTrie():
	file = open('names.txt', 'r')
	n = 0
	m = 0
	for word in file:
		word = word[:len(word) - 1] + '$'
		n+=1
		if word in trie:
			m+=1
	file.close()
	print(n, m)


def checkSpelling():
	while True:
		word = input('Enter a word ')
		if len(word) < 1:
			break
		if not word + '$' in trie:
			print(word)

def main():
	makeTrie()
	checkSpelling()

if __name__ == "__main__":
	main()
