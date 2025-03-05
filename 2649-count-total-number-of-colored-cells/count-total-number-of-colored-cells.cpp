class Solution {
public:
    long long coloredCells(unsigned int n) {
        unsigned long long result = 1;
        unsigned int i;
        for (i = 1; i <= n; ++i) {
            result += 4 * (i - 1);
        }
        return result;
    }
};