def sort(width: float, height: float, length: float, mass: float) -> str:
  """
  Desc::
    Sorts a package into one of three catagories:
    1. STANDARD if the package is not bulky nor heavy
    2. SPECIAL if the package either heavy or bulky
    3. REJECTED is the pacakge is both heavy and bulky

    Prints the string value of the correct category.

    Assume all packages are rectangular.
  
  Args::
    width: float. The width of the package in cm.
    height: float. The height of the package in cm.
    length: float. The length of the package in cm.
    mass: float. The mass of the package in kg.

  Return:: 
    str. The category type. One of either STANDARD, SPECIAL, or REJECTED.
  """
  
  is_bulky = False
  is_heavy = False
  is_large_volume = False
  has_long_dim = False
  
  volume: float = width * height * length

  # Check if volume >= 1,000,000 cm cubed.
  if (volume >= 1_000_000):
    is_large_volume = True

  # Check if one of the dims >= 150 cm.
  if (width >= 150 or height >= 150 or length >= 150):
    has_long_dim = True

  if (is_large_volume or has_long_dim):
    is_bulky = True

  if (mass >= 20):
    is_heavy = True

  # Assume STANDARD. Check conditions to see if it is not.
  category = "STANDARD"
  if (is_bulky and is_heavy): # REJECTED must be checked before SPECIAL.
    category = "REJECTED"
  elif (is_bulky or is_heavy):
    category = "SPECIAL"

  return category
  
