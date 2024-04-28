// my solution:
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        for (int i=0;i<n-1;i++){
            for (int j=i+1;j<n;j++){
                if (nums[i]==nums[j])
                return true;
            }
        }
        return false;
    }
    
};
// Uses two pointers to iterate through array but it's really slow. 
// To make the runtime O(N) we can use hashsets
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> seen;
        for (int num : nums) {
            if (seen.count(num) > 0)
                return true;
            seen.insert(num);
        }
        return false;
    }
};