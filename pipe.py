import pygame

class Pipe:
    def __init__(self, x, gap_y, gap_height=300, speed=5):
        self.x = x
        self.gap_y = gap_y
        self.gap_height = gap_height
        self.speed = speed

        self.pipe_width = 80
        self.pipe_height = 400

        self.pipe_img = pygame.Surface((self.pipe_width, self.pipe_height))
        self.pipe_img.fill((0, 200, 0)) 
        self.pipe_img_flipped = pygame.transform.flip(self.pipe_img, False, True)


        self.update_rects()

    def update(self):

        self.x -= self.speed
        self.update_rects()

    def update_rects(self):
 
        top_y = self.gap_y - self.pipe_height
        bottom_y = self.gap_y + self.gap_height

        self.top_rect = pygame.Rect(self.x, top_y, self.pipe_width, self.pipe_height)
        self.bottom_rect = pygame.Rect(self.x, bottom_y, self.pipe_width, self.pipe_height)

    def draw(self, screen):

        screen.blit(self.pipe_img_flipped, self.top_rect.topleft)
        screen.blit(self.pipe_img, self.bottom_rect.topleft)

    def get_rects(self):
        return self.top_rect, self.bottom_rect
