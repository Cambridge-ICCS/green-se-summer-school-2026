"""
CodeCarbon demo.

Here we demonstrate how to track carbon emissions of Python code using CodeCarbon.

Exercises:

1. Replace the TODO note with some code to execute.

2. Run the Python script to find out the associated emissions.

Hint: Running with `python3 demos/code_carbon.py 2>codecarbon.log` will print
      CodeCarbon's logging output to a separate file so that you can more clearly see
      any print statements.

3. Inspect the log file and the `emissions.csv` file that is produced.

4. Launch the CodeCarbon dashboard to explore the results visually:

       carbonboard --filepath="emissions.csv" --port=3333

   Then open http://localhost:3333 in your browser. The dashboard shows carbon
   equivalents (e.g. km driven, TV hours) and a global map of energy mix by region.
"""
import random
import numpy as np
from codecarbon import EmissionsTracker

SIZE = 10_000_000
list1 = [random.random() for _ in range(SIZE)]
list2 = [random.random() for _ in range(SIZE)]
arr1 = np.array(list1)
arr2 = np.array(list2)

# Tracking Pure Python dot product
tracker = EmissionsTracker(log_level="error")
tracker.start()
sum(a * b for a, b in zip(list1, list2))
emissions_py = tracker.stop()
print(f"Pure Python emissions: {emissions_py:.2e} kg CO₂")

# Tracking NumPy dot product
tracker = EmissionsTracker(log_level="error")
tracker.start()
np.dot(arr1, arr2)
emissions_np = tracker.stop()
print(f"NumPy emissions:       {emissions_np:.2e} kg CO₂")

print(f"Ratio: {emissions_py / emissions_np:.0f}x more emissions for pure Python")
