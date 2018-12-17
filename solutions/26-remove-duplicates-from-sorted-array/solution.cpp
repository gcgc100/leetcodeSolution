#include<iostream>
#include<vector>

using namespace std;


class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int removeDuplicates(vector<int>& nums) {
        vector<int>::iterator it = nums.begin();
        it++;
        int curIndex = 0;
        while(it != nums.end()) {
            if(*it != nums[curIndex]) {
                nums[++curIndex] = *it;
            }
            it++;
        }
        int i = nums.size()-curIndex-1;
        while(i > 0) {
            nums.pop_back();
            i--;
        }
        return curIndex+1;
    }
};


int main(int argc, char *argv[])
{
    vector<int> v = {0,0,1,1,1,2,2,3,3,4};
    int len = Solution().removeDuplicates(v);
    cout << len << endl;
    int i;
    for (i = 0; i < v.size(); ++i) {
        cout << v[i] << " ";
    }
    cout << endl;
    return 0;
}
