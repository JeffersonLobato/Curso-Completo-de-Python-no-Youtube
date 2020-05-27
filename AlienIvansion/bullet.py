import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Uma classe que administra projéteis disparados pela espaçonave."""

    def __init__(self, ai_settings, screen, ship):
        """Cria um objeto para o projétil na posição atual da espaçonave."""
        super(Bullet, self).__init__()
        self.screen = screen

        # Cria um retângulo para o projétil em (0,0) e, em seguida, define a posição correta
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # Armazena a posição do projétil como um valor decimal
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move o projétil para cima na tela."""

        # Atualiza a posição decima do projétil
        self.y -= self.speed_factor
        # Atualiza a posição do rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Desenha o projétil na tela."""

        pygame.draw.rect(self.screen, self.color, self.rect)