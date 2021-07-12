import sys, os, time, math
import numpy as np
from fisica import Cinematica


class Sensores:
    def __init__(self, n_sensores, comprimento_sensores, distancia_centro):
        self.n_sensores = n_sensores
        self.comprimento_sensores = comprimento_sensores
        self.distancia_centro = distancia_centro

    def gera_pontos_sensores(self, x, y, theta):
        x1 = x + self.distancia_centro*np.cos(theta)
        y1 = y + self.distancia_centro*np.sin(theta)
        theta2 = (np.pi/2) + theta
        d = self.comprimento_sensores/(self.n_sensores-1)
        pontos = [(x1, y1)]
        for i in range(math.floor(self.n_sensores/2)):
            x2 = x1 + (i+1)*d*np.cos(theta2)
            y2 = y1 + (i+1)*d*np.sin(theta2)
            x3 = x1 - (i+1)*d*np.cos(theta2)
            y3 = y1 - (i+1)*d*np.sin(theta2)
            pontos.append((x2, y2))
            pontos.append((x3, y3))
        return pontos

    def desenha_sensors(self, arcade, x, y, theta):
        x1 = x + self.distancia_centro*np.cos(theta)
        y1 = y + self.distancia_centro*np.sin(theta)
        theta2 = (np.pi/2) + theta
        # theta3 = theta - (np.pi/2)
        x2 = x1 + (self.comprimento_sensores/2)*np.cos(theta2)
        y2 = y1 + (self.comprimento_sensores/2)*np.sin(theta2)
        x3 = x1 - (self.comprimento_sensores/2)*np.cos(theta2)
        y3 = y1 - (self.comprimento_sensores/2)*np.sin(theta2)
        arcade.draw_line(x2, y2, x3, y3, arcade.color.GREEN, 5)
        pontos = self.gera_pontos_sensores(x, y, theta)
        for ponto in pontos:
            arcade.draw_circle_filled(  # ROBO
            ponto[0], ponto[1], 
            2, arcade.color.RED
            )

    def le_sensores(self, arcade):
        pass

class Robo(Cinematica):
    '''
    Guarda de atualiza os estados do robo
    '''
    def __init__(self, x, y, theta):
        '''
        
        '''
        self.x = x
        self.y = y
        self.raio = 30
        self.theta = theta
        self.v = 0
        self.v_theta = 0
        Cinematica.__init__(self)
                
    def anda(self, motor1, motor2, delta_time):
        delta_theta, self.v_theta = self.rotacao(motor1, motor2, self.v_theta, delta_time)
        self.theta += delta_theta
        ds, self.v = self.translacao(motor1, motor2, self.v, delta_time)
        self.update_cartesiano(ds)
        
    def update_cartesiano(self, ds):
        self.x += ds*np.cos(self.theta)
        self.y += ds*np.sin(self.theta)
    
    def __str__(self):
        return f'X:{self.x} Y:{self.y} V:{self.v} Theta:{self.theta} V_theta:{self.v_theta}'
    
    def __repr__(self):
        return f'X:{self.x} Y:{self.y} V:{self.v} Theta:{self.theta} V_theta:{self.v_theta}'
        

        