class Robot:

    def __init__(self, width: int, height: int):
        self.grid = [height, width]
        self.dirs = deque(['East', 'North', 'West', 'South'])
        self.pos = [0,0]
        self.drxn = {'East': (0, 1), 'North': (1, 0),'West': (0, -1), 'South': (-1, 0)}
    def inbound(self, x, y):
        return 0 <= x < self.grid[0] and 0<= y < self.grid[1]

    def step(self, num: int) -> None:
        total = 2 * self.grid[1] + 2 * self.grid[0] - 4
        mod = num % total
        num = mod
        if mod == 0 and self.pos == [0,0]:
            while self.dirs[0] != 'South':
                self.dirs.append(self.dirs.popleft())


        for i in range(num):
            dx, dy = self.drxn[self.dirs[0]]
            if not self.inbound(self.pos[0] + dx, self.pos[1] + dy):
                self.dirs.append(self.dirs.popleft())
            
            dx, dy = self.drxn[self.dirs[0]]
            
            self.pos[0] += dx
            self.pos[1] += dy
        

    def getPos(self) -> List[int]:
        return self.pos[::-1]
        

    def getDir(self) -> str:
        return self.dirs[0]


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()