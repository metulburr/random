#makefile template

CC=g++
CFLAGS=-c -Wall
LDFLAGS=
SOURCES=main.cpp People.cpp Birthday.cpp 
OBJECTS=$(SOURCES:.cpp=.o)
EXECUTABLE=main
BINDIR=/usr/bin

all: $(SOURCES) $(EXECUTABLE)
	
$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

.cpp.o:
	$(CC) $(CFLAGS) $< -o $@

clean:
	rm *.o $(EXECUTABLE)

install:
	install -s $(EXECUTABLE) $(BINDIR)
uninstall:
	rm $(BINDIR)/$(EXECUTABLE)
