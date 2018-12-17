#include <vector>
#include <iostream>
using namespace std;

class Solution {
    public:
        vector<int> twoSum(vector<int>& nums, int target) {
            vector<int> retVec;
            int i, j;
            for (i = 0; i < nums.size(); ++i) {
                for (j = 0; j < i; ++j) {
                    if(nums[i]+nums[j]==target) {
                        retVec.push_back(nums[i]);
                        retVec.push_back(nums[j]);
                        break;
                    }
                }
            }
            return retVec;
        }
};

int main(int argc, char *argv[])
{
    int arr[4] = {2,7,11,15};
    int i;
    vector<int> aa(arr, arr+4);
    aa = Solution().twoSum(aa, 9);
    for (i = 0; i < aa.size(); ++i) {
        cout << aa[i] << endl;
    }
    cout << endl;
    return 0;
}
