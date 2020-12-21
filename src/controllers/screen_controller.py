from src.common.constants import *
from src.screens.screens import *
from src.screens import *
from src.controllers.game_controller import *
from src.ui.text_input import TextInput
from src.ui.popup import PopUp
from datetime import datetime
import pygame


class ScreenController:

    def __init__(self, runtime):
        self.runtime = runtime
        self.last_generic_action = ''
        self._screen = None
        self.active = True

    def display(self):
        self._screen.display()

    def update(self):
        self.last_generic_action = 'UPDATE'

    def handle_event(self, event):
        self.last_generic_action = 'HANDLE_EVENT'

    def handle_switch_to(self):
        self.last_generic_action = 'HANDLE_SWITCH_TO'


class StartScreenController(ScreenController):

    def __init__(self, runtime):
        super(self.__class__, self).__init__(runtime)
        self.games_list = None
        self.reset()
        self._screen = StartScreen(self)

    def handle_event(self, event):
        if self.active:
            if event.type == pygame.MOUSEBUTTONUP:
                clicked_object = self._view.get_object_under_mouse()
                if clicked_object is not None:
                    if str(clicked_object.element_id).startswith(GAME_BUTTON):
                        splits = str(clicked_object.element_id).split(':')
                        self.runtime.game = GameController(self.runtime, splits[1])
                        if self.runtime.game.new:
                            self.runtime.set_current_screen(GAME_CREATION_SCREEN)
                            return True
                    if str(clicked_object.element_id).startswith(GAME_DELETE):
                        splits = str(clicked_object.element_id).split(':')
                        self.runtime.game = GameController(self.runtime, splits[1])
                        self.active = False
                        deletion_confirmation = PopUp(self.runtime,
                                                      TEXT_DO_YOU_WANT_TO_DELETE,
                                                      ((1, TEXT_YES), (0, TEXT_NO)), 250, 125
                                                      ).display()
                        self.active = True
                        if deletion_confirmation == 1 and not self.runtime.game.new:
                            self.runtime.game.reset()
                            PopUp(self.runtime,
                                  'Löschen erfolgreich',
                                  ((1, TEXT_OK),), 250, 125
                                  ).display()
                            return True

    def reset(self):
        self._view = StartScreen(self)

    def update(self):
        return True


