class Material:
  'Represents a material definition'
  
  def __init__(self,name,epsilon,mu,conductivity):
    self.name = name
    self.epsilon = epsilon
    self.mu = mu
    self.conductivity = conductivity

class MaterialLibrary:
  'Collection of possible materials'
  
  def __init__(self):
    self.library = {}
    
  def addmat(self, material):
    self.library[material.name] = material
    
materials = MaterialLibrary()
materials.addmat(Material('vacuum',1,1,0))
