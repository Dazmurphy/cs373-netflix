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

from math      import sqrt

from numpy     import mean, sqrt, square, subtract

#customer_average_rating = 'http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-customer_average.pickle'
#movie_average_rating = 'http://www.cs.utexas.edu/users/downing/netflix-caches/kdg445_movie_avgs.pickle'
#actual_ratings = 'http://www.cs.utexas.edu/users/downing/netflix-caches/kdg445_true_ratings.pickle'

#r = requests.get(movie_average_rating).content
#pickle_dic = pickle.loads(r)

#s = requests.get(actual_ratings).content
#real_ratings = pickle.loads(s)

f = open('kh549-customer_average.pickle', 'rb')
customer_av_unpickled = pickle.load(f)

g = open('kdg445_true_ratings.pickle', 'rb')
true_ratings = pickle.load(g)
#training_data_url = 'http://www.cs.utexas.edu/users/downing/netflix-caches/'

prediction_list = []
actual_ratings_list = []

customer_id = 0
movie_id = 0

#--------
#netflix_eval
#--------

def netflix_eval(i) :
    return customer_av_unpickled[i]

def netflix_read(s) :
    return int(s)


def netflix_print(w, v) :
    w.write(str(v) + "\n")

def netflix_rmse(a, p) :
    v = sum(map(lambda x, y : (x - y) ** 2, a, p))

    return sqrt(v / len(a))


def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """

    i = 0

    for s in r :

        if ":" in s :
            w.write(s)

            #remove newline character and colon
            s = s.strip()
            s = s.strip(":")

            movie_id = int(s)

        else :
            customer_id = netflix_read(s)
            predicted_rating = netflix_eval(customer_id)

            prediction_list.append(predicted_rating)
            actual_ratings_list.append(true_ratings[movie_id][customer_id])

            netflix_print(w, predicted_rating)

    w.write("RMSE: " + str(netflix_rmse(prediction_list, actual_ratings_list)))


#when movie id is read in
#need to check it's data
#i.e. year it was made
#average rating for it
#when user id is read in
#need to check it's data
#user's average rating overall
#user's average for a decade
#user's average rating for a year

"""
need to open movie file when movie name is read in
then go through customer ids and predict value
put all predicted values into list
put corresponding
"""
