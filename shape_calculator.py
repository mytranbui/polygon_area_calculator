import math

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    picture = ""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    j = 0
    while j < self.height:
      picture += "*" * self.width + "\n"
      j += 1
    return picture

  def get_amount_inside(self, shape):
    return math.floor(self.get_area() / shape.get_area())

  def __str__(self):
    return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"

class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  
  def set_side(self, side):
    self.set_width(side)
    self.set_height(side)
  
  def set_width(self,side):
    super().set_width(side)
    super().set_height(side)

  def set_height(self, side):
    super().set_height(side)
    super().set_width(side)

  def __str__(self):
    return "Square(side=" + str(self.height) + ")"

# rect = Rectangle(5, 10)
# print(rect.get_area())
# rect.set_width(3)
# print(rect.get_perimeter())
# print(rect)
# rect.set_height(7)
# print(rect)
# print(rect.get_picture())

# sq = Square(9)
# print(sq.get_area())
# sq.set_side(4)
# print(sq.get_diagonal())
# print(sq)
# print(sq.get_picture())

# sq.set_width(2)
# print(sq)
# print(sq.get_picture())

# sq.set_height(8)
# print(sq)
# print(sq.get_picture())