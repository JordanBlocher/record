cdef extern int run(char *filename) #nogil
cdef extern void stop() #nogil

def capture(filename):
        run(filename)
    #with nogil:
    #   run(filename)

def capture_stop():
        stop()
    #with nogil:
        #stop()
