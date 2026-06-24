/*
 * Test conversion from Celsius to Fahrenheit.
 */

#include <assert.h>
#include <math.h>
#include <stdio.h>

#include "conversion.c"

#define EPSILON 0.001

int main() {
  assert(fabs(c2f(0.0) - 32.0) < EPSILON);
  assert(fabs(c2f(-40.0) - (-40.0)) < EPSILON);
}
