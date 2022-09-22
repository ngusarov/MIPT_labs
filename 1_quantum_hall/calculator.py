from dataclasses import dataclass

import numpy as np
import scipy as sp
import scipy.optimize
import matplotlib.pyplot as plt

me = 9.1e-31
q = 1.6e-19
hpl = 1.055e-34

class PotHole:
    def __init__(self, V=0.3*q, m1=0.067*me, m2=0.067*me, a=50e-9):
        self.V = V
        self.m1 = m1
        self.m2 = m2
        self.a = a
        self.k0 = np.sqrt(2*m1*V/hpl**2)
        self.enlevels = set()

    def f(self, k):
        return np.tan(k * self.a / 2)

    def g1(self, k):
        return np.sqrt((self.k0**2 - k**2) / k ** 2)*np.sqrt(self.m1/self.m2)

    def g2(self, k):
        return -np.sqrt(k**2/(self.k0**2 - k**2))*np.sqrt(self.m2/self.m1)

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
        self.enlevels = [(each**2*hpl**2/(2*self.m1))/q for each in self.enlevels]
        return self.enlevels

    def plot_hole(self, filename):
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
        plt.annotate(filename, xy=(self.a/2, max(self.enlevels)))
        plt.annotate('$m_1$='+str(self.m1/me), xy=(-self.a, max(self.enlevels)))
        plt.annotate('$m_2$='+str(self.m2 / me), xy=(-self.a, max(self.enlevels)/2))
        plt.savefig('pot_hole_'+filename+'.pdf', dpi=300)
        #plt.show()
        plt.close()


#A579
hole_el = PotHole(V=0.3*q, m1=0.067*me, m2=0.067*me, a=5.3e-9)
hole_heavy_hole = PotHole(V=0.15*q, m1=0.45*me, m2=0.45*me, a=5.3e-9)
hole_light_hole = PotHole(V=0.15*q, m1=0.082/0.8*me, m2=0.0082*me, a=5.3e-9)
enlevels_el = hole_el.find_levels()
enlevels_hh = hole_heavy_hole.find_levels()
enlevels_lh = hole_light_hole.find_levels()
hole_el.plot_hole('Electron')
hole_heavy_hole.plot_hole('Heavy_hole')
hole_light_hole.plot_hole('Light_hole')
print(enlevels_el)
print(enlevels_hh)
print(enlevels_lh)

print('Light hole vs heavy hole theory')
Eg = 1.401 - enlevels_el[1] - enlevels_hh[1]
print(Eg)
Eg = 1.424 - enlevels_el[1] - enlevels_lh[1]
print(Eg)

print('Second level theory')
Eg = 1.401 - enlevels_el[1] - enlevels_hh[1]
print(Eg)
Eg = 1.424 - enlevels_el[2] - enlevels_hh[2]
print(Eg)
Eg = 1.424 - enlevels_el[2] - enlevels_lh[2]
print(Eg)


#A580
hole_el = PotHole(V=0.3*q, m1=0.067*me, m2=0.067*me, a=2.8e-9)
hole_heavy_hole = PotHole(V=0.15*q, m1=0.45*me, m2=0.45*me, a=2.8e-9)
hole_light_hole = PotHole(V=0.15*q, m1=0.082/0.8*me, m2=0.0082*me, a=2.8e-9)
enlevels_el = hole_el.find_levels()
enlevels_hh = hole_heavy_hole.find_levels()
enlevels_lh = hole_light_hole.find_levels()
hole_el.plot_hole('Electron')
hole_heavy_hole.plot_hole('Heavy_hole')
hole_light_hole.plot_hole('Light_hole')
print(enlevels_el)
print(enlevels_hh)
print(enlevels_lh)

print('Light hole vs heavy hole theory')
Eg = 1.502 - enlevels_el[1] - enlevels_hh[1]
print(Eg)
Eg = 1.516 - enlevels_el[1] - enlevels_lh[1]
print(Eg)

print('Second level theory')
Eg = 1.502 - enlevels_el[1] - enlevels_hh[1]
print(Eg)
Eg = 1.516 - enlevels_el[2] - enlevels_hh[2]
print(Eg)
Eg = 1.516 - enlevels_el[2] - enlevels_lh[2]
print(Eg)
