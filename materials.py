# Defines material properties, includes the library of materials

class Material:
  'Represents a material definition'
  
  def __init__(self,name,epsilon,mu,conductivity):
    self.name = name
    self.epsilon = epsilon
    self.mu = mu
    self.conductivity = conductivity

class Collection:
  'Collection of possible materials'
  
  def __init__(self):
    self.dict = {}
    
  def addmat(self, material):
    self.dict[material.name] = material

  def lookup(self, name):
    return(self.dict[name])
    
library = Collection()
library.addmat(Material('vacuum',1,1,0))
