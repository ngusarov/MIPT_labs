from dataclasses import dataclass

import numpy as np
import scipy as sp
import scipy.optimize
import matplotlib.pyplot as plt


class PotHole:
    def __init__(self, V=0.3*1.6e-19, m=0.1 * 9.1e-31, a=50e-9):
        self.V = V
        self.m = m
        self.a = a
        self.hpl = 6.6e-34
        self.q = 1.6e-19
        self.k0 = np.sqrt(2*m*V/self.hpl**2)
        self.enlevels = set()

    def f(self, k):
        return np.tan(k * self.a / 2)

    def g1(self, k):
        return np.sqrt((self.k0**2 - k**2) / k ** 2)

    def g2(self, k):
        return -np.sqrt(k**2/(self.k0**2 - k**2))

    def h1(self, k):
        return self.f(k)-self.g1(k)

    def h2(self, k):
        return self.f(k)-self.g2(k)

    def find_levels(self):
        guess = 0
        while guess-np.pi <= self.k0*self.a:
            if guess == 0:
                guess = 0.01
                self.enlevels.add(sp.optimize.root(self.h1, np.array([guess / self.a]))['x'][0])
                guess = 0
            else:
                self.enlevels.add(sp.optimize.root(self.h1, np.array([guess / self.a]))['x'][0])
            guess += 2*np.pi

        guess = 0
        while guess-np.pi <= self.k0*self.a:
            if guess == 0:
                guess = 0.01
                self.enlevels.add(sp.optimize.root(self.h2, np.array([guess / self.a]))['x'][0])
                guess = 0
            else:
                self.enlevels.add(sp.optimize.root(self.h2, np.array([guess / self.a]))['x'][0])
            guess += 2*np.pi
        self.enlevels = sorted(self.enlevels)
        self.enlevels = [(each**2*self.hpl**2/(2*self.m))/self.q for each in self.enlevels]
        return self.enlevels

    def plot_hole(self):
        x = np.linspace(-self.a / 2, self.a / 2, 1000)
        for i, en in enumerate(self.enlevels):
            plt.plot(x, [en for each in x])
            if i % 2 == 0:
                plt.plot(x, [0.02 * np.cos(np.pi * (i + 1) * each / self.a) + en for each in x])
            else:
                plt.plot(x, [0.02 * np.sin(np.pi * (i + 1) * each / self.a) + en for each in x])
        plt.xlim(-self.a, self.a)
        plt.xlabel("x, [m]")
        plt.ylabel("E, [eV]")
        plt.savefig('pot_hole1.pdf', dpi=300)
        plt.close()

#(each**2*hpl**2/(2*m))/q
hole1 = PotHole(V=0.3*1.6e-19, m=0.1*9.1e-31, a=5.3e-9)
hole2 = PotHole(V=0.15*1.6e-19, m=0.6*9.1e-31, a=5.3e-9)
enlevels1 = hole1.find_levels()
enlevels2 = hole2.find_levels()
hole1.plot_hole()
hole2.plot_hole()
print(enlevels1)
print(enlevels2)

Eg = 1.401 - enlevels1[1] - enlevels2[1]
print(Eg)
