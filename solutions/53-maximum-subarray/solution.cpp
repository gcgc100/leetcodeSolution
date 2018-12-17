#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int maxSubArray(vector<int>& nums) {
        int maxSum = 0;
        int curSum = nums[0];
        int i, j;
        for (i = 0; i < nums.size(); ++i) {
            curSum = nums[i];
            maxSum = max(curSum, maxSum);
            for (j = i+1; j < nums.size(); ++j) {
                curSum += nums[j];
                maxSum = max(curSum, maxSum);
            }
        }
        return maxSum;
    }
};

int main(int argc, char *argv[])
{
    vector<int> v = {-2, 1, -3, 4, -1, 2, 1, -5, 4};
    int ms = Solution().maxSubArray(v);
    cout << ms << endl;
    return 0;
}
