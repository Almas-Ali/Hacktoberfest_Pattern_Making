#include<bits/stdc++.h> 
using namespace std; 

 
class Solution
{
public:
    void subsets(vector<int>&arr,int N,int index,int sum,vector<int>&v)
    {
            if(index==N)
            {
            v.push_back(sum);
            return ;
            }
        
        //pick the element
        subsets(arr,N,index+1,sum+arr[index],v);
        
        
        
        //Dont pick the element
        subsets(arr,N,index+1,sum,v);
        
        
    }

    vector<int> subsetSums(vector<int> arr, int N)
    {
        vector<int>v;
        subsets(arr,N,0,0,v);
        sort(v.begin(),v.end());
        return v;
        
    }
};

// { Driver Code Starts.
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int N;
        cin>>N;
        vector<int> arr(N);
        for(int i = 0 ; i < N ; i++){
            cin >> arr[i];
        }
        Solution ob;
        vector<int> ans = ob.subsetSums(arr,N);
        sort(ans.begin(),ans.end());
        for(auto sum : ans){
            cout<< sum<<" ";
        }
        cout<<endl;
    }
    return 0;
}
