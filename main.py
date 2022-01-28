import random, os, sys
import numpy as np
import arcade
from robo import Robo, Sensores
import pista


class TelaPrincipal(arcade.Window):
    """ Main application class. """

    def __init__(self):
        self.SCREEN_HEIGHT = 600  # Mapa de 600x600
        self.SCREEN_WIDTH = 800   # Lateral de 200x600 para debug
        self.fps = 1
        self.fps_counter = 0
        self.sensorlinha = Sensores(5, 60, 30)
        self.robo = Robo(400, 100, 0)
        super().__init__(self.SCREEN_WIDTH, self.SCREEN_HEIGHT, 
                         "Simulador - Seguidor de linha EBOT")
        arcade.set_background_color(arcade.color.BLUE_GRAY)

    def on_draw(self):
        '''
        Atualiza a cada frame
        '''    
        arcade.start_render()
        pontos_pista = pista.gera_pontos()
        arcade.draw_ellipse_outline(self.SCREEN_WIDTH/2, self.SCREEN_HEIGHT/2,
                                    600, 400, arcade.color.BLACK, 12)
        # arcade.draw_line_strip(pontos_pista,
        #                        arcade.color.BLACK, 18)
        self.robo.le_sensores(arcade, 
            self.sensorlinha.gera_pontos_sensores(self.robo.x, self.robo.y, self.robo.theta),
            self.sensorlinha)
        self.sensorlinha.desenha_sensors(arcade, self.robo.x, self.robo.y, self.robo.theta)
        arcade.draw_circle_filled(  # ROBO
            self.robo.x, self.robo.y, 
            self.robo.raio, arcade.color.BLUE
        )
        arcade.draw_line(           # Linha mostrando "frente" do robo
            self.robo.x, self.robo.y,
            self.robo.x + self.robo.raio*np.cos(self.robo.theta),
            self.robo.y + self.robo.raio*np.sin(self.robo.theta),
            arcade.color.BLACK, 5
        )
        arcade.draw_text(f'fps: {self.fps:.2f} ', 10, 20, arcade.color.WHITE, 14)

    def update(self, delta_time):
        self.fps_counter += 1
        self.fps = 1/delta_time
        s = self.sensorlinha.ultima_leitura
        if s[0] == 1 or s[1] == 1:
            me = 2
            md = 0
        elif s[-1] == 1 or s[-2] == 1:
            me = 0
            md = 2
        else:
            me, md = 2, 2
        self.robo.anda(me, md, delta_time)
        print(s, me, md)

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