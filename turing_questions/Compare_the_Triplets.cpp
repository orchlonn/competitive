#include <iostream>

using namespace std;

int main()
{
    int arrB[3], arrA[3], a = 0, b = 0;
    for (int i = 0; i < 3; i++)
    {
        cin >> arrA[i];
    }

    for (int i = 0; i < 3; i++)
    {
        cin >> arrB[i];
    }

    for (int i = 0; i < 3; i++)
    {
        if (arrA[i] > arrB[i])
        {
            a += 1;
        }
        else if (arrA[i] != arrB[i])
        {
            b += 1;
        }
    }
    cout << a << " " << b << endl;
}
