import math
import random
from ROOT import gROOT, gRandom, gSystem, TCanvas, TFile, TH1F, TH2F
from Particle import Particle
from ParticlePair import ParticlePair

# Generator settings
nev = 100
npart = 100

# Generate dataset
dataset = []
for iev in range(0,nev):
    event = []
    for ii in range(0,npart):
        pt = random.uniform(0.5, 1.0)
        eta = random.uniform(-0.8, 0.8)
        phi = random.uniform(0, 2*math.pi)
        event.append(Particle(pt, eta, phi))
    dataset.append(event)

# Prepare variables
ievent = 0
pi = math.pi
hyield = TH2F('hyield', 'Associated yield per trigger particle', 32, -1.6, 1.6, 32, -0.5*math.pi, 1.5*math.pi)
cyield = TCanvas('cyield', 'Yield canvas', 200, 10, 700, 500)

# Process dataset
for event in dataset:
    print(ievent)
    for trig in event:
        for assoc in event:
            if trig == assoc:
                continue
            pair = ParticlePair(trig, assoc)
            deta = pair.deta
            dphi = pair.dphi
            if dphi < -0.5*pi:
                dphi += 2*pi
            if dphi > 1.5*pi:
                dphi -= 2*pi
            #print(str(deta) + ", " + str(dphi))
            hyield.Fill(deta, dphi)
    ievent += 1

# Plotting and saving
hyield.Draw("colz")
cyield.Modified()
cyield.Update()
cyield.Print()
