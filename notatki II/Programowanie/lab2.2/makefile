CFILES   = $(wildcard *.c)
CPPFILES = $(wildcard *.cpp)
OBJFILES = $(CFILES:.c=.o) $(CPPFILES:.cpp=.o)
OUT      = main

LOADLIBES = -lm
CXXFLAGS = -Wall -O2 -g

CC = g++

$(OUT): $(OBJFILES)

run: $(OUT)
	./$(OUT)

.PHONY: clean
clean:
	rm -f $(OBJFILES) $(OUT)
