class Material:
  'Represents a material definition'
  
  def __init__(self,name,epsilon,mu,conductivity):
    self.name = name
    self.epsilon = epsilon
    self.mu = mu
    self.conductivity = conductivity
