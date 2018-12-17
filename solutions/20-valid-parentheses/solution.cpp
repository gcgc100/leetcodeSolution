#include <iostream>
#include <vector>
#include <map>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};
    
    bool isValid(string s) {
        int i = 0;
        vector<char> v;
        vector<char> beginP = {'[', '{', '('};
        vector<char>::iterator it;
        while(i < s.length()) {
            it = find(beginP.begin(), beginP.end(), s[i]);
            if(it != beginP.end())
                v.push_back(s[i]);
            else
                if(this->isParentheseMatch(v.back(),s[i]))
                    v.pop_back();
                else
                    return false;
            i++;
        }
        if(v.size()==0)
            return true;
        else
            return false;
    }

    bool isParentheseMatch(char s1, char s2) {
        map<char, char> m = { {'[', ']'}, {'{', '}'}, {'(', ')'}};
        return m[s1] == s2;
    }
};

int main(int argc, char *argv[])
{
    cout << Solution().isValid("{()}") << endl;
    return 0;
}
