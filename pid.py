class PID(object):
    def __init__(self, P=1, I=0.1, D=0.1, 
                 obj=0, ki_max=10):
        self.kp = P
        self.kd = I
        self.ki = D
        self.dt = 0.01
        self.obj = obj
        self.ki_max = ki_max
        self.clear()

    def clear(self):
        self.ultimo_erro = 0
        self.I = 0
        self.D = 0

    def update(self, raio, ponto_atual):
        erro = ponto_atual - self.obj
        self.I += erro*self.dt
        if self.I > self.ki_max:
            self.I = self.ki_max
        elif self.I < -self.ki_max:
            self.I = -self.ki_max
        delta_erro = (erro - self.ultimo_erro)/self.dt
        self.ultimo_erro = erro
        return self.kp*erro + self.ki*self.I + self.kd*self.D

def bound(v):
    if v > 1:
        v = 1
    elif v < 0:
        v = 0
    return v

def motor(pid_out, raio):
    md = (raio/100)*(1 - pid_out)
    me = (raio/100)*(pid_out + 1)
    return bound(md), bound(me)
    
