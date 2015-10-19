# I used union and find way to solve this problem.Maybe not as fast as BFS way, you could see the BFS file alternatively.
# This used quick-union method with one-pass path compression, to reduce each brach by half in the process of finding its root.
class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return  # empty board

        if not (len(board) and len(board[0])):
            return 
        
        self.M = len(board)
        self.N = len(board[0])
        self.id = {(-1,-1):(-1,-1)} #(i,j)=>parent
        
        for i in range(0,self.M):
            for j in range(0,self.N):
                if board[i][j]=='O':
                    self.union(board,i,j)

        for i in range(0,self.M):
            for j in range(0,self.N):
                if board[i][j] == 'O' and self.root((i,j))!=(-1,-1):
                    board[i][j]='X'
        
        return             
                    
                    
    def root(self,p):
        while(p!=self.id[p]):
            self.id[p] = self.id[self.id[p]] #path compression
            p = self.id[p]
        return p 
        
    def union(self,board,i,j): #called when this is 0
        self.id[(i,j)] = (i,j)
        neighbors = [(m,n) for (m,n) in [(i,j-1),(i-1,j)] if m>=0 and m<=self.M-1 and n>=0 and n<=self.N-1]
        for (m,n) in neighbors:
            if board[m][n]=='O':
                root1 = self.root((i,j))
                root2 = self.root((m,n))
                self.id[root1] = root2
        if  i==0 or j==0 or i==self.M-1 or j ==self.N-1:
            self.id[self.root((i,j))] = (-1,-1)
    
       
        
