/*
 * Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
 *
 * click to show follow up.
 *
 * Follow up:
 * Did you use extra space?
 * A straight forward solution using O(mn) space is probably a bad idea.
 * A simple improvement uses O(m + n) space, but still not the best solution.
 * Could you devise a constant space solution?
 *
 */

/* Method1 Using O(mn) extra space
 * taken as a practice for vector and matrix
 * std::fill
 * To copy a vector:
 * if not allocated space---> using copy constructor
 * else---> using assignment operator or std::copy
 */



class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {

        vector<vector<int> > copy(matrix);
        //copy the original matrix to the backup one
        int m = matrix.size();
        if(!m) return;
        int n = matrix[0].size();
        if(!n) return;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(!copy[i][j]){
                    std::fill(matrix[i].begin(),matrix[i].end(),0);
                    for(int k=0;k<m;++k) matrix[k][j]=0;
                }
            }
        }
    }

};

/* Method2 using O(m+n) extra space
 * firstly select out the rows and columns which should be set to zeros then set them
 */
class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if(!m) return;
        int n = matrix[0].size();
        if(!n) return;
        //to record which rows should be set zeroes
        set<int> rows;
        set<int> cols;
        for(int i=0;i<m;++i){
            for(int j=0;j<n;++j){
                if(!matrix[i][j]){
                    rows.insert(i);
                    cols.insert(j);
                }
            }
        }
        //to set the corresponding rows and cols
        for(int row:rows) std::fill(matrix[row].begin(),matrix[row].end(),0);
        for(int col:cols){
            for(int k=0;k<m;++k) matrix[k][col]=0;
        }
    }

};
