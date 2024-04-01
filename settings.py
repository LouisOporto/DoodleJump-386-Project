class Settings:
    def __init__(self):
        self.screen_width = 900
        self.screen_height = 900
        self.background_color = (10, 10, 30)

        self.platform_spawn_rate = 30

        self.player_speed = 20

        self.laser_speed = 2.0
        self.laser_width = 3
        self.laser_height = 15
        self.laser_color = (0, 255, 255)

        self.jumping = False
        self.gravity = 10
        self.jump_height = 75
        self.y_velocity = self.jump_height

        self.initialize_dynamic_settings()
    
    # TODO Add more dynmaic settings that would challenge the game overtime. Everytime player hits a platform the dificullty scales.
    # Or certain distance mark has been passed.
    def initialize_dynamic_settings(self):
        self.enemy_spawn_rate = 500

    def increase_dynamics(self):
        self.enemy_spawn_rate *= 0.9
        