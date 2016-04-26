
/*
 *
 * Given a 2D board and a word, find if the word exists in the grid.
 *
 * The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
 *
 * For example,
 * Given board =
 *
 * [
 *   ['A','B','C','E'],
 *     ['S','F','C','S'],
 *       ['A','D','E','E']
 *       ]
 *       word = "ABCCED", -> returns true,
 *       word = "SEE", -> returns true,
 *       word = "ABCB", -> returns false.
 *
 */
class Solution {
private:
        vector<vector<bool> > visited;
        int m;
        int n;

public:
    bool withinBound(int x,int y){
        return x>=0 && x<m && y>=0 && y<n;
    }
    void resetVisited(){
        for(int i=0;i<m;++i){
            fill(visited[i].begin(),visited[i].end(),false);
        }
            //    printf("lalla");
    }

    bool dfs(vector<vector<char>>& board, string word,int x,int y,int word_idx){
        if(word_idx==word.size()) return true;
        char c = word[word_idx];
        //printf("lalla");
        if(!withinBound(x,y) || visited[x][y] || board[x][y]!=c) return false;

        bool found = false;
        visited[x][y] = true;
        found = (dfs(board,word,x+1,y,word_idx+1)) || (dfs(board,word,x,y+1,word_idx+1)) || (dfs(board,word,x-1,y,word_idx+1)) || (dfs(board,word,x,y-1,word_idx+1));
        visited[x][y] = false;
        return found;
    }
    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        if(m==0) return false;
        n = board[0].size();
        if(n==0) return false;
        if(word.size()==0) return true;
        if(m*n<word.size()) return false;
        visited = vector<vector<bool>>(m,vector<bool>(n,false));
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(board[i][j]==word[0]){
                 if(dfs(board,word,i,j,0)) return true;

                  //  resetVisited();
                }


            }
        }

        return false;
    }

};


/*
 * Some methods for optimization
 * 1. Preprocessing. HashMap to check the total number of the characters.
 * 2. Simplify the withinBound check. due to each new grip is just one step from the original grid. So that only one direction bound is needed to be checked!
