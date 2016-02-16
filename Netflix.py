#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

#--------
#netflix_eval
#--------

def netflix_eval(i) :
    return i

def netflix_read(s) :
    return int(s)

def netflix_print(w, v) :
    w.write(str(v) + "\n")

#def netflix_rmse() :


def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """

    for s in r :
        if ":" in s :
            w.write(s)
        else :
            i = netflix_read(s)
            v = netflix_eval(i)
            netflix_print(w, v)
