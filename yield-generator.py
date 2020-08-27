import math
import random
from ROOT import gROOT, gRandom, gSystem, TCanvas, TFile, TH1F, TH2F, TLatex, TString
from Particle import Particle
from ParticlePair import ParticlePair
from EventPool import EventPool

# Generator settings
nev = 1000
npart = 100
# Generator settings for event mixing
targettracksize = 1000

# Generate dataset
dataset = []
for iev in range(0,nev):
    event = []
    npart = random.randint(80, 120)
    print(str(npart))
    for ii in range(0,npart):
        pt = random.uniform(0.5, 1.0)
        eta = random.uniform(-0.8, 0.8)
        phi = random.uniform(0, 2*math.pi)
        event.append(Particle(pt, eta, phi))
    dataset.append(event)

# Prepare variables
ievent = 0
ntrigger = 0
pi = math.pi
ep = EventPool(targettracksize)
wdphi = pi / 16
wdeta = 0.1
hsame = TH2F('hsame', 'Same events histogram', 32, -1.6, 1.6, 32, -0.5*pi, 1.5*pi)
hmixed = TH2F('hmixed', 'Mixed events histogram', 32, -1.6, 1.6, 32, -0.5*pi, 1.5*pi)
hyield = TH2F('hyield', 'Associated yield per trigger particle', 32, -1.6, 1.6, 32, -0.5*pi, 1.5*pi)
csame = TCanvas('csame', 'Same events canvas', 200, 10, 700, 500)
cmixed = TCanvas('cmixed', 'Mixed events canvas', 200, 10, 700, 500)
cyield = TCanvas('cyield', 'Yield canvas', 200, 10, 700, 500)

# Process dataset
for event in dataset:
    print(ievent)
    for trig in event:
        ntrigger += 1
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
            hsame.Fill(deta, dphi)
    if ep.is_ready():
        print("Event pool ready");
        for mixtrig in ep.trackpool():
            for mixassoc in ep.trackpool():
                if mixtrig == mixassoc:
                    continue
                mixpair = ParticlePair(mixtrig, mixassoc)
                mixdeta = mixpair.deta
                mixdphi = mixpair.dphi
                if mixdphi < -0.5*pi:
                    mixdphi += 2*pi
                if mixdphi > 1.5*pi:
                    mixdphi -= 2*pi
                hmixed.Fill(mixdeta, mixdphi)
    ep.add(event)
    ievent += 1

# Calculate yield factors
print("ntrigger: " + str(ntrigger))
alpha = 1. / (wdphi * ntrigger)
print("alpha: " + str(alpha))
f = 1. - 1. / (2. * 0.8) * wdeta / 2.
print("f: " + str(f))
xmin = hmixed.GetXaxis().FindBin(-wdeta+0.001)
xmax = hmixed.GetXaxis().FindBin(wdeta-0.001)
ymin = hmixed.GetYaxis().FindBin(-wdphi+0.001)
ymax = hmixed.GetYaxis().FindBin(wdphi-0.001)
mixedFactor = hmixed.Integral(xmin, xmax, ymin, ymax)
print("mixedFactor: " + str(mixedFactor))
gamma = 4. * f / mixedFactor
print("gamma: " + str(gamma))

# Calculate final yield
#hyield = hsame.Clone()
hyield.Add(hsame)
hyield.Divide(hmixed)
print("alpha / gamma: " + str(alpha / gamma))
hyield.Scale(alpha / gamma)

# Plotting and saving
csame.cd()
hsame.Draw("colz")
csame.Modified()
csame.Update()
csame.Print()

cmixed.cd()
hmixed.Draw("colz")
cmixed.Modified()
cmixed.Update()
cmixed.Print()

cyield.cd()
hyield.Draw("colz")
integral = hyield.Integral() / (32.*32.)
print(str(integral))
panelIntegral = TLatex(-0.5, 1.5, str(integral));
panelIntegral.Draw()
cyield.Modified()
cyield.Update()
cyield.Print()
