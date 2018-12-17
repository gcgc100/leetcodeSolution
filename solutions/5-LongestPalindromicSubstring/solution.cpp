#include<iostream>
#include<vector>

using namespace std;

class Solution
{
public:
    Solution (){};
    virtual ~Solution (){};

    string longestPalindrome(string s) {
        int len = 2*s.size() + 3;
        char* str = new char[len+1];
        char head = '$', mid = '#';
        int* p = new int[len+1];
        int id = 0;
        int ans = 0;
        int mx = 1;
        int pre_len = 0;
        str[0] = str[len-1] = head;
        str[len-1] = '@';
        for(int i = 1; i < len-1; i++) {
            if(i%2) str[i] = mid;
            else str[i] = s[i/2-1];
        }
        p[0] = 1;
        cout << str << endl;
        for (int i = 0; i < len-1; ++i) {
            if(i <= mx) p[i] = min<int>(mx-i, p[2*id-i]);
            else p[i] = 1;
            while(str[i-p[i]] == str[i+p[i]]) {
                p[i]++;
            }
            if(p[i] >= p[id]) {
                id = i;
                mx = id+p[id];
                if(pre_len <= mx-id) {
                    ans = id;
                    pre_len = mx-id;
                }
            }
        }
        if((mx-id-1)%2) return s.substr(ans/2-1-(mx-id-1)/2, mx-id-1);
        else return s.substr(ans/2 - (mx-id-1)/2, mx-id-1);
    }
};


int main(int argc, char *argv[])
{
    string s = Solution().longestPalindrome("babad");
    cout << s << endl;
    return 0;
}
