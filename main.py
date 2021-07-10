import random, os, sys
import numpy as np
import arcade
from robo import Robo

class TelaPrincipal(arcade.Window):
    """ Main application class. """

    def __init__(self):
        self.SCREEN_HEIGHT = 600  # Mapa de 600x600
        self.SCREEN_WIDTH = 800   # Lateral de 200x600 para debug
        self.fps = 1
        self.fps_counter = 0
        self.robo = Robo(200, 200, 0)
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 
                         "Simulador - Seguidor de linha EBOT")
        arcade.set_background_color(arcade.color.BLUE_GRAY)

    def on_draw(self):
        '''
        Atualiza a cada frame
        '''    
        arcade.start_render()
        arcade.draw_circle_filled(  # ROBO
            self.robo.x, self.robo.y, 
            self.robo.raio, arcade.color.BLUE
        )
        arcade.draw_line(           # Linha mostrando "frente" do robo
            self.robo.x, self.robo.y,
            self.robo.x + self.robo.raio*np.cos(self.robo.theta),
            self.robo.y + self.robo.raio*np.sin(self.robo.theta),
            arcade.color.BLACK_OLIVE, 5
        )
        arcade.draw_line(           # Linha mostrando "frente" do robo
            self.robo.x, self.robo.y,
            self.robo.x + self.robo.raio*np.cos(self.robo.theta),
            self.robo.y + self.robo.raio*np.sin(self.robo.theta),
            arcade.color.BLACK, 5
        )
        arcade.draw_line(           # Linha mostrando "frente" do robo
            self.robo.x + self.robo.raio*np.cos(self.robo.theta + np.pi/2),
            self.robo.y + self.robo.raio*np.sin(self.robo.theta + np.pi/2),
            self.robo.x + self.robo.raio*np.cos(self.robo.theta - np.pi/2),
            self.robo.y + self.robo.raio*np.sin(self.robo.theta - np.pi/2),
            arcade.color.YELLOW_GREEN, 5
        )
        arcade.draw_text(f'fps: {self.fps:.2f} !', 20, 200, arcade.color.WHITE, 14)
        arcade.draw_text(f'Hello !', 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        '''

        '''
        self.fps_counter += 1
        self.fps = 1/delta_time
        self.robo.anda(10, 10, delta_time)
        print(self.robo)

    def on_mouse_press(self, x, y, button, modifiers):
        '''
        Called whenever the mouse button is clicked.
        '''
        pass


def main():
    TelaPrincipal()
    arcade.run()


if __name__ == "__main__":
    main()