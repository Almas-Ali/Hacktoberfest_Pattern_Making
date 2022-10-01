#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    // The size of matrix.
    int N;
    cin>>N;
    vector<vector<int>> matrix(N, vector<int>(N));

    // Input the elements of matrix;
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cin>>matrix[i][j];
        }
    }

    // Rotation Algorithm

    for(int i=0; i<N; i++) {
        for(int j=0; j<i; j++) {
            swap(matrix[i][j], matrix[j][i]);
        }
    }

    for(int i=0; i<N; i++) {
        reverse(matrix[i].begin(), matrix[i].end());
    }

    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            cout<<matrix[i][j]<<' ';
        }
        cout<<'\n';
    }

    return 0;
}