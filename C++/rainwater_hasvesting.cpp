#include <iostream>
using namespace std;

int calc_water(int a[1000000], int n)
{
    int max_left = 0;
    int max_right = 0;

    int lo = 0;
    int hi = n - 1;
    int water = 0;

    while (lo <= hi)
    {

        if (a[lo] < a[hi])
        {
            if (a[lo] > max_left)
            {
                max_left = a[lo];
            }

            else
            {
                water += max_left - a[lo];
            }
            lo++;
        }

        else
        {
            if (a[hi] > max_right)
            {
                max_right = a[hi];
            }

            else
            {
                water += max_right - a[hi];
            }
            hi--;
        }
    }

    return water;
}

int main()
{
    int n;
    cin >> n;
    int a[1000000];
    for (int i = 0; i < n; i++)
    {
        cin >> a[i];
    }
    cout << calc_water(a, n);

    return 0;
}