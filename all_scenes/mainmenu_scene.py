import pygame
from scene import Scene
from gui import (Label, Button, Options)


class MainMenuScene(Scene):
    title = None

    single_player_btn = None
    multi_player_btn = None
    about_btn = None

    # Create the various gui elements
    def start(self, width, height):
        self.title = Label(pygame.rect.Rect(width / 2 - 200, height / 7, 400, 60), "Python PenFight!", options={
            Options.BACKGROUND: (20, 61, 89),
            Options.FOREGROUND: (244, 180, 26),
            Options.BORDER_WIDTH: 4,
            Options.FONT: pygame.font.SysFont("Comic Sans MS", 40, bold=True, italic=False)
        })

        btn_rect = pygame.rect.Rect(width / 2 - 125, height / 2 - 50, 250, 30)
        btn_options = {
            Options.BORDER_WIDTH: 0,
            Options.BACKGROUND: (20, 61, 89),
            Options.FOREGROUND: (244, 180, 26),
            Options.HOVERED_BACKGROUND: (10, 30, 45),
            Options.FONT: pygame.font.SysFont("Comic Sans MS", 25),
        }

        self.single_player_btn = Button(btn_rect, "Single Player", btn_options)
        self.multi_player_btn = Button(btn_rect.copy().move(0, 100), "Multi Player", btn_options)
        self.about_btn = Button(btn_rect.copy().move(0, 200), "About", btn_options)

    # Check the buttons and switch to corresponding scenes when clicked
    def update(self, event):
        for btn in (self.single_player_btn, self.multi_player_btn, self.about_btn):
            btn.update(event)

        # Goto single player enemy select scene
        if self.single_player_btn.clicked:
            Scene.change_scene(2)

        # Goto multi player network connection scene
        elif self.multi_player_btn.clicked:
            pass
            # Scene.change_scene(...)
            # Will add this later

        # Goto about the game scene
        elif self.about_btn.clicked:
            Scene.change_scene(7)

    # Clear the screen and draw the gui
    def draw(self, screen):
        screen.fill((82, 173, 200))

        self.title.draw(screen)

        for btn in (self.single_player_btn, self.multi_player_btn, self.about_btn):
            btn.draw(screen)
