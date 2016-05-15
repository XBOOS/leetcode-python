/*
 * Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
 *
 * Example 1:
 *
 * 11110
 * 11010
 * 11000
 * 00000
 * Answer: 1
 *
 * Example 2:
 *
 * 11000
 * 11000
 * 00100
 * 00011
 * Answer: 3
 *
 */
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        if(m==0) return 0;
        int n = grid[0].size();
        if(n==0) return 0;
        int count=0;
        vector<vector<bool>> visited(m,vector<bool>(n,false));
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(!visited[i][j]&&grid[i][j]=='1'){
                    ++count;
                    dfs(grid,visited,m,n,i,j);
                }
            }
        }
        return count;
    }
    void dfs(vector<vector<char>>& grid, vector<vector<bool>>& visited,int m,int n,int i,int j){
        if(i<0||i>=m||j<0||j>=n||visited[i][j]) return;
        visited[i][j]=true;
        if(grid[i][j]=='1'){
            dfs(grid,visited,m,n,i-1,j);
            dfs(grid,visited,m,n,i+1,j);
            dfs(grid,visited,m,n,i,j-1);
            dfs(grid,visited,m,n,i,j+1);
    }
    }
};
