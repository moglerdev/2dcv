# Makefile zum Bauen von sobel_demo

CXX          := c++
EIGEN_INC    := /usr/include/eigen3
PYBIND11_INC := $(shell python3 -m pybind11 --includes)
PYEXT        := $(shell python3-config --extension-suffix)
CXXFLAGS     := -O3 -Wall -shared -std=c++11 -fPIC \
                -I$(EIGEN_INC) $(PYBIND11_INC)

SRC    := sobel_demo.cpp
TARGET := sobel_demo$(PYEXT)

.PHONY: all clean

all: $(TARGET)

$(TARGET): $(SRC)
	$(CXX) $(CXXFLAGS) $< -o $@

clean:
	rm -f $(TARGET)
