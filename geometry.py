class Set:
  'A set, like in math'
  
  def __init__(self,dimension):
    self.dimension = dimension

class Object(Set):
  'Material objects, like with material properties'
  
  def __init__(self,dimension):
    Set.__init__(self,dimension)

class Rectangle(Object):
  '3D Rectangular prism, or 2D rectangle'
  
  def __init__(self,xmin,xmax,ymin,ymax,zmin,zmax):
    
    if xmin == xmax or ymin == ymax or zmin == zmax:
      dimension = 2
    else:
      dimension = 3
    Object.__init__(self,dimension)
    
    self.xmin = xmin
    self.xmax = xmax
    self.ymin = ymin
    self.ymax = ymax
    self.zmin = zmin
    self.zmax = zmax

class Domain(Rectangle):
  'The whole domain, within which all the objects exist (except possibly PML boundaries)'
  
  def __init__(self,xmin,xmax,ymin,ymax,zmin,zmax):
    Rectangle.__init__(self,xmin,xmax,ymin,ymax,zmin,zmax)

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
