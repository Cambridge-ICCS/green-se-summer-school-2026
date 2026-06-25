/*
 * Library of functions for converting between Celsius and Fahrenheit
 */

/*
 * Convert Celsius to Fahrenheit
 */
double c2f(double celsius) { return 9.0 * celsius / 5.0 + 32.0; }

/*
 * Convert Fahrenheit to Celsius
 */
double f2c(double fahrenheit) { return (fahrenheit - 32.0) * 5.0 / 8.0; }
