cmake_minimum_required(VERSION 3.12)
project(SobelDemo LANGUAGES CXX)

# --- Find Python and Pybind11 ---
# Use find_package which is more robust
find_package(Python COMPONENTS Interpreter Development REQUIRED)

# Get pybind11 cmake dir (needed when installed via pip)
execute_process(
  COMMAND ${Python_EXECUTABLE} -m pybind11 --cmakedir
  OUTPUT_VARIABLE pybind11_CMAKE_DIR
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

# Add pybind11's cmake directory to the search paths
list(APPEND CMAKE_PREFIX_PATH ${pybind11_CMAKE_DIR})

find_package(pybind11 CONFIG REQUIRED)

# --- Add Eigen ---
# Assuming Eigen headers are in the 'eigen-3.4.0' subdirectory relative to this CMakeLists.txt
include_directories(eigen-3.4.0)
message(STATUS "Added eigen-3.4.0 to include directories.")

# --- Create the Python module ---
# pybind11_add_module(<name> [SHARED|MODULE|STATIC] [EXCLUDE_FROM_ALL]
#                    [NO_EXTRAS] source1 [source2 ...])
pybind11_add_module(sobel_demo SHARED sobel_demo.cpp)

# --- Link dependencies ---
# pybind11 headers are handled by pybind11_add_module
# Eigen is header-only, so only include directories are needed (done above)
# Link against Python
target_link_libraries(sobel_demo PRIVATE Python::Module)

# --- Optional: Improve compiler flags ---
# Add C++11 standard requirement
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add optimization flags for Release builds (similar to -O3)
set(CMAKE_CXX_FLAGS_RELEASE "${CMAKE_CXX_FLAGS_RELEASE} /O2") # MSVC equivalent of -O3 is often /O2
set(CMAKE_CXX_FLAGS_RELWITHDEBINFO "${CMAKE_CXX_FLAGS_RELWITHDEBINFO} /O2 /Zi")

# Add warning flags (similar to -Wall)
if(MSVC)
    target_compile_options(sobel_demo PRIVATE /W4) # /W4 is roughly equivalent to -Wall
else()
    # Add flags for GCC/Clang if needed
    target_compile_options(sobel_demo PRIVATE -Wall -Wextra)
endif()

# Print Python paths for debugging
message(STATUS "Python_INCLUDE_DIRS: ${Python_INCLUDE_DIRS}")
message(STATUS "Python_LIBRARIES: ${Python_LIBRARIES}")
message(STATUS "pybind11_INCLUDE_DIRS: ${pybind11_INCLUDE_DIRS}")

