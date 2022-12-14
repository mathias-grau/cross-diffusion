from lib.animation import Animate
from lib.euler import BackwardEuler
from lib.utils import UVtoX
import numpy as np


class Population:

    Xlist = []

    def __init__(self, Space: np.ndarray, u0, v0, D: np.ndarray):
        self.D = D
        self.Space = Space
        X0 = UVtoX(u0(Space), v0(Space))
        self.Xlist = [X0]
        self.Tlist = np.array([0])

    def sim(self, duration: float, N=100):
        Time = np.linspace(0, duration, N)
        self.Tlist = np.append(self.Tlist,
                               self.Tlist[-1] + Time)
        X0 = self.Xlist[-1].copy()
        self.Xlist = self.Xlist + BackwardEuler(X0, Time, self.Space, self.D)

    def anim(self, length=5, filename=None):
        K, N = len(self.Space), len(self.Tlist)
        txt = 'D={}, K={}, N={}'.format(
            str(self.D).replace('\n', ''), K, N - 2)
        Animate(self.Space,
                self.Xlist,
                self.Tlist,
                length=length,
                text=txt,
                filename=filename)
