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


true_ratings_url = 'http://www.cs.utexas.edu/users/downing/netflix-caches/kdg445_true_ratings.pickle'

f = requests.get(true_ratings_url).content
true_ratings = pickle.loads(f)

customer_av_unpickled_url = 'http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-customer_average.pickle'

g = requests.get(customer_av_unpickled_url).content
customer_av_unpickled = pickle.loads(g)

movie_std_avg_url = 'http://www.cs.utexas.edu/users/downing/netflix-caches/ad35988-movie_stddev_average.pickle'

h = requests.get(movie_std_avg_url).content
movie_std_avg = pickle.loads(h)


#--------
#netflix_eval
#--------

def netflix_eval(i, j) :

    std_offset = movie_std_avg[i]

    return (customer_av_unpickled[j] + std_offset)

def netflix_read(s) :
    return int(s)

def netflix_print(w, v) :
    w.write(str(v) + "\n")

def netflix_solve(r, w) :
    """
    r a reader
    w a writer
    """

    def netflix_rmse(a, p) :
        return sqrt(mean(square(subtract(a, p))))

    prediction_list = []
    actual_ratings_list = []

    customer_id = 0
    movie_id = 0

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

            predicted_rating = netflix_eval(movie_id, customer_id)

            prediction_list.append(predicted_rating)
            actual_ratings_list.append(true_ratings[movie_id][customer_id])

            predicted_rating_truncated = '{:.1f}'.format(predicted_rating)

            netflix_print(w, predicted_rating_truncated)

    rmse = netflix_rmse(prediction_list, actual_ratings_list)

    rmse ='{:.2f}'.format(rmse)

    w.write("RMSE: " + str(rmse))



