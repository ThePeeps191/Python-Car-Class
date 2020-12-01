# AN EXAMPLE OF A PYTHON CLASS

# Define The Class
class Car:
  # Initialize
  def __init__(self, color, number_of_wheels, owner):
    self.color = color
    self.wheels = number_of_wheels
    self.owner = owner
  # Callable Functions
  # Always Have The Parameter "self"
  def car_color(self):
    return self.color
  
  def car_wheels(self):
    return self.wheels
  
  def car_owner(self):
    return self.owner

# Make An Object In The Class
car = Car("red", 4, "The Peeps191")

print(f"car is {car.car_color()}")

print(f"car has {car.car_wheels()} wheels")

print(f"{car.car_owner()} owns the car")
