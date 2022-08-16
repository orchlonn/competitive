#include <iostream>
using namespace std;

string nums[30] = {
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "quarter",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
    "twenty",
    "twenty one",
    "twenty two",
    "twenty three",
    "twenty four",
    "twenty five",
    "twenty six",
    "twenty seven",
    "twenty eight",
    "twenty nine",
    "half",
};

int main()
{
    int h, m, newMin;
    cin >> h >> m;
    if (m == 0)
    {
        cout << nums[h - 1] << " o' clock" << endl;
    }
    else if (m == 1)
    {
        cout << "one minute past " << nums[h - 1] << endl;
    }

    else if (m == 15)
    {
        cout << "quarter past " << nums[h - 1] << endl;
    }
    else if (m == 30)
    {
        cout << "half past " << nums[h - 1] << endl;
    }
    else if (m < 30)
    {
        cout << nums[m - 1] << " minutes past " << nums[h - 1] << endl;
    }
    else if (m == 45)
    {
        cout << "quarter to " << nums[h] << endl;
    }
    else
    {
        newMin = 60 - m;
        cout << nums[newMin - 1] << " minutes to " << nums[h] << endl;
    }
}