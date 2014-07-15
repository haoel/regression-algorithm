PYTHON_LIB=/usr/include/python2.6

all: cylowess.so

cylowess.c: cylowess.pyx
	cython cylowess.pyx

cylowess.o:cylowess.c
	gcc -c -fPIC -I${PYTHON_LIB}  cylowess.c	

cylowess.so:cylowess.o
	gcc -shared -o cylowess.so cylowess.o


.PHONY: clean

clean:
	rm -f cylowess.c *.o *.so
