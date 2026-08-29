class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        int n=nums.size();
        vector<pair<int,int>>elements;
        for(int i=0;i<n;i++){
            elements.emplace_back(nums[i],i);
        }
        sort(elements.begin(),elements.end());
        auto sortIt=[&nums,&elements](int left,int right){
            vector<int>indecies;
            for(int i=left;i<right;i++){
                indecies.push_back(elements[i].second);
            }
            sort(indecies.begin(),indecies.end());
            for(int i=0;i<indecies.size();i++){
                nums[indecies[i]]=elements[left+i].first;
            }
        };
        int left=0,right=1;
        while(right<n){
            while(right<n && elements[right].first-elements[right-1].first<=limit) right++;
            sortIt(left,right);
            left=right;
            right++;
        }
        return nums;
    }
};