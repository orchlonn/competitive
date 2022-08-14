#include <iostream>

using namespace std;

int main()
{
    int n;
    cin >> n;
    long long arr[n], ans = 0;

    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        ans += arr[i];
    }

    cout << ans << endl;
}
