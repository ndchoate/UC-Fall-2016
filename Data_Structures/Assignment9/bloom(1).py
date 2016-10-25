numberOfBytes = 131295
numberOfBits = 1050360
BloomFilter = bytearray(numberOfBytes)
endings = '0123456'

def makeBloomFilter():
	file = open('wordsEn.txt', 'r')
	for word in file:
		word = word[:len(word) - 1]
		for i in range(7):
			biton = hash(word + endings[i]) % numberOfBits
			BloomFilter[biton // 8] |= 1 << (7 - biton % 8)
	file.close()

def useBloomFilter():
	file = open('names.txt', 'r')
	n = 0
	m = 0
	for word in file:
		word = word[:len(word) - 1]
		n+=1
		spellerror = False
		for i in range(7):
			biton = hash(word + endings[i]) % numberOfBits
			if BloomFilter[biton // 8] & (1 << (7 - biton % 8)) == 0:
				spellerror = True
		if not spellerror:
			m+=1
	file.close()
	print(n, m)

def checkSpelling():
	while True:
		word = input('Enter a word ')
		if len(word) < 1:
			break
		spellerror = False
		for i in range(7):
			biton = hash(word + endings[i]) % numberOfBits
			if BloomFilter[biton // 8] & (1 << (7 - biton % 8)) == 0:
				spellerror = True
		if spellerror:
			print(word)

def main():
	makeBloomFilter()
	checkSpelling()

if __name__ == "__main__":
	main()
