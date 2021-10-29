#include<bits/stdc++.h>
using namespace std;

// undirected graph formation
void addEdge(vector<int> graph[],int a,int b)
{
    graph[a].push_back(b);
    graph[b].push_back(a);
}

void bfs(vector<int> graph[],int start)
{
    queue<int> q;
    vector<bool> visited(graph->size(),false);
    q.push(start);
    visited[start] = true;

    vector<int>::iterator i;
    while(!q.empty())
    {
        int v = q.front();
        cout<<v<<" ";
        q.pop();
        for(i = graph[v].begin();i!=graph[v].end();i++)
        {
            if(!visited[*i])
            {
                q.push(*i);
                visited[*i] = true;

            }
        }

    }
}
int main()
{
    int V = 10;
    vector<int> graph[V];

    //input the values to form graph
    addEdge(graph,0,1);
    addEdge(graph,0,4);
    addEdge(graph,2,3);
    addEdge(graph,0,2);
    addEdge(graph,2,5);
    addEdge(graph,2,7);
    addEdge(graph,2,8);
    addEdge(graph,5,1);
    addEdge(graph,5,8);
    addEdge(graph,8,5);
    addEdge(graph,8,2);
    cout<<"The Output of BFS is\n";
    bfs(graph,0);
}