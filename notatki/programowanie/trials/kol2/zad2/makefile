CFILES   = $(wildcard *.c)
CPPFILES = $(wildcard *.cpp)
OBJFILES = $(CFILES:.c=.o) $(CPPFILES:.cpp=.o)
OUT      = main

CC = g++

$(OUT): $(OBJFILES)

run: $(OUT)
	/bin/bash -c "time ./$(OUT)"

.PHONY: clean
clean:
	rm -f $(OBJFILES) $(OUT)
