# Geometry related functions and definitions

import materials

class Set:
  'A set, like in math'
  
  def __init__(self,dimension):
    self.dimension = dimension
    
class Point(Set):
  'A single point in space'
  
  def __init__(self,position):
    Set.__init__(self,0)
    self.position = position
    
class Object(Set):
  'Material objects, like with material properties'
  
  def __init__(self,dimension,material):
    Set.__init__(self,dimension)
    self.material = material


    
class Rectangle(Object):
  '3D Rectangular prism, or 2D rectangle'
  
  def __init__(self,xmin,xmax,ymin,ymax,zmin,zmax,material):
    
    if xmin == xmax or ymin == ymax or zmin == zmax:
      dimension = 2
    else:
      dimension = 3
    Object.__init__(self,dimension,material)
    
    self.xmin = xmin
    self.xmax = xmax
    self.ymin = ymin
    self.ymax = ymax
    self.zmin = zmin
    self.zmax = zmax

class Domain(Rectangle):
  'The whole domain, within which all the objects exist (except possibly PML boundaries)'
  
  def __init__(self,xmin,xmax,ymin,ymax,zmin,zmax):
    vacuum = materials.library.lookup('vacuum')
    Rectangle.__init__(self,xmin,xmax,ymin,ymax,zmin,zmax,vacuum)

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
    
    self.domain = Domain(xmin,xmax,ymin,ymax,zmin,zmax)
    self.objects = []
    self.materials = []
    self.mesh = None
