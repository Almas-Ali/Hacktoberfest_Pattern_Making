#include<iostream>
using namespace std;

void rectangle(int x, int y){
	for(int i=0;i<x;i++){
		for(int j=0;j<y;j++){
			cout<<"*";
		}
		cout<<endl;
	}
}

int main(){
	int length,breadth;
	cin>>length>>breadth;
	rectangle(length,breadth);
}
