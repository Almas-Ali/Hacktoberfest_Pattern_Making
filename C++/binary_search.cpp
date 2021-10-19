#include <iostream>
using namespace std;

int binary_search(int a[1000], int n, int key)
{
    int s = 0;
    int e = n - 1;

    while (s <= e)
    {
        int mid = (s + e) / 2;
        if (a[mid] == key)
        {
            return mid;
        }

        else if (a[mid] > key)
        {
            e = mid - 1;
        }

        else if (a[mid] < key)
        {
            s = mid + 1;
        }

    }

    cout<<"Element not found"<<endl;
    return 0;
}
int main()
{
    int n;
    cin >> n;
    int a[1000];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    int key;
    cin >> key;

    int element = binary_search(a, n, key);
    cout<<element;

    return 0;
}