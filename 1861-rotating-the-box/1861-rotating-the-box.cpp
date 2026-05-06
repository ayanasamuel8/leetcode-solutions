class Solution {
public:
    vector<vector<char>> rotateTheBox(vector<vector<char>>& box) {
        ios::sync_with_stdio(0);
        int row=box.size();
        int col=box[0].size();
        vector<vector<char>>ans(col,vector<char>(row,'.'));
        for(int i=0;i<row;i++){
            int right=col-1;
            for(int left=col-1;left>=0;left--){
                if(box[i][left]=='.') continue;
                else if(box[i][left]=='#'){
                    ans[right][row-1-i]='#';
                    --right;
                }else if(box[i][left]=='*'){
                    ans[left][row-1-i]='*';
                    right=left-1;
                }
               
            }
        }
        return ans;
    }
};