#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int removeElement(vector<int>& nums, int val) {
        vector<int>::iterator it = nums.begin();
        int curIndex = 0;
        while(it != nums.end()) {
            if(*it != val) {
                nums[curIndex++] = *it;
            }
            it++;
        }
        int i = nums.size()-curIndex;
        while(i > 0) {
            nums.pop_back();
            i--;
        }
        return curIndex;
    }
};

int main(int argc, char *argv[])
{
    vector<int> v = {0,1,2,2,3,0,4,2};
    int val = 2;
    int len = Solution().removeElement(v, val);
    cout << len << endl;
    int i = 0;
    for (i = 0; i < v.size(); i++) {
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}
