class Settings():
    """"A class to store all settings for ALien Invasion."""

    def __init__(self):
        """"Initialize the game's static settings."""

        #screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # ship settings
        self.ship_speed_factor = 1.5
        self.ship_limit = 3