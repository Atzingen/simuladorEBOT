'''

'''

class Cinematica(object):
    '''
    Propriedades "Físicas" do carrinho simulado
    '''
    def __init__(self):
        # variáveis cinemáticas
        self.v_max = 50
        self.v_theta_max = 5
        # elementos incerciais
        self.massa = 0.1
        self.momento_inercia = 0.0005
        # Geradores de deslocamento
        self.forca_max_motor = 10
        self.braco_motor = 0.05 # Distância entre um motor e o centro de massa (eixo de rotação)
        self.freio_max = 50
    
    def rotacao(self, motor1, motor2, v_theta, delta_time):
        torque = self.braco_motor*(motor1 - motor2)
        a_theta = torque/self.momento_inercia
        v_theta += a_theta*delta_time
        
        if v_theta > self.v_theta_max:
            v_theta = self.v_theta_max
        elif v_theta < -self.v_theta_max:
            v_theta = -self.v_theta_max
        delta_theta = v_theta*delta_time
        return delta_theta, v_theta
    
    def translacao(self, motor1, motor2, v, delta_time):
        a = (motor1 + motor2)/self.massa
        v += a*delta_time
        if v > self.v_max:
            v = self.v_max
        elif v < -self.v_max:
            v = -self.v_max
        delta_mov = v*delta_time
        return delta_mov, v
               
        
    