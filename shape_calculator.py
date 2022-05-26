class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    area = self.width * self.height
    return area

  def get_perimeter(self):
    perimeter = (2 * self.width + 2 * self.height)
    return perimeter

  def get_diagonal(self):
    diagonal = ((self.width ** 2 + self.height ** 2) ** .5)
    return diagonal

  def get_picture(self):
    picture = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    j = 0
    while j < self.height:
      picture = '*' * self.width + "\n"
      # i = 0
      # while i < self.width:
      #   i += 1
      j += 1
    return picture

  # def get_amount_inside(self, shape):
  #   nb = ""
    
  #   return nb

  def __str__(self):
    string = ""
    string = "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    return string
# get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.

class Square(Rectangle):
  def __init__(self, side):
    self.height = side
    self.width = side
    self.side = side
  
  def set_side(self, side):
    self.side = side
  
  def __str__(self):
    string = ""
    string = "Square(side=" + str(self.side) + ")"
    return string

