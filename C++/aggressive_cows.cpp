#include <bits/stdc++.h>
using namespace std;



const int me = 100025;
const int mod = 0x3b9aca07;


int t, n, c;
int a[me];
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> t;
    while(t --){
        cin >> n >> c;
        for(int i = 0; i < n; i ++)
            cin >> a[i];
        
        sort(a, a + n);
        int low = 0, high = a[n-1], mid, best = 0;
        while(low <= high){
            mid = (low + high + 1) / 2;
            int cnt = 1, left = 0;
            for(int i = 1; i < n && cnt < c; i ++){
                if(a[i] - a[left] >= mid)
                    left = i, cnt ++;
            }
            if(cnt >= c){
                best = mid;
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        cout << best << endl;
    }
    
    return 0;
}