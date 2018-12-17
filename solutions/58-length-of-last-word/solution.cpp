#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int lengthOfLastWord(string s) {
        int i;
        int lwordLength = -1;
        for (i = s.length(); i > -1; --i) {
            if(s[i] != ' ') {
                lwordLength++;
            } else {
                break;
            }
        }
        return lwordLength;
    }
};


int main(int argc, char *argv[])
{
    int l = Solution().lengthOfLastWord("Hello World");
    cout << l << endl;
    return 0;
}
