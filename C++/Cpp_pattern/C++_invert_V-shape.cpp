#include <iostream>
using namespace std;
/*
    *
   * *
  *   *
 *     *
*       *
*/
int main(){
    cout << "--->";
    int a;
    cin >> a;
    for(int i =0;i<a;i++){
        for(int j = 0;j<a-i-1;j++){
            cout << " ";
        }
        cout << "*";
        for(int k =0;k<2*(i)-1;k++){
            cout << " ";
        }
        if(i!=0){
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}