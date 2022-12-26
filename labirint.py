import pygame


smezh1 = {1: [2],
         2: [1, 5, 3],
         3: [2, 6],
         4: [5, 7],
         5: [2, 4, 6],
         6: [3, 5, 9],
         7: [4, 8],
         8: [7],
         9: [6]}



smezh = {1: [2],
         2: [1, 6, 3],
         3: [2, 4, 7],
         4: [3],
         5: [9],
         6: [2, 10],
         7: [3, 11],
         8: [],
         9: [5,10],
         10: [6, 9, 11],
         11: [7, 10, 12],
         12: [11]}

points = [[1, 2, 3, 4],[5,6,7,8],[9,10,11,12]]

def cletcka(color, r, c):
    pygame.draw.rect(screen, color, ((board.left + c * board.cell_size + 10, board.top + r * board.cell_size + 10), (board.cell_size - 20, board.cell_size - 20)))

def printpath(path):
    rerender()
    for p in path:
        for y in range(len(points)):
            if p in points[y]:
                r = y
                c = points[y].index(p)
        cletcka('yellow', r, c)
    cletcka('red', r,c)




def isintable(pos):
    if board.left < pos[0] < board.left + board.pixwidth and board.top < pos[1] < board.top + board.pixheight:
        return True
    else:
        return False


def dfs_paths(graph, start, goal):
    stack = [(start, [start])]  # (vertex, path)
    while stack:
        (vertex, path) = stack.pop()
        for next in set(graph[vertex]) - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


def get_cords(pos):
    tx = (pos[0] - board.left) // board.cell_size
    ty = (pos[1] - board.top) // board.cell_size
    return (tx, ty)
class Board:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
     
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.pixwidth = self.width * self.cell_size
        self.pixheight = self.height * self.cell_size
     
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
        self.pixwidth = self.width * cell_size
        self.pixheight = self.height * cell_size

    def render(self, screen):
        for stolb in range(self.width + 1):
            perem_cord = self.left + stolb * self.cell_size
            pygame.draw.line(screen, 'white', (perem_cord, self.top), (perem_cord, self.top + self.height * self.cell_size), 2)
        for stroke in range(self.height + 1):
            perem_cord = self.top + stroke * self.cell_size
            pygame.draw.line(screen, 'white', (self.left, perem_cord), (self.left + self.width * self.cell_size, perem_cord), 2)

def hor_line(r, c):
   pygame.draw.line(screen, 'green', (board.left + board.cell_size * c, board.top + board.cell_size * (r + 1)), (board.left + board.cell_size * (c + 1), board.top + board.cell_size * (r + 1)), 5)
   #pygame.draw.line(screen, 'green', (0,0), (500,500), 5)


def vert_line(r, c):
    pygame.draw.line(screen, 'green', (board.left + board.cell_size * (c), board.top + board.cell_size * (r)), (board.left + board.cell_size * (c), board.top + board.cell_size * (r + 1)), 5)


def granica():
    pygame.draw.rect(screen, 'green', ((board.left, board.top), (board.cell_size * board.width + 2, board.cell_size * board.height + 2)), 5)


def robot(r,c):
    pygame.draw.circle(screen, 'blue', (board.left + board.cell_size * c + board.cell_size // 2, board.top + board.cell_size * (r) + board.cell_size // 2), board.cell_size // 2 - 10)


def rclear(r, c):
    pygame.draw.circle(screen, 'black', (board.left + board.cell_size * c + board.cell_size // 2, board.top + board.cell_size * (r) + board.cell_size // 2), board.cell_size // 2 - 10)

pygame.init()
screen = pygame.display.set_mode((500, 500))
screen.fill('black')

board = Board(len(points[0]), len(points))
board.set_view(40, 40, 100)
board.render(screen)
running = True
granica()
rob_r = 1
rob_c = 0
robot(rob_r, rob_c)

def rerender():
    screen.fill('black')
    board.render(screen)
    granica()
    robot(rob_r, rob_c)
    stena()

def stena():
    for row in range(len(points)):
        for col in range(len(points[0])):
            try:
                if points[row + 1][col] not in smezh[points[row][col]]:
                    hor_line(row, col)
            except:
                pass

            try:
                if points[row - 1][col] not in smezh[points[row][col]]:
                    hor_line(row - 1, col)
            except:
                pass

            try:
                if points[row][col + 1] not in smezh[points[row][col]]:
                    vert_line(row, col + 1)
            except:
                pass
            try:
                if points[row][col - 1] not in smezh[points[row][col]]:
                    vert_line(row, col)
            except:
                pass
stena()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                try:
                    if points[rob_r - 1][rob_c] in smezh[points[rob_r][rob_c]]:
                        rclear(rob_r, rob_c)
                        rob_r -= 1
                        robot(rob_r, rob_c)
                except:
                    pass
            elif event.key == pygame.K_RIGHT:
                try:
                    if points[rob_r][rob_c + 1] in smezh[points[rob_r][rob_c]]:
                        rclear(rob_r, rob_c)
                        rob_c += 1
                        robot(rob_r, rob_c)
                except:
                    pass
            elif event.key == pygame.K_DOWN:
                try:
                    if points[rob_r + 1][rob_c] in smezh[points[rob_r][rob_c]]:
                        rclear(rob_r, rob_c)
                        rob_r += 1
                        robot(rob_r, rob_c)
                except:
                    pass
            elif event.key == pygame.K_LEFT:
                try:
                    if points[rob_r][rob_c - 1] in smezh[points[rob_r][rob_c]]:
                        rclear(rob_r, rob_c)
                        rob_c -= 1
                        robot(rob_r, rob_c)
                except:
                    pass
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if event.button == 3 and isintable(pos):
                (x, y) = get_cords(pos)
                try:
                    paths = list(dfs_paths(smezh, points[rob_r][rob_c], points[y][x]))

                    paths2 = []
                    for i in paths:
                        paths2.append(len(i))
                    path = paths[paths2.index(min(paths2))]

                    rclear(rob_r, rob_c)
                    printpath(path)
                    (rob_r, rob_c) = (y, x)
                    robot(y, x)
                except:
                    print('Ход невозможен!')

                #(mx, my) = get_cords()
            elif event.button == 2:
                rerender()
    pygame.display.flip()
