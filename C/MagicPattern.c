#include <stdio.h>
 
void overLapping(int N, int matrix[100][100])
{
 
    int max, inc = 0, dec, start;
 
    // The size of matrix
    max = 2 * N - 1;
 
    // Fixing the range
    dec = max;
 
    // Overlapping value
    start = N;
 
    while (start != 0) {
        for (int row = 0; row < max; row++) {
            for (int col = 0; col < max; col++) {
                if (row == inc
                    || row == dec - 1
                    || col == dec - 1
                    || col == inc) {
 
                    matrix[row][col] = start;
                }
            }
        }
        start--;
        inc++;
        dec--;
    }
 
    // return matrix;
}
 
void DisplayMatrix(int matrix[][100], int max)
{
    // To display the overlapping matrix
    for (int row = 0; row < max; row++) {
        for (int col = 0; col < max; col++) {
            printf("%d ", matrix[row][col]);
        }
        printf("\n");
    }
}
 
// Driver code
int main()
{
    int N = 3;
 
    // Declaring the overlapping matrix
    int matrix[100][100];
 
    // Create the magical matrix
    overLapping(N, matrix);
 
    // Print the magical matrix
    DisplayMatrix(matrix, (2 * N - 1));
}

Output

 3 2 1 2 3
 2 2 1 2 2
 1 1 1 1 1
 2 2 1 2 2
 3 2 1 2 3

