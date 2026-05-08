"""
Demo for `pytest --last-failed`.

Here we implement functions for converting between Celsius and Fahrenheit and provide
some basic unit tests for verifying that they work as expected. However, the
implementations and tests contain three errors.

Exercises:

1. Run `pytest --verbose demos/test_temperature_conversion.py` to see the failures.

2. Track down each issue, running `pytest --verbose --last-failed` each time you make a
   fix. You should see that fewer tests are run each time.
"""
import numpy
import pytest

# --- Function definitions

def c2f(celsius):
    """Convert a temperature from degrees Celsius to degrees Fahrenheit."""
    return 9 * celsius / 5 + 32.0


def f2c(fahrenheit):
    """Convert a temperature from degrees Fahrenheit to degrees Celsius."""
    return (fahrenheit - 32.0) * 5 / 8

# --- Unit tests

@pytest.mark.parametrize("celsius,expected", [(0.0, 32.0), (-40.0, -40.0)])
def test_c2f(celsius, expected):
    """Test for the Celsius-to-Fahrenheit conversion."""
    fahrenheit = c2f(celsius)
    numpy.testing.assert_almost_equal(fahrenheit, expected)


@pytest.mark.parametrize("fahrenheit,expected", [(32.0, 1.0), (-40.0, -40.0)])
def test_f2c(fahrenheit, expected):
    """Test for the Fahrenheit-to-Celsius conversion."""
    celsius = f2c(fahrenheit)
    numpy.testing.assert_almost_equal(celsius, expected)


@pytest.mark.parametrize("expected", [0.0, 7.5, 23.0])
def test_inverse1(expected):
    """Test that f2c is the inverse of c2f."""
    fahrenheit = c2f(expected)
    celsius = f2c(fahrenheit)
    numpy.testing.assert_almost_equal(celsius, expected)


@pytest.mark.parametrize("expected", [0.0, 7.5, 23.0])
def test_inverse2(expected):
    """Test that c2f is the inverse of f2c."""
    celsius = f2c(expected)
    fahrenheit = f2c(celsius)
    numpy.testing.assert_almost_equal(fahrenheit, expected)
