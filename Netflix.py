#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

#--------
#netflix_eval
#--------

def netflix_eval() :


def netflix_read() :


def netflix_print(w, v) :
    w.write(str(v) + "\n")

def netflix_rmse() :


def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """

    for s in r :
        #if s is movie
        #just print it
        #if s is customer id
        #perform eval on it
        if ":" in s :
            netflix_print(w, v)

        i = netflix_read(s)
        v = netflix_eval(i)
        netflix_print(w, v)
