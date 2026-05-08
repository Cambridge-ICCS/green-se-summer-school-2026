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
"""
from codecarbon import EmissionsTracker

tracker = EmissionsTracker()
tracker.start()

# TODO: Your code here!

emissions = tracker.stop()

print(f"Emissions: {emissions} kg CO₂")
