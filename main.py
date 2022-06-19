import numpy as np
import random
from utils import add_class

output_el = Element('output')

arr = np.array([22,15,14,34,2,6])

# pyscript.write('output', f"{arr}")
output_el.innerHTML = f"{arr}"

def shuffle_array(*args):
  shuffled = sorted(arr, key=lambda k: random.random())

  add_class(output_el, 'text-blue-500')

  # pyscript.write('output', f"{shuffled}")
  output_el.innerHTML = shuffled