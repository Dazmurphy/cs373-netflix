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


if os.path.isfile('/u/downing/public_html/netflix-caches/kdg445_true_ratings.pickle') :
    f = open('/u/downing/public_html/netflix-caches/kdg445_true_ratings.pickle','rb')
    true_ratings = pickle.load(f)
else:
    bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kdg445_true_ratings.pickle').content
    true_ratings = pickle.loads(bytes)

if os.path.isfile('/u/downing/public_html/netflix-caches/kh549-customer_average.pickle') :
    f = open('/u/downing/public_html/netflix-caches/kh549-customer_average.pickle','rb')
    customer_av_unpickled = pickle.load(f)
else:
    bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/kh549-customer_average.pickle').content
    customer_av_unpickled = pickle.loads(bytes)

if os.path.isfile('/u/downing/public_html/netflix-caches/ad35988-movie_stddev_average.pickle') :
    f = open('/u/downing/public_html/netflix-caches/ad35988-movie_stddev_average.pickle','rb')
    movie_std_avg = pickle.load(f)
else:
    bytes = requests.get('http://www.cs.utexas.edu/users/downing/netflix-caches/ad35988-movie_stddev_average.pickle').content
    movie_std_avg = pickle.loads(bytes)


#--------
#netflix_eval
#--------

def netflix_eval(i, j) :
    """
    i movie id
    j customer id

    output predicted rating

    """

    assert i > 0 and i <= 17770
    assert j > 0 and j <= 2649429

    std_offset = movie_std_avg[i]

    rating = (customer_av_unpickled[j] + std_offset)

    if (rating > 5) :
        rating = 5

    if (rating < 1) :
        rating = 1

    assert rating > 0 and rating <= 5

    return rating 

def netflix_read(s) :
    return int(s)

def netflix_print(w, v) :
    w.write(str(v) + "\n")

def netflix_solve(r, w) :
    """
    r a reader
    w a writer

    output predicted ratings and rmse

    """

    def netflix_rmse(a, p) :
        """
        a is list of predicted ratings
        p is list of actual ratings

        output rmse
        
        """

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

            assert predicted_rating >= 1
            assert predicted_rating <= 5

            prediction_list.append(predicted_rating)
            actual_ratings_list.append(true_ratings[movie_id][customer_id])

            predicted_rating_truncated = '{:.1f}'.format(predicted_rating)

            netflix_print(w, predicted_rating_truncated)

    rmse = netflix_rmse(prediction_list, actual_ratings_list)

    rmse ='{:.2f}'.format(rmse)

    w.write("RMSE: " + str(rmse))



