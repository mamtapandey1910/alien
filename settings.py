class Settings:
    def __init__(self):
        """Initialize the game settings"""
        #screen settings

        self.screen_width= 1200
        self.screen_height= 600
        self.bg_color= (255,255,255)

        #ship setting
        self.ship_speed = 2.5
        self.ship_limit = 3

        # bullet settings
        self.bullet_speed = 2.5
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 10

        # Alien settings
        self.alien_speed = 1
        self.fleet_drop_speed = 1
        # fleet_direction of 1 represents right, -1 represents left.
        self.fleet_direction = 1


