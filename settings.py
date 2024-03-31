class Settings:
    def __init__(self):
        self.screen_width = 700
        self.screen_height = 700
        self.background_color = (10, 10, 30)

        self.platform_spawn_rate = 30
        
        self.gravity = 10
        self.player_speed = 10

        self.laser_speed = 2.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (60, 60, 60)

        self.initialize_dynamic_settings()
    
    # TODO Add more dynmaic settings that would challenge the game overtime. Everytime player hits a platform the dificullty scales.
    # Or certain distance mark has been passed.
    def initialize_dynamic_settings(self):
        self.enemy_spawn_rate = 500

    def increase_dynamics(self):
        self.enemy_spawn_rate *= 0.9
        