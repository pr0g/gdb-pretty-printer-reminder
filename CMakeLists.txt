cmake_minimum_required(VERSION 3.28)
project(pretty-printers-test LANGUAGES CXX)
add_executable(${PROJECT_NAME})
target_sources(${PROJECT_NAME} PRIVATE main.cpp)
target_compile_features(${PROJECT_NAME} PRIVATE cxx_std_23)

configure_file(${CMAKE_SOURCE_DIR}/my_gdb_autoload.py.in
               ${CMAKE_CURRENT_BINARY_DIR}/my_gdb_autoload.py @ONLY)

file(
  GENERATE
  OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/$<CONFIG>/${PROJECT_NAME}-gdb.py
  INPUT ${CMAKE_CURRENT_BINARY_DIR}/my_gdb_autoload.py)
