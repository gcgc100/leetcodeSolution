#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    string countAndSay(int n) {
        string s = "";
        while(n > 0) {
            s = this->say(s);
            n--;
        }
        return s;
    }

    string say(string s) {
        int i;
        char curChar = s[0];
        int count = 1;
        string retStr = "";
        if(s=="") {
            return "1";
        }
        for (i = 1; i < s.length(); ++i) {
            if(s[i] == curChar) {
                count++;
            } else {
                retStr.append(to_string(count));
                retStr.push_back(curChar);
                curChar = s[i];
                count = 1;
            }
        }
        retStr.append(to_string(count));
        retStr.push_back(curChar);
        return retStr;
    }
};


int main(int argc, char *argv[])
{
    int i = 10;
    string s = Solution().countAndSay(3);
    //string s = Solution().say("");
    cout << s << endl;
    return 0;
}
