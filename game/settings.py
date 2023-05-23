class Settings():
    """Uma classe para armazenar as configurações"""
    def __init__(self):
        """inicializa as configurações do jogo"""
        # configurações da tela
        self.screen_width = 1200
        self.screen_height = 800
        # configurações dos alimentos
        self.food_speed_factor = 0.05
        self.object_speed_factor = 0.05
        self.food_number = 0
        self.object_number = 0
        self.max_vida = 2
