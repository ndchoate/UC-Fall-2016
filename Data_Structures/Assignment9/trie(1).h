class TrieNode{
public:
	char val;
	TrieNode *next;
	TrieNode *follows;
	TrieNode(char v, TrieNode* n = 0, TrieNode* f = 0): val(v), next(n), follows(f){}
};

class Trie{
	TrieNode *start;
	TrieNode * __insert(TrieNode*, char*);
	bool __contains(TrieNode*, char*);
public:	
	Trie(){ start = 0; }
	void insert(char *s){ start = __insert(start, s); }
	bool contains(char *s){ return __contains(start, s); }
};

TrieNode* Trie::__insert(TrieNode* node, char* s){
	if (*s) if (node){  
		if (*s == node->val) node->follows = Trie::__insert(node->follows, s+1); // case 3
		else node->next = Trie::__insert(node->next, s); // case 4
		return node;
		}else return new TrieNode(*s, 0, Trie::__insert(0, s+1)); // case 2
	else return 0;  // case 1
}

bool Trie::__contains(TrieNode* node, char* s){
	if (*s) if (node)
		if (*s == node->val) return Trie::__contains(node->follows, s+1); // case 3
		else return Trie::__contains(node->next, s); // case 4
		else return 0; // case 2
	else return !node;  // case 1
}
