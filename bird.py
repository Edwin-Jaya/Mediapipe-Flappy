import pygame

class PixelBird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.velocity = 0
        self.gravity = 0.5
        self.jump_strength = -5
        self.image = pygame.image.load("./assets/dababy-convertible.png")  
    
    def jump(self):
        self.velocity = self.jump_strength
    
    def update_pos(self):
        self.velocity += self.gravity      
        self.y += self.velocity            
    
    def draw(self, screen):
        # pygame.draw.circle(screen, (0, 0, 0), (int(self.x), int(self.y)), self.radius)
        screen.blit(self.image, (self.x - self.image.get_width()//2,
                         self.y - self.image.get_height()//2))
