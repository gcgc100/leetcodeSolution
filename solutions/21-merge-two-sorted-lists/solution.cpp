#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    vector<int> iv = {1,2,3,4,5};
    //vector<int>::iterator it;
    //for (it = iv.begin(); it != iv.end() ; ++it) {
    //    *it += 10;
    //}
    for (auto it = iv.cbegin(); it != iv.cend() ; ++it) {
        cout << *it << endl;
    }
    return 0;
}
