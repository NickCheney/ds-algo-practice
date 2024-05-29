from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        to_check = [(sr,sc)]
        valid_row = lambda x: len(image) > x >= 0
        valid_col = lambda y: len(image[0]) > y >= 0
        filled = [[0len(image[0])]*len(image)
        start_color = image[sr][sc]

        while len(to_check) > 0:
            sr, sc = to_check.pop()
            image[sr][sc] = color
            filled[sr][sc] = 1

            for ro, co in [(-1,0),(1,0),(0,-1),(0,1)]:
                rcon = sr + ro
                ccon = sc + co
                print(rcon, valid_row(rcon), ccon, valid_col(ccon), filled[rcon][ccon]==0, image[rcon][ccon]==start_color)
                if valid_row(rcon) and valid_col(ccon) and filled[rcon][ccon] == 0 and image[rcon][ccon]==start_color:
                    to_check.append((rcon, ccon))

        return image

    
if __name__ == '__main__':
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(sol.floodFill(image, sr, sc, color))
