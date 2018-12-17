#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int strStr(string haystack, string needle) {
        int i = 0;
        int j = 0;
        for (i = 0; i < haystack.length()-needle.length()+1; ++i) {
            while(j<needle.length()) {
                if(haystack[i+j] != needle[j])
                    break;
                else
                    j++;
            }
            if(j==needle.length())
                break;
        }
        return i==(haystack.length()-needle.length()+1) ? -1 : i;
    }
};

int main(int argc, char *argv[])
{
    int i = Solution().strStr("heello", "dll");
    cout << i << endl;
    return 0;
}
