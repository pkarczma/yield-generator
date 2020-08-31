import random

class Particle():
    # Particle is a generic particle class
    # containing all the parameters of itself
    def __init__(self, pt=0., eta=0., phi=0.):
        # Each particle has:
        # - a transverse momentum pt
        self.pt = pt
        # - a pseudorapidity eta
        self.eta = eta
        # - an azimuthal angle phi
        self.phi = phi
    # Method for skipping particles due to efficiency
    def skip(self, eff=1.0):
        # Generate random value in (0, 1) range
        rand = random.uniform(0, 1)
        # Check if efficiency is lower than generated value
        skip = False
        if eff < rand:
            skip = True
        # Return the result
        return skip
