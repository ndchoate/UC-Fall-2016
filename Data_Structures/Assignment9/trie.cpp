#include <iostream>
#include <fstream>
#include <string.h>
#include "trie.h"
using namespace std;

Trie trie;

void makeTrie(){
	ifstream infile;
	char word[100];

	infile.open("../programs/wordsEn.txt");
	if (!infile){
		cerr << " could not be opened " << endl;
		return;
	}
	while (infile >> word) trie.insert(strcat(word, "$"));
	infile.close();
}

int main(){
	makeTrie();
}

