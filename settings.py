class Settings:
    def __init__(self):
        #Game Screen
        self.screen_width = 600
        self.screen_height = 1000
        self.background_color = (10, 10, 30)

        # Platform Spawning
        self.platform_spawn_rate = 30
        self.platform_height = 10
        self.platform_max_width = 100
        self.platform_min_width = 40
        self.platform_color = (255, 255, 255)

        # Laser Settings
        self.laser_speed = 10
        self.laser_width = 5
        self.laser_height = 20
        self.laser_color = (0, 255, 255)
        self.lasers_allowed = 5               #(optional) limiting the amount of lasers on screen

        #Player Variables
        self.image_scale = 75
        self.player_speed = 20
        self.dog_speed = 5
        self.gravity = 1
        self.fall_speed = 20
        self.jump_height = 25

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        self.dog_spawn_rate = 500
        self.dog_shoot = 100
        self.platform_point = 100
        self.dog_point = 250
        self.next_level = 10

    def increase_dynamics(self):
        self.dog_spawn_rate = self.dog_spawn_rate // 1.1
        self.dog_shoot = self.dog_shoot // 1.1
        self.platform_point *= 1.1
        self.dog_point *= 1.1
        self.next_level += 2
        

if __name__ == '__main__':
    print("\nERROR: settings.py is the wrong file! To play run game.py\n")