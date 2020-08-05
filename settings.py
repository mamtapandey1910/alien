class Settings:
    def __init__(self):
        """Initialize the game static settings"""
        # screen settings

        self.screen_width= 1200
        self.screen_height= 600
        self.bg_color= (255,255,255)

        # ship setting
        self.ship_limit = 2

        # bullet settings
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # Alien settings
        self.fleet_drop_speed = 1

        # How quickly the game speed up.
        self.speedup_scale = 1.1

        # How quickly the alien point values increase.
        self.score_scale = 1.5

        self.initialize_dynamic_setting()

    def initialize_dynamic_setting(self):
        """ Initialize the setting that change throughout the game"""
        self.ship_speed = 2.5
        self.bullet_speed = 2.5
        self.alien_speed = 1

        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        """ Increase speed setting and alien point values"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)





