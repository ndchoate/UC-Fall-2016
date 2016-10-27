#include <iostream>
#include <fstream>
#include <cstdlib>
#include <cmath>
#include <string>
using namespace std;

const int numberOfBytes = 131295;
const int numberOfBits = 1050360;
char BloomFilter[numberOfBytes];
const string endings = "0123456";
const double A = 0.6180339887;

int hash_instructor(string str){
    int sum = 0;
    for (int i = 0; i < str.length(); i++) sum = sum * 17 + str[i];
    double B = sum * A;
    B = B - floor(B);
    return (int)(floor(B * numberOfBits));
}

void makeBloomFilter(){
    ifstream infile;
    string word;

    infile.open("C:\\Users\\ndcho_000\\Documents\\assignment9_data_structures\\wordsEn.txt");
    if (!infile){
        cerr << " could not be opened " << endl;
        exit(1);
    }
    while (infile >> word){
        for (int i = 0; i < 7; i++){
            int biton = hash_instructor(word + endings.substr(i,1));
            BloomFilter[biton / 8] |= 1 << (7 - biton % 8);
        }
    }
    infile.close();
}

void useBloomFilter() {
    ifstream infile;
    string word;
    int n = 0;
    int m = 0;

    infile.open("C:\\Users\\ndcho_000\\Documents\\assignment9_data_structures\\names.txt");
    if (!infile){
        cerr << " could not be opened " << endl;
        exit(1);
    }

    while (infile >> word) {
        n++;
        bool spellError = false;
        for (int i = 0; i < 7; i++) {
            int biton = hash_instructor(word + endings.substr(i,1));
            int weird_int = BloomFilter[biton / 8] & 1 << (7 - biton % 8);
            if (weird_int == 0) {
                spellError = true;
            }
        }
        if (!spellError) {
            m++;
        }
    }

    infile.close();
    cout << "n: " << n << endl;
    cout << "m: " << m << endl;
}

int main(){
    makeBloomFilter();
    useBloomFilter();
}
