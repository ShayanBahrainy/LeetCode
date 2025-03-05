class Solution {
public:
    long long coloredCells(int n) {
        long long result = 1;
        int i;
        for (i = 1; i <= n; ++i) {
            result += 4 * (i - 1);
        }
        return result;
    }
};