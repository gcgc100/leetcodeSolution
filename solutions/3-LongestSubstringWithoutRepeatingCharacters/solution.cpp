#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int lengthOfLongestSubstring(string s) {
        string longestSubStr = "";
        string subStr = "";
        int i = 0;
        while(i < s.length()) {
            if(this->inStr(s[i], subStr)) {
                subStr.erase(0,1);
            } else {
                subStr.push_back(s[i]);
                i++;
                if(subStr.length() > longestSubStr.length()) {
                    longestSubStr = subStr;
                }
            }
        }
        for (i = 0; i < s.length(); ++i) {
            if(this->inStr(s[i], subStr)) {
                subStr.erase(0,1);
            }
        }
        return longestSubStr.length();
    }

private:
    bool inStr(char c, string s) {
        for (auto i = s.cbegin(); i < s.cend(); ++i) {
            if(*i == c)
                return true;
        }
        return false;
    }
};

int main(int argc, char *argv[])
{
    int l = Solution().lengthOfLongestSubstring("pwwkew");   
    cout << l << endl;
    return 0;
}
