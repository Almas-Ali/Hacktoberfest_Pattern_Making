#include <bits/stdc++.h>
using namespace std;

int main(void){
  int n = 100;
  for(double y = 0;y<n;y++){
  	int s = sin(y/n*10)*10 + 10;
  	int s2 = sin(y/n*10+3.14/2)*20 + 20;
  	for(int x = 0;x<s2;x++){
  		printf(" ");
  	}printf("*\n");
  }


  return 0;
}
