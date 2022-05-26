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
      picture += "*" * self.width + "\n"
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
    super().__init__(side, side)
  
  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)
    # self.side = side
  
  def set_width(self,side):
    super().set_width(side)
    super().set_height(side)
    # self.side = side

  def set_height(self, side):
    super().set_height(side)
    super().set_width(side)
    # self.side = side

  def __str__(self):
    string = ""
    string = "Square(side=" + str(self.height) + ")"
    return string

rect = Rectangle(5, 10)
print(rect.get_area())
rect.set_width(3)
print(rect.get_perimeter())
print(rect)
rect.set_height(7)
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

sq.set_width(2)
print(sq)
print(sq.get_picture())

sq.set_height(8)
print(sq)
print(sq.get_picture())
