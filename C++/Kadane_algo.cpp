#include <iostream>
using namespace std;

int main()
{
    int test_cases;
    cin >> test_cases;
    for (int i = 0; i < test_cases; i++)
    {

        int n;
        cin >> n;
        int a[1000];

        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
        }
        int cs = 0;
        int ms = 0;
        for (int i = 0; i < n; i++)
        {
            cs = cs + a[i];
            if (cs < 0)
            {
                cs = 0;
            }

            ms = max(cs, ms);
        }

        cout << ms;
    }

    return 0;
}