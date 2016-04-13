/*
 * Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
 *
 * For example,
 * Given the following matrix:
 *
 * [
 *  [ 1, 2, 3 ],
 *   [ 4, 5, 6 ],
 *    [ 7, 8, 9 ]
 *    ]
 *    You should return [1,2,3,6,9,8,7,4,5].
 *
 */

/* Method1
 * by walking and wall_detection and turn directions---like a game design
 */

class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        //always get aground and turn right
        vector<pair<int,int> > directions = {make_pair(0,1),make_pair(1,0),make_pair(0,-1),make_pair(-1,0)};
        int dir_idx = 0;//always %4

        vector<int> res;
        int m = matrix.size();
        if(!m) return res;
        int n = matrix[0].size();
        if(!n) return res;

        vector<int> bounds = {1,m-1,0,n-1};
        int row = 0, col = 0, touched = 0,total = m*n;
        while(touched<total){
            res.push_back(matrix[row][col]);
            touched++;
            if(wall_detection(row,col,bounds,dir_idx)){
                dir_idx= (dir_idx+1)%4;
            }
                row = row+directions[dir_idx].first;
                col = col+directions[dir_idx].second;


        }
        return res;

    }
    bool wall_detection(const int row,const int col,vector<int>& bounds,int dir_idx){
        if(dir_idx%4==0 && col==bounds[3]){
            bounds[3]--;
            return true;
        }
        if(dir_idx%4==1 && row==bounds[1]){
            bounds[1]--;
            return true;
        }
        if(dir_idx%4==2 && col==bounds[2]){
            bounds[2]++;
            return true;
        }
        if(dir_idx%4==3 && row==bounds[0]){
            bounds[0]++;
            return true;
        }

        return false;
    }

};
