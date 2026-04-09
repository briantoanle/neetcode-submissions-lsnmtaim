class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        # scan for the first square

        rows = len(grid)
        cols = len(grid[0])
        result = 0 
        firstIsland = [0,0]
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    firstIsland = [i,j]
                    break
        #print('the first island is at',firstIsland)
        #print('((()))')
        q = deque()
        q.append(firstIsland)
        visited = set()
        visited.add((firstIsland[0],firstIsland[1]))
        #print(q)
        directions = [[0,1],[0,-1],[-1,0],[1,0]]
        
        while q:
            coordX, coordY = q.popleft()
            result += 4
            #print("I'm currently traveling to",coordX,coordY)
            for i,j in directions:
                tempX = coordX + i
                tempY = coordY + j
                if 0 <= tempX < rows and 0 <= tempY < cols and grid[tempX][tempY] == 1:
                    result -= 1
                    if (tempX,tempY) not in visited:
                        q.append([tempX,tempY])
                        visited.add((tempX,tempY))
                    

        #print(result)
        return result 

        
        
        