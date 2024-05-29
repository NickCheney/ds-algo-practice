from typing import List

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        mat[0][0] = self.bfs(mat, 0, 0)

        for i in range(1,len(mat)):
            mat[i][0] = min(mat[i-1][0]+1,self.bfs(mat,i,0))
        
        for j in range(1,len(mat[0])):
            mat[0][j] = min(mat[0][j-1]+1, self.bfs(mat,0,j))
        
        for i in range(1,len(mat)):
            for j in range(1,len(mat[0])):
                mat[i][j] = min(mat[i-1][j]+1,mat[i][j-1]+1, self.bfs(mat, i, j))

        return mat

    def bfs(self, mat, i, j):
        minDist = float('inf')     
        for row in range(i, len(mat)):
            for col in range(j,len(mat[0])):
                if mat[row][col]==0:
                    minDist = min(minDist, row - i + col - j)
        
        return minDist


if __name__ == '__main__':
    mat = [[0,1,1,0,0],[0,1,1,0,0],[0,1,0,0,1],[1,1,1,1,0],[1,0,0,1,0]]
    sol = Solution()
    print(sol.updateMatrix(mat))
    
