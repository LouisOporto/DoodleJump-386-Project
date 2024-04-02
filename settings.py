class Settings:
    def __init__(self):
        #Game Screen
        self.screen_width = 900
        self.screen_height = 900
        self.background_color = (10, 10, 30)

        # Platform Spawning
        self.platform_spawn_rate = 30

        # Laser Settings
        self.laser_speed = 10
        self.laser_width = 5
        self.laser_height = 20
        self.laser_color = (0, 255, 255)
        #self.lasers_allowed = 3               (optional) limiting the amount of lasers on screen

        #Player Variables
        self.player_speed = 20
        self.jumping = False
        self.gravity = 10
        self.jump_height = 75
        self.y_velocity = self.jump_height

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.enemy_spawn_rate = 500

    def increase_dynamics(self):
        self.enemy_spawn_rate *= 0.9
        