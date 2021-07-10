import sys, os, time
import numpy as np
from fisica import Cinematica

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
        self.theta, self.v_theta = self.rotacao(motor1, motor2, self.v_theta, delta_time)
        ds, self.v = self.translacao(motor1, motor2, self.v, delta_time)
        self.update_cartesiano(ds)
        
    def update_cartesiano(self, ds):
        self.x += ds*np.cos(self.theta)
        self.y += ds*np.sin(self.theta)
    
    def __str__(self):
        return f'X:{self.x} Y:{self.y} V:{self.v} Theta:{self.theta} V_theta:{self.v_theta}'
    
    def __repr__(self):
        return f'X:{self.x} Y:{self.y} V:{self.v} Theta:{self.theta} V_theta:{self.v_theta}'
        

        