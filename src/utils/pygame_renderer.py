import pygame
import sys
from models.Map import Map
from models.MovingObject import Pacman, Ghost
from utils.enums import *

pygame.init()

font = pygame.font.SysFont('Arial', FONT_SIZE)
big_font = pygame.font.SysFont('Arial', BIG_FONT_SIZE)
title_font = pygame.font.SysFont('Arial', TITLE_FONT_SIZE, bold=True)

class PygameRenderer:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(PygameRenderer, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.screen = None
        self.clock = pygame.time.Clock()
        self.fps = FRAMES_PER_SECOND

    def initialize(self, map_width, map_height):
        self.screen_width = map_width * CELL_SIZE
        self.screen_height = map_height * CELL_SIZE + INFO_HEIGHT
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Pac-Man Game')

    def render_menu(self, selected_level=0):
        if self.screen is None:
            self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
            pygame.display.set_caption('Pac-Man Menu')

        self.screen.fill(BLACK)

        title_surface = title_font.render('PAC-MAN Main Menu', True, YELLOW)
        self.screen.blit(title_surface, (WINDOW_WIDTH // 2 - title_surface.get_width() // 2, 
                            title_surface.get_height()))

        level_titles = [
            "Level 1: Blue Ghost using BFS",
            "Level 2: Pink Ghost using DFS/IDDFS",
            "Level 3: Orange Ghost using UCS",
            "Level 4: Red Ghost using A*",
            "Level 5: All Ghosts (Parallel Execution)",
            "Level 6: User-Controlled Pac-Man"
        ]

        for i, title in enumerate(level_titles):
            color = YELLOW if i == selected_level else WHITE
            text_surface = big_font.render(title, True, color)
            y_position = 150 + i * 60
            self.screen.blit(text_surface, (WINDOW_WIDTH // 2 - text_surface.get_width() // 2, y_position))

        instructions = font.render("Use UP/DOWN arrows to navigate. ENTER to select.", True, RED)
        self.screen.blit(instructions, (WINDOW_WIDTH // 2 - instructions.get_width() // 2, 520))

        pygame.display.flip()
        self.clock.tick(FRAMES_PER_SECOND)

    def render_game(self, map: Map, pacman: Pacman, ghosts: list[Ghost], level: int, metrics=None):
        if self.screen is None or self.screen_width != map.M * CELL_SIZE or self.screen_height != map.N * CELL_SIZE + INFO_HEIGHT:
            self.initialize(map.M, map.N)

        self.screen.fill(BLACK)

        for i in range(map.N):
            for j in range(map.M):
                cell = map.get_cell(i, j)
                rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                
                if cell == CELL_TYPES['WALL']:
                    pygame.draw.rect(self.screen, BLUE, rect)
                elif cell == CELL_TYPES['FOOD']:
                    pygame.draw.circle(self.screen, YELLOW, 
                                      (j * CELL_SIZE + CELL_SIZE // 2, i * CELL_SIZE + CELL_SIZE // 2), 
                                      CELL_SIZE // 6)

        pacman.draw(self.screen)

        for idx, ghost in enumerate(ghosts):
            ghost.draw(self.screen)

        info_rect = pygame.Rect(0, map.N * CELL_SIZE, self.screen_width, INFO_HEIGHT)
        pygame.draw.rect(self.screen, GREY, info_rect)

        level_text = font.render(f"Level: {level}", True, WHITE)
        score_text = font.render(f"Score: {pacman.score}", True, WHITE)
        lives_text = font.render(f"Lives: {pacman.lives}", True, WHITE)
        
        self.screen.blit(level_text, (10, map.N * CELL_SIZE + 10))
        self.screen.blit(score_text, (10, map.N * CELL_SIZE + 30))
        self.screen.blit(lives_text, (120, map.N * CELL_SIZE + 10))

        if metrics:
            metrics_text = font.render(f"Search Time: {metrics['search_time']:.4f}s | Nodes: {metrics['expanded_nodes']}", True, WHITE)
            self.screen.blit(metrics_text, (220, map.N * CELL_SIZE + 10))

            if 'memory_usage' in metrics:
                memory_text = font.render(f"Memory: {metrics['memory_usage']}", True, WHITE)
                self.screen.blit(memory_text, (220, map.N * CELL_SIZE + 30))

        pygame.display.flip()
        self.clock.tick(self.fps)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
        return pygame.key.get_pressed()

    def set_fps(self, fps):
        self.fps = fps

    def get_menu_input(self):
        selected = 0
        while True:
            self.render_menu(selected)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    elif event.key == pygame.K_UP:
                        selected = (selected - 1) % NUM_LEVELS
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % NUM_LEVELS
                    elif event.key == pygame.K_RETURN:
                        return selected + 1
                        
            self.clock.tick(10)

    def show_game_over(self, score):
        overlay = pygame.Surface((self.screen_width, self.screen_height))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        self.screen.blit(overlay, (0, 0))
        
        game_over_text = big_font.render("GAME OVER", True, RED)
        score_text = big_font.render(f"Final Score: {score}", True, YELLOW)
        continue_text = font.render("Press any key to continue", True, WHITE)
        
        self.screen.blit(game_over_text, (self.screen_width//2 - game_over_text.get_width()//2, 
                                         self.screen_height//2 - 60))
        self.screen.blit(score_text, (self.screen_width//2 - score_text.get_width()//2, 
                                     self.screen_height//2))
        self.screen.blit(continue_text, (self.screen_width//2 - continue_text.get_width()//2, 
                                       self.screen_height//2 + 60))
        
        pygame.display.flip()
        
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    waiting = False
                    self.screen = None