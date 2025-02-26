#include <limits>

class Solution {
public:
    int maxAbsoluteSum(vector<int>& nums) {
        int max = -std::numeric_limits<int>::infinity();
        int min = std::numeric_limits<int>::infinity();
        int curr = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] + curr > max) {
                max = nums[i] + curr;
            }
            curr += nums[i];
            if (curr < 0) {
                curr = 0;
            }
        }
        curr = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] + curr < min) {
                min = nums[i] + curr;
            }
            curr += nums[i];
            if (curr > 0) {
                curr = 0;
            }
        }
        cout << min << endl << max << endl;
        return fabs(min) > max ? fabs(min) : max;
    }
};