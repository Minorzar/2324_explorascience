import pygame
import random

WHITE = (255, 255, 255, 255)
ALPHA = 100

BLOCK_COLORS = {
    0: (240, 128, 128, ALPHA),  # Red
    1: (152, 251, 152, ALPHA),  # Green
    2: (135, 206, 235, ALPHA),  # Blue
    3: (127, 255, 212, ALPHA),  # Cyan
    4: (147, 112, 219, ALPHA),  # Magenta
    5: (250, 250, 210, ALPHA),  # Yellow
    6: (244, 164, 96, ALPHA),  # Orange
    7: (255, 182, 193, ALPHA),  # Pink
    8: (119, 136, 153, ALPHA)  # Gray
}

CELL_W = 50
CELL_H = 50
X_OFFSET = 30
Y_OFFSET = 100

pygame.font.init()
my_font = pygame.font.SysFont('Century Schoolbook', 30)


class Cell:
    def __init__(self, x, y, value=0):
        self.row = x
        self.column = y
        self.value = value
        self.block = y // 3 + (x // 3) * 3

        self.collapsed = False
        self.options = [i + 1 for i in range(9)]

    def show(self, screen):
        rec = pygame.Rect((X_OFFSET + self.column * CELL_W, Y_OFFSET + self.row * CELL_H, CELL_W, CELL_H))
        screen.fill(pygame.Color("black"),
                         (X_OFFSET + self.column * CELL_W, Y_OFFSET + self.row * CELL_H, CELL_W, CELL_H))

        surf = pygame.Surface((CELL_W - 20, CELL_H - 20), flags=pygame.SRCALPHA)
        surf.fill(BLOCK_COLORS[self.block])
        screen.blit(surf, (X_OFFSET + self.column * CELL_W + 10, Y_OFFSET + self.row * CELL_H + 10))

        pygame.draw.rect(screen, WHITE, rec, width=1)
        value_text = my_font.render(str(self.value), False, WHITE)

        if self.value:
            screen.blit(value_text, (X_OFFSET + self.column * CELL_W + 15, Y_OFFSET + self.row * CELL_H + 5))

    def update_value(self):
        self.value = (self.value + 1) % 10

    def collapse(self, value=None):
        self.collapsed = True
        choice = None

        if value is None:
            choice = random.choice(self.options)
        else:
            choice = value  # Collapse to entered value

        self.value = choice
        self.options = [choice]

    def getInfo(self):  # FOR DEBUGGING PURPOSES
        print(
            f"\nRow : {self.row}\nColumn : {self.column}\nBlock : {self.block}\nValue: {self.value}"
        )