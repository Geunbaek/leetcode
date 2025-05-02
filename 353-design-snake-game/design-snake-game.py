class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height

        self.foods = food
        self.food_index = 0

        self.dxy = {
            "R": (1, 0),
            "L": (-1, 0),
            "U": (0, -1),
            "D": (0, 1),
        }
        
        self.positions = deque([(0, 0)])
        self.score = 0

    def move(self, direction: str) -> int:
        dx, dy = self.dxy[direction]

        head_x, head_y = self.positions[0]

        nx = head_x + dx
        ny = head_y + dy

        if not (0 <= nx < self.width and 0 <= ny < self.height):
            return -1
        print((nx, ny), list(self.positions)[:-1])
        if (nx, ny) in list(self.positions)[:-1]:
            return -1

        if self.food_index >= len(self.foods):
            self.positions.pop()
        else:
            y, x = self.foods[self.food_index]
            if not (nx == x and ny == y):
                self.positions.pop()
            else:
                self.score += 1
                self.food_index += 1

        self.positions.appendleft((nx, ny))
        return self.score

        

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)