import math
import random
from ROOT import gROOT, gRandom, gSystem, TCanvas, TFile, TH1F, TH2F

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

class ParticlePair():
    # ParticlePair is a class containing 
    # a pair of particles and all their properties, 
    # where the first one in a pair is a trigger particle, 
    # while the second one is an associated particle
    def __init__(self, particle1, particle2):
        # A pair has:
        # - a pseudorapidity difference deta
        self.deta = particle1.eta - particle2.eta
        # - an azimuthal angle difference dphi
        self.dphi = particle1.dphi - particle2.dphi


nev = 100
npart = 100
dataset = []
for iev in range(0,nev):
    event = []
    for ii in range(0,npart):
        pt = random.uniform(0.5, 1.0)
        eta = random.uniform(-0.8, 0.8)
        phi = random.uniform(0, 2*math.pi)
        event.append(Particle(pt, eta, phi))
    dataset.append(event)

ievent = 0
hyield = TH2F('hyield', 'Associated yield per trigger particle', 32, -1.6, 1.6, 32, -0.5*math.pi, 1.5*math.pi)
cyield = TCanvas('cyield', 'Yield canvas', 200, 10, 700, 500)
for event in dataset:
    print(ievent)
    for trig in event:
        for assoc in event:
            if trig == assoc:
                continue
            deta = trig.eta - assoc.eta
            dphi = trig.phi - assoc.phi
            if dphi < -0.5*math.pi:
                dphi += 2*math.pi
            if dphi > 1.5*math.pi:
                dphi -= 2*math.pi
            #print(str(deta) + ", " + str(dphi))
            hyield.Fill(deta, dphi)
    ievent += 1

hyield.Draw("colz")
cyield.Modified()
cyield.Update()
cyield.Print()
