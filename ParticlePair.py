import math

class ParticlePair():
    # ParticlePair is a class containing 
    # a pair of particles and all their properties, 
    # where the first one in a pair is a trigger particle, 
    # while the second one is an associated particle
    def __init__(self, particle1, particle2):
        # A pair has:
        # - a pseudorapidity difference deta
        self.deta = particle1.eta - particle2.eta
        # - an azimuthal angle difference 0.5*pi < dphi < 1.5*pi
        self.dphi = particle1.phi - particle2.phi
        if self.dphi < -0.5*math.pi:
            self.dphi += 2*math.pi
        if self.dphi > 1.5*math.pi:
            self.dphi -= 2*math.pi

