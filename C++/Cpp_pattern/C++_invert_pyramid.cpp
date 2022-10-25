#include <iostream>
using namespace std;
/*
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * * 
        * 
*/
main(){
    cout << "--->";
    int a;
    cin >> a;
    for(int i=0;i<a;i++){
        for(int space=0;space<2*i;space++){
            cout << " ";
        }
        for(int star=0;star<2*(a-i)-1;star++){
            cout << "* ";
        }
        cout << "\n";
    }
}