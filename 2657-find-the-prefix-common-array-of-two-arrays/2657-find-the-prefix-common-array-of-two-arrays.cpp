class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n=A.size();
        unordered_set<int>seenInA,seenInB;
        vector<int>ans;
        int cnt=0;
        for(int i=0;i<n;i++){
            seenInA.insert(A[i]);
            seenInB.insert(B[i]);
            if(seenInA.find(B[i])!=seenInA.end()){
                cnt++;
                seenInA.erase(B[i]);
                seenInB.erase(B[i]);
            }
            if(seenInB.find(A[i])!=seenInB.end()){
                cnt++;
                seenInA.erase(A[i]);
                seenInB.erase(A[i]);
            }
            ans.push_back(cnt);
        }
        return ans;
    }
};