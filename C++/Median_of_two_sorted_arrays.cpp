// Leetcode : (Hard Problem) 4. Median of Two Sorted Arrays
// Link : https://leetcode.com/problems/median-of-two-sorted-arrays/


#include<bits/stdc++.h>
using namespace std; 

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        int m = nums1.size() ; 
        int n = nums2.size() ; 
        
        vector<int> merge ; 
        int i = 0 ; 
        int j = 0 ; 
        
        sort(nums1.begin() , nums1.end()); 
		sort(nums2.begin() , nums2.end()); 
        
        
        while(i<m && j<n){
            if(nums1[i] == nums2[j]){
                merge.push_back(nums1[i]); 
                merge.push_back(nums2[j]);
                i++ ; 
                j++ ; 
            }
            
            else if(nums1[i] < nums2[j]){
                merge.push_back(nums1[i]);
                i++; 
            }
            
            else if(nums1[i] > nums2[j]){
                merge.push_back(nums2[j]);
                j++; 
            }
        }
        // cout << i << "  " << j << endl ; 
        if(i!=(m)){
            for(int j = i; j < m ; j++){
                merge.push_back(nums1[j]); 
            }
        }
        
        if(j!=(n)){
            for(int k = j ; k < n ; k++){
                merge.push_back(nums2[k]); 
            }
        }

        // for(auto & i : merge) cout << i << " "  ; 
        // 	cout << endl ; 
           int s = n+m ;
           
           if((s)%2 ==0 ){
               double d = merge[(s/2)-1] + merge[(s/2)] ; 
               return d/2 ;
           }
           else{
               return merge[(s/2)]*1.0;
           }
               
    }


int main(){
    int n1 , n2 ; 
    cout << "Enter the size of the first vector : " ; 
    cin >> n1 ; 
    vector<int> vec1(n1) ; 
    for (int i = 0; i < n1; i++)
    {
        cout << "Enter the element for vector 1 : " ;
        cin >> vec1[i] ; 
        cout << endl ; 
    }
    cout << "Enter the size of the second vector : " ; 
    cin >> n2 ; 
    vector<int> vec2(n2) ; 
    for (int i = 0; i < n2; i++)
    {
        cout << "Enter the element for vector 2 : " ;
        cin >> vec2[i] ; 
        cout << endl ; 
    }


    double ans = findMedianSortedArrays(vec1 , vec2) ; 
    cout << "The median of the arrays is " << ans << endl ; 

    return 0;
}