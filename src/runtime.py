from src.common.config import Config
from src.controllers.screen_controller import *
import src.controllers.screen_controller


class Runtime:

    def __init__(self):
        self.config = Config()
        self.clock = pygame.time.Clock()
        # info_object = pygame.display.Info()
        # self.size = self.width, self.height = info_object.current_w, info_object.current_h
        self.width = int(1800)
        self.height = int(1000)
        self.size = self.width, self.height
        self.screen = pygame.display.set_mode((1800,1000))
        self.current_screen = None
        self.screens = dict()  # {INTRO_SCREEN: IntroScreenController(self), }
        self.set_current_screen(self.config.values[CONFIG_FIRST_SCREEN])
        self.game = None

    def set_current_screen(self, screen_name):
        self.current_screen = screen_name
        if self.current_screen not in self.screens:
            screen_class = getattr(src.controllers.screen_controller, self.current_screen)
            self.screens[self.current_screen] = screen_class(self)
