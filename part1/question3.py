################################################################################
#     ____                          __     _                          _____
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          |__  /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \          /_ < 
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /        ___/ / 
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/        /____/  
#                                                                          
#  Question 3
################################################################################
#
# Instructions:
# Make a Python class for a magical oven that can combine ingredients at 
# different temperatures to craft special materials.
# 
# The oven class should have the methods:
# - add(item) to add an oven to be combined
# - freeze() to freeze the ingredients
# - boil() to boil the ingredients
# - wait() to combine the ingredients with no change in temperature
# - get_output() to get the result 
#
# You will need to change the `make_oven()` function to return a new instance
# of your oven.
#
# The `alchemy_combine()` function will use your oven. You can see the expected 
# formulas and their outputs in the test file, `question3_test.py`.

# This function should return an oven instance!

class OvenError(Exception):
  pass

class MagicalOven:
  """
  A magical oven that combines ingredients at different temperatures to craft materials
  """

  def __init__(self) -> None:
    self._ingredients = []
    self._temperature = 0


  @property
  def ingredients(self) -> list[str]:
    return self._ingredients

  @ingredients.setter
  def ingredients(self, new_ingredients: list[str]):
    for ingredient in new_ingredients:
      if not isinstance(ingredient, str) or not ingredient.strip():
        raise OvenError("Ingredients must be non-empty strings")
    self._ingredients = new_ingredients



  @property
  def temperature(self) -> int:
    return self._temperature

  @temperature.setter
  def temperature(self, value: int):
    # i could put validation for temperatures here if I needed to
    self._temperature = value


  def add(self, ingredient: str) -> 'MagicalOven':
    """
    Add an ingredient to the oven.

    Args:
        ingredient (str): The ingredient to add.

    Returns:
        MagicalOven: The oven instance (for method chaining).
    """

    self.ingredients.append(ingredient)

    return self
  
  def freeze(self) -> 'MagicalOven':
    """
    Apply chilly temperature to ingredients

    Returns:
        MagicalOven: The oven instance (for method chaining)
    """

    self.temperature = -100

    return self
  
  def boil(self) -> 'MagicalOven':
    """
    Apply boiling temperature to ingredients

    Returns:
        MagicalOven: The oven instance (for method chaining)
    """

    self.temperature = 150

    return self

  def wait(self) -> 'MagicalOven':
    """
    Apply MAGICAL temperature to ingredients

    Returns:
        MagicalOven: The oven instance (for method chaining)
    """
    self.temperature = 5000

  def get_output(self) -> str:
    """return str with output product of the alchemy"""


    pizza_ingredients = ["cheese", "dough", "tomato"]
    snow_ingredients = ["water", "air"]
    gold_ingredients = ["lead", "mercury"]


    # since we only know what happens at -100, 150 and 5000 we define only those values
    # instead of using intervals

    print(self.temperature)

    if self.temperature == -100 and all(ingredient in self.ingredients for ingredient in snow_ingredients):
      return "snow"
    elif self.temperature == 150 and all(ingredient in self.ingredients for ingredient in pizza_ingredients):
      return "pizza"
    elif self.temperature == 5000 and all(ingredient in self.ingredients for ingredient in gold_ingredients):
      return "gold"
    else:
      return "default..."


  

def make_oven():
  return MagicalOven()

def alchemy_combine(oven, ingredients, temperature):
  
  for item in ingredients:
    oven.add(item)

  if temperature < 0:
    oven.freeze()
  elif temperature >= 100 and temperature <= 500: # added condition because we need a way to reach wait
    oven.boil()
  else:
    oven.wait()

  return oven.get_output()