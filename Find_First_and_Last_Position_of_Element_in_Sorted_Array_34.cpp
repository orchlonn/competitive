class Solution
{
public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        int pos1 = -1, pos2 = -1;
        for (int i = 0; i < nums.size(); i++)
        {
            if (target == nums[i])
            {
                pos1 = i;
            }
        }
    }
};