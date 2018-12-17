#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    string longestCommonPrefix(vector<string>& strs) {
        int i;
        int j = 0;
        string s = "";
        char cur;
        while(j != -1) {
            if(j==strs[0].length())
                break;
            cur = strs[0][j];
            for (i = 1; i < strs.size(); ++i) {
                if(j==strs[i].length() || strs[i][j] != cur) {
                    j = -1;
                    break;
                }
            }
            if(j != -1) {
                s.push_back(cur);
                j++;
            }
        }
        return s;
    }
};


int main(int argc, char *argv[])
{
    vector<string> v;
    v.push_back("flower");
    v.push_back("flow");
    v.push_back("flight");
    string s = Solution().longestCommonPrefix(v);
    cout << s << endl;
    return 0;
}
