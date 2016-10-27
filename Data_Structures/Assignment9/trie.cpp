#include <iostream>
#include <fstream>
#include <string.h>
#include "trie.h"
using namespace std;

Trie trie;

void makeTrie(){
    ifstream infile;
    char word[100];

    infile.open("C:\\Users\\ndcho_000\\Documents\\assignment9_data_structures\\wordsEn.txt");
    if (!infile){
        cerr << " could not be opened " << endl;
        return;
    }
    while (infile >> word) trie.insert(strcat(word, "$"));
    infile.close();
}

void useTrie() {
    ifstream infile;
    char word[100];

    infile.open("C:\\Users\\ndcho_000\\Documents\\assignment9_data_structures\\names.txt");
    if (!infile){
        cerr << " could not be opened " << endl;
        return;
    }

    int n = 0;
    int m = 0;
    while (infile >> word) {
        n++;
        if (trie.contains(strcat(word, "$"))) {
            m++;
        }
    }

    infile.close();
    cout << "n: " << n << endl;
    cout << "m: " << m << endl;

}

int main(){
    makeTrie();
    useTrie();
}

