#include <string>
class Solution {
public:
    string findDifferentBinaryString(vector<string>& nums) {
        ostringstream different;
        for (int i = 0; i < nums.size(); ++i) {
            different << (nums[i][i] == '1' ?  "0": "1");
        }
        return different.str();
    }
};