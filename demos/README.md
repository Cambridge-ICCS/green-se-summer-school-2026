# Demos

There are several demos that we encounter in the Green Software Engineering
Practices course. Some of them involve navigating to a website and others
involve code found in this subdirectory.

## 1. CodeCarbon

1. Take a look at [code_carbon.py](code_carbon.py).
2. Replace the TODO note with some code to execute.
3. Run the Python script to find out the associated emissions.

> [!HINT]
> Running with `python3 demos/code_carbon.py 2>codecarbon.log` will print
> CodeCarbon's logging output to a separate file so that you can more clearly
> see any print statements.

4. Inspect the log file and the `emissions.csv` file that is produced.
5. Launch the CodeCarbon dashboard to explore the results visually:
   ```sh
   carbonboard --filepath="emissions.csv" --port=3333
   ```
   Then open [http://localhost:3333](http://localhost:3333) in your browser. The
   dashboard shows carbon equivalents (e.g. km driven, TV hours) and a global
   map of energy mix by region.

## 2. GreenAlgorithms calculator

1. Navigate to the
   [GreenAlgorithms calculator](https://calculator.green-algorithms.org/)
2. Open this [paper](https://gmd.copernicus.org/articles/17/3081/2024/)
   comparing the energy usage of different models participating in CMIP.
3. Plug in numbers for different models

## 3. Climate-Aware Task Scheduler

1. Install the [CATS](https://github.com/GreenScheduler/cats) Python package.
2. Query for the optimal time to run a 30 minute job in your postcode using the
   `--duration` and `--location` flags.
3. Plot the forecast using the `--plot` flag.
4. What happens if you try a long job, e.g., 2800 mins?

## 4a. Pytest

1. Take a look at [pytest_last_failed.py](pytest_last_failed.py).
2. Run `pytest --verbose pytest_last_failed.py` and inspect the failures.
3. Track down each issue, running `pytest --verbose --last-failed` each time you
   make a fix. You should see that fewer tests are run each time.

## 4b. CTest

Navigate to [ctest_rerun_failed](ctest_rerun_failed) and read the README there.

## 5. AI footprint calculator

1. Navigate to https://www.climatealigned.co/tools/ai-footprint-calculator
2. Play around with the different options.
3. Get a sense for your current footprint and how it would change with different
   levels of AI usage.
