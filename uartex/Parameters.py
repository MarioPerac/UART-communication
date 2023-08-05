class QuaternionParam:
    def __init__(self, q0, q1, q2, q3):
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3

    @property
    def parameters(self):
        return self.q0, self.q1, self.q2, self.q3

    def set_parameters(self, q0, q1, q2, q3):
        self.q0 = q0
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3


class GyroParam:
    def __init__(self, gx, gy, gz):
        self.gx = gx
        self.gy = gy
        self.gz = gz

    @property
    def parameters(self):
        return self.gx, self.gy, self.gz

    def set_parameters(self, gx, gy, gz):
        self.gx = gx
        self.gy = gy
        self.gz = gz


class AccelerometerParam:
    def __init__(self, ax, ay, az):
        self.ax = ax
        self.ay = ay
        self.az = az

    @property
    def parameters(self):
        return self.ax, self.ay, self.az

    def set_parameters(self, ax, ay, az):
        self.ax = ax
        self.ay = ay
        self.az = az


class MagnetometerParam:
    def __init__(self, mx, my, mz):
        self.mx = mx
        self.my = my
        self.mz = mz

    @property
    def parameters(self):
        return self.mx, self.my, self.mz

    def set_parameters(self, mx, my, mz):
        self.mx = mx
        self.my = my
        self.mz = mz
