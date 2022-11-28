import pygame
from screens import BaseScreen
from components import TextBox, InputBox
import requests


class UploadScoreScreen(BaseScreen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sprites = pygame.sprite.Group()
        self.toptext = TextBox(
            (300, 100), "Upload your score", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.usernametext = TextBox(
            (200, 50), "Enter Username:", color=(0, 0, 0), bgcolor=(255, 255, 255)
        )
        self.name_input = InputBox(
            (300, 100), self.store.last_username, color=(255, 255, 255), bgcolor=(0, 0, 0)
        )

        self.upload_button = TextBox(
            (200, 100), "Upload Score", color=(100, 100, 200), bgcolor=(255, 100, 50)
        )
       
        self.toptext.rect.topleft = (250, 100)
        self.name_input.rect.topleft = (250, 280)
        self.usernametext.rect.topleft = (250, 230)
        self.upload_button.rect.topleft = (300, 500)
        self.sprites.add(self.upload_button, self.toptext, self.name_input, self.usernametext)
        self.activeinput = None

    def draw(self):
        self.window.fill((255, 255, 255))
        self.sprites.draw(self.window)

    def update(self):
        print("updatating...")
        if self.name_input.text == "":
            self.upload_button.bgcolor = (130, 130, 130)
        else:
            self.upload_button.bgcolor = (255, 100, 50)
        self.upload_button.draw()


    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.name_input.rect.collidepoint(event.pos):
                if self.activeinput:
                    self.activeinput.set_active(False)
                self.activeinput = self.name_input
                self.activeinput.set_active(True)
            elif self.upload_button.rect.collidepoint(event.pos) and self.name_input.text != "":
                self.store.last_username = self.name_input.text
                requests.post("http://127.0.0.1:5000/api/add_score", json={ "username": self.store.last_username, "score": self.store.score })
                self.running = False
                self.next_screen = "welcome"
                
        if self.activeinput is not None:
            self.activeinput.update(event)
