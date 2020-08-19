class GameStats():
    """Armazena dados estatísticos da Invasão Alienígena."""

    def __init__(self, ai_settings):
        """Inicializa os dados estatísticos."""
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0

    def reset_stats(self):
        """Inicializa os dados estatísticos que podem mudar durante o jogo."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
