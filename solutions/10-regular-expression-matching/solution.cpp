#include <iostream>
#include <algorithm>
#include <string>
using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};
    bool isMatch(string s, string p) {
        int i, j;
        char pre;
        for (i = 0; i < min(s.length(), p.length()); ++i) {
            char pat = p[i];
            if(p[i] == '*') {
                j = i;
                while((s[j] == pre || pre == '.') && j<s.length()) {
                    if(this->isMatch(s.substr(j+1), p.substr(i+1))) {
                        return true;
                    }
                    j++;
                }
                return false;
            } else if(p[i] == '.') {
                pre = p[i];
            } else if (p[i] == s[i]) {
                pre = p[i];
            } else {
                return false;
            }
        }
        if(s.length() == p.length())
            return true;
        return false;
    }
};

int main(int argc, char *argv[])
{
    string str = "adddaaa";
    string pattern = "a.*aaa";
    cout << "Compare " << str << "," << pattern << endl;
    bool ret = Solution().isMatch(str, pattern);
    //bool ret = Solution().isMatch("ad", "aa");
    cout << ret << endl;
    return 0;
}
