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

int hash(string str){
	int sum = 0;
	for (int i = 0; i < str.length(); i++) sum = sum * 17 + str[i];
	double B = sum * A;
	B = B - floor(B);
	return (int)(floor(B * numberOfBits));
}    

void makeBloomFilter(){
	ifstream infile;
	string word;

	infile.open("../programs/wordsEn.txt");
	if (!infile){
		cerr << " could not be opened " << endl;
		exit(1);
	}
	while (infile >> word){
		for (int i = 0; i < 7; i++){
			int biton = hash(word + endings.substr(i,1));
			BloomFilter[biton / 8] |= 1 << (7 - biton % 8);
		}
	}
	infile.close();
}
int main(){
	makeBloomFilter();

}
