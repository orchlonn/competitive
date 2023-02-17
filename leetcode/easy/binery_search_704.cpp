class Solution
{
public:
    int search(vector<int> &nums, int target)
    {

        int sum = -1;
        bool isTrue = false;
        for (int i = 0; i < nums.size(); i++)
        {
            sum++;
            if (target == nums[i])
            {
                isTrue = true;
                break;
            }
        }
        if (isTrue)
        {
            return sum;
        }
        else
        {
            return -1;
        }
    }
};