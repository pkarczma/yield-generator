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
