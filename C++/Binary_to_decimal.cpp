#include <iostream>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        string bin;
        cin >> bin;
        int result = 0;
        int multiplier = 1;
        for (int i = bin.size() - 1; i >= 0; --i)
        {
            int b_digit = bin[i] - '0';
            result = result + (b_digit * multiplier);
            multiplier = multiplier * 2;
        }

        cout << result << endl;
    }
}
