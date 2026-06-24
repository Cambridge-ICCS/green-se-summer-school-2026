/*
 * Test conversion from Fahrenheit to Celsius.
 */

#include <assert.h>
#include <math.h>
#include <stdio.h>

#include "conversion.c"

#define EPSILON 0.001

int main() {
  assert(fabs(f2c(32.0) - 1.0) < EPSILON);
  assert(fabs(f2c(-40.0) - (-40.0)) < EPSILON);
}
