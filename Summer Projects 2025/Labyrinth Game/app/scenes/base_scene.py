# app/scenes/base_scene.py
from abc import ABC, abstractmethod


class Scene(ABC):
    def __init__(self, app):
        self.app = app

    @abstractmethod
    def handle_events(self):
        pass

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
