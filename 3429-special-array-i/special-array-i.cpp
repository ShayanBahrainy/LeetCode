class Solution {
public:
    bool isArraySpecial(vector<int>& nums) {
        for (int i = 1; i < nums.size(); i++) {
            if (nums.at(i) % 2 == nums.at(i - 1) % 2) {
                return false;
            }
        }
        return true;
    }
};