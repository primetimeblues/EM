class Collection:
  'Collection of geometric objects, and related methods'
  
  def __init__(self):
    self.objects = []

class Set:
  'A set, like in math'
  
  def __init__(self,dimension):
    self.dimension = dimension
    
class Object(Set):
  'Material objects, like with material properties'
  
  def __init__(self,dimension):
    Set.__init__(self,dimension)
