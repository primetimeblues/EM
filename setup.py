# Simulation parameters other than the geometry

import geometry

class Simulation:
  'Collection of simulation parameters, geometric objects, etc.'
  
  def __init__(self, fLower,fUpper):
    self.flower = fLower # lower frequency of the simulation
    self.fupper = fUpper # upper frequency of the simulation
    
    c = 1 # I'll figure out units later
    if fLower == 0:
      wlMax = 4/fUpper
    else:
      wlMax = 1/fLower
    qwl = wlMax/4 # quarter wavelength
    xmin,ymin,zmin = -qwl,-qwl,-qwl
    xmax,ymax,zmax = qwl,qwl,qwl
    
    self.domain = geometry.Domain(xmin,xmax,ymin,ymax,zmin,zmax)
    self.objects = []
    self.materials = []
    self.mesh = None
