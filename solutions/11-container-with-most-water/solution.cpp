#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int maxArea(vector<int>& height) {
        int mostWater = 0;
        int begin = 0;
        int end = height.size()-1;
        int i = 0;
        int j = height.size()-1;
        while(i < j) {
            if(height[begin] > height[end]) {
                if(height[j] > height[end]) {
                    if(min(height[begin], height[j])*(j-begin) > mostWater) {
                        end = j;
                        mostWater = min(height[begin], height[j])*(j-begin);
                    }
                }
                j--;
            } else {
                if(height[i] > height[begin]) {
                    if(min(height[i], height[end])*(end-i) > mostWater) {
                        begin = i;
                        mostWater = min(height[i], height[end])*(end-i);
                    }
                }
                i++;
            }
        }
        return mostWater;
    }

};

int main(int argc, char *argv[])
{
    int arr[9] = {1,8,6,2,5,4,8,3,7};
    vector<int> aa(arr, arr+9);
    int mw = Solution().maxArea(aa);
    cout << mw << endl;
    return 0;
}
