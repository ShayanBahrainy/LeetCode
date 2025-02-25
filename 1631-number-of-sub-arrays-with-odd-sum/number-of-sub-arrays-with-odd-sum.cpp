class Solution {
public:
    int numOfSubarrays(vector<int>& arr) {
        int possible = 0;
        const int MOD = 1e9 + 7;
        int prefixSum = 0;
        int evens = 1;
        int odds = 0;

        for (int i = 0; i < arr.size(); ++i) {
            prefixSum += arr[i];
            if (prefixSum % 2 == 0) {
                possible += odds;
                evens++;
            }
            else {
                possible += evens;
                odds++;
            }
            possible %= MOD;
        }
        return possible;
    }
};