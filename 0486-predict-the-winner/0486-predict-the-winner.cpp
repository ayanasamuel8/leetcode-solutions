struct TupleHash {
    template <class T1, class T2>
    size_t operator()(const tuple<T1, T2>& t) const {
        // Get hashes of individual elements
        auto h1 = hash<T1>{}(get<0>(t));
        auto h2 = hash<T2>{}(get<1>(t));
        
        // Combine them using a standard bit-shifting formula
        return h1 ^ (h2 << 1); 
    }
};
class Solution {
public:
    // left, right, firsttakes
    unordered_map<tuple<int,int>,int, TupleHash> dp;
    int pick(vector<int> &nums, int left,int right){
        if (left == right){
            return nums[left];
        }
        tuple<int, int>  tup= make_tuple(left, right);
        if (dp.find(tup) != dp.end()){
            return dp[tup];
        }
        //pick left
        int take_left = nums[left] - pick(nums, left + 1, right);
        //pick right
        int take_right = nums[right] - pick(nums, left, right - 1);
        return dp[tup] = max(take_left, take_right);
    }
    bool predictTheWinner(vector<int>& nums) {
        int ans = pick(nums, 0, nums.size() - 1);
        return ans >= 0;
    }
};