#!/usr/bin/env python3

# ---------------------------
# projects/netflix/Netflix.py
# Copyright (C) 2016
# Glenn P. Downing
# ---------------------------

#--------
#imports
#--------

import requests, os, pickle

customer_average_rating = 'http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-customer_average.pickle'
r = requests.get(customer_average_rating).content
pickle_dic = pickle.load(r)

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


#when movie id is read in
#need to check it's data
#i.e. year it was made
#average rating for it
#when user id is read in
#need to check it's data
#user's average rating overall
#user's average for a decade
#user's average rating for a year
