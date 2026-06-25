/*
 * Test f2c is the inverse of c2f.
 */

#include <assert.h>
#include <math.h>
#include <stdio.h>

#include "conversion.c"

#define EPSILON 0.001

int main() {
  double values[] = {0.0, 7.5, 23.0};
  for (int i = 0; i < 3; i++) {
    double celsius = f2c(values[i]);
    double fahrenheit = f2c(celsius);
    assert(fabs(fahrenheit - values[i]) < EPSILON);
  }
}
