cmake_minimum_required(VERSION 3.10)
project(CTestRerunFailed)

# Build the library
add_library(conversion conversion.c)

# Add the test suite, linking to the library
add_executable(test_c2f test_c2f.c)
target_link_libraries(test_c2f conversion)
add_executable(test_f2c test_f2c.c)
target_link_libraries(test_f2c conversion)
add_executable(test_c2f_inverse test_c2f_inverse.c)
target_link_libraries(test_c2f_inverse conversion)
add_executable(test_f2c_inverse test_f2c_inverse.c)
target_link_libraries(test_f2c_inverse conversion)

# Enable testing
enable_testing()

# Add tests
add_test(NAME test_c2f COMMAND test_c2f)
add_test(NAME test_f2c COMMAND test_f2c)
add_test(NAME test_c2f_inverse COMMAND test_c2f_inverse)
add_test(NAME test_f2c_inverse COMMAND test_f2c_inverse)
