#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+2;
int vis[N];
vector<int> adj[N];

int main(){
        int n,m;
        cin>>n>>m;
        int x,y;
        for(int i=0;i<m;i++){
            cin>>x>>y;
            adj[x].push_back(y);
            adj[y].push_back(x);
        }
        queue<int> q;
        q.push(1);
        vis[1]=1;
        while(!q.empty()){
            int node=q.front();
            q.pop();
            cout<<node<<" ";
            for(int it:adj[node]){
                if(!vis[it]){
                    q.push(it);
                    vis[it]=1;
                }
            }
        }
    return 0;
}