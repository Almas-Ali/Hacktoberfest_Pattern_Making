#include<bits/stdc++.h>
using namespace std;

void floodfill(vector<vector<int>> maze, int sr, int sc, string asf){
    if(sr==maze.size()-1 && sc==maze[0].size()-1){
        cout << asf << endl;
        return;
    }
    if(sr > 0 && maze[sr-1][sc] == 0){
        maze[sr][sc] = 1;
        floodfill(maze, sr-1, sc, asf+"t");
    }
    if(sc < maze[0].size()-1 && maze[sr][sc+1] == 0){
        maze[sr][sc] = 1;
        floodfill(maze, sr, sc+1, asf+"r");
    }
    if(sr < maze.size()-1 && maze[sr+1][sc] == 0){
        maze[sr][sc] = 1;
        floodfill(maze, sr+1, sc, asf+"d");
    }
    if(sc > 0 && maze[sr][sc-1] == 0){
        maze[sr][sc] = 1;
        floodfill(maze, sr, sc-1, asf+"l");
    }
}


int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int n, m;
    cin >> n >> m;
    // cout << n << m << endl;
    vector<vector<int>> v(n, vector<int> (m));
    for(int i = 0; i < v.size(); i++){
        for(int j = 0; j < v[i].size(); j++){
            cin  >> v[i][j];
        }
    }
    // for(int i = 0; i < v.size(); i++){
    //     for(int j = 0; j < v[i].size(); j++){
    //         cout  <<  v[i][j]  << " ";
    //     }cout << endl;
    // }
    // cout << "Ans: " << endl;
    floodfill(v, 0, 0, "");
    return 0;
}
