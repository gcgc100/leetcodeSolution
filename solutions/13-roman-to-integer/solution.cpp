#include <iostream>
//#include <string>
#include <map>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    int romanToInt(string s) {
        map<char, int> m;
        m['I'] = 1;
        m['V'] = 5;
        m['X'] = 10;
        m['L'] = 50;
        m['C'] = 100;
        m['D'] = 500;
        m['M'] = 1000;
        int pre = m[s[0]];
        int preInt = pre;
        int romanInt = 0;
        int i = 1;
        while(i < s.length()) {
            //cout << pre << "," << preInt << endl;
            if(m[s[i]] < pre) {
                romanInt += preInt;
                pre = m[s[i]];
                preInt = pre;
            } else if(m[s[i]] == pre){
                pre = m[s[i]];
                preInt += pre;
            } else {
                romanInt += (m[s[i]] - preInt);
                i++;
                if(i==s.length()) {
                    pre = 0;
                    preInt = 0;
                    break;
                }
                pre = m[s[i]];
                preInt = pre;
            }
            i++;
        }
        romanInt += preInt;
        return romanInt;
        //cout << s.substr(1) << endl;
        return 0;
    }
};


int main(int argc, char *argv[])
{
    int ret = 0;
    ret = Solution().romanToInt("III");
    cout << ret << endl;
    ret = Solution().romanToInt("IV");
    cout << ret << endl;
    ret = Solution().romanToInt("IX");
    cout << ret << endl;
    ret = Solution().romanToInt("LVIII");
    cout << ret << endl;
    ret = Solution().romanToInt("MCMXCIV");
    cout << ret << endl;
    ret = Solution().romanToInt("MCDLXXVI");
    cout << ret << endl;
    ret = Solution().romanToInt("MMMCDIII");
    cout << ret << endl;
    ret = Solution().romanToInt("MMCCCVII");
    cout << ret << endl;
    return 0;
}
