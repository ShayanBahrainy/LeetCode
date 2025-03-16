class Solution {
public:
    long long repairCars(vector<int>& ranks, int cars) {
        long long left = 0;
        long long right = ranks.at(0);
        for (int i = 0 ; i < ranks.size(); ++i) {
            if (ranks.at(i) > right) {
                right = ranks.at(i);
            }
        }
        right = right * cars * cars;
         while (left <= right) {
            long long mid = (left + right) / 2;
            if (canRepair(ranks, cars, mid)) {
                right = mid - 1;
            }
            else {
                left = mid + 1;
            }
        }
        return left;
       }
  bool canRepair(vector<int>&ranks, int cars, long long time) {
        long long carsFixed = 0;
        for (int i = 0; i < ranks.size(); ++i) { 
            carsFixed += (sqrt(((long long) time / ranks.at(i))));
        }
        if (carsFixed >= cars) {
            return true;
        }
        return false;
    }
};