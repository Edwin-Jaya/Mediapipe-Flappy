from bird import PixelBird
from pipe import Pipe
import pygame
import random
from controller import MediaPipeController

class Game:
    def __init__(self, controller=None):
        self.state = "menu"  
        self.controller = controller or MediaPipeController()
        self.bird = PixelBird(100, 300)
        self.score = 0
        self.pipes = []
        self.running = True
        self.font = pygame.font.Font(None, 48)

    def reset(self):

        self.bird = PixelBird(100, 300)
        self.score = 0
        self.pipes = [Pipe(400, random.randint(150, 400))]
        self.state = "playing"

    def update(self):
        if self.state == "playing":
            if self.controller.update():   
                self.bird.jump()
            else:
                self.bird.update_pos()


            for pipe in self.pipes:
                pipe.update()
                if self.check_collision(self.bird, pipe):
                    self.state = "game_over"


                if not hasattr(pipe, "scored") and pipe.x + pipe.pipe_width < self.bird.x:
                    self.score += 1
                    pipe.scored = True


            self.pipes = [pipe for pipe in self.pipes if pipe.x + pipe.pipe_width > 0]


            if len(self.pipes) < 2:
                new_gap_y = random.randint(150, 400)
                self.pipes.append(Pipe(400, new_gap_y))

    def check_collision(self, bird, pipe):
        bx, by, r = bird.x, bird.y, bird.radius
        top_rect, bottom_rect = pipe.get_rects()

        for rect in [top_rect, bottom_rect]:
            closest_x = max(rect.left, min(bx, rect.right))
            closest_y = max(rect.top, min(by, rect.bottom))
            dx = bx - closest_x
            dy = by - closest_y
            if dx * dx + dy * dy < r * r:
                return True
        return False

    def draw(self, screen):
        if self.state == "menu":
            self.draw_menu(screen)
        elif self.state == "playing":
            self.draw_playing(screen)
        elif self.state == "game_over":
            self.draw_game_over(screen)

    def draw_menu(self, screen):
        title = self.font.render("Flappy Bird", True, (255, 255, 255))
        prompt = self.font.render("Press SPACE to Start", True, (200, 200, 200))
        screen.blit(title, (100, 200))
        screen.blit(prompt, (50, 300))

    def draw_playing(self, screen):
        self.bird.draw(screen)
        for pipe in self.pipes:
            pipe.draw(screen)

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

    def draw_game_over(self, screen):
        game_over = self.font.render("Game Over!", True, (255, 0, 0))
        retry = self.font.render("Press R to Retry", True, (200, 200, 200))
        main_menu = self.font.render("Press M for Menu", True, (200, 200, 200))
        final_score = self.font.render(f"Final Score: {self.score}", True, (255, 255, 0))

        screen.blit(game_over, (100, 200))
        screen.blit(retry, (80, 300))
        screen.blit(main_menu, (60, 360))
        screen.blit(final_score, (90, 420))
