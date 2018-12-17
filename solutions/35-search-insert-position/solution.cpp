#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int searchInsert(vector<int>& nums, int target) {
        int start = 0;
        int end = nums.size()-1;
        int mid, pos;
        while(!(end < start)) {
            mid = (start+end)/2;
            if(nums[mid] == target)
                return mid;
            else if(nums[mid] < target) {
                start = mid+1;
            } else {
                end = mid-1;
            }
        }
        return start;
    }
};


int main(int argc, char *argv[])
{
    vector<int> nums = {1,3,5,6};
    int i = Solution().searchInsert(nums, 0);
    cout << i << endl;
    return 0;
}
