#!/usr/bin/env python3

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# --------
# imports
# --------

from io import StringIO
from unittest import main, TestCase

from Netflix import netflix_read, netflix_eval, netflix_print, netflix_solve

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase) :
	
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s = "3"
        movies = netflix_read(s)
        self.assertEqual(movies, 3)

    def test_read_2 (self) :
        s = "1001"
        movies = netflix_read(s)
        self.assertEqual(movies, 1001)

    def test_read_3 (self) :
        s = "8209"
        movies = netflix_read(s)
        self.assertEqual(movies, 8209)
   
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = netflix_eval(8209, 2000622)
        self.assertEqual(v, 4.279008432960954)

    def test_eval_2 (self) :
        v = netflix_eval(8038, 147141)
        self.assertEqual(v, 4.718157156289632)

    def test_eval_3 (self) :
        v = netflix_eval(16262, 91166)
        self.assertEqual(v, 2.389508247681013)

    def test_eval_4 (self) :
        v = netflix_eval(12127, 559906)
        self.assertEqual(v, 2.6017255309394556)

    # -----
    # print
    # -----

    def test_print_1 (self)	:
    	w = StringIO()
    	netflix_print(w, 4.279008432960954)
    	self.assertEqual(w.getvalue(), "4.279008432960954\n")
  
    def test_print_2 (self)	:
    	w = StringIO()
    	netflix_print(w, 3.4756)
    	self.assertEqual(w.getvalue(), "3.4756\n")

    def test_print_3 (self) :
    	w = StringIO()
    	netflix_print(w, 2)
    	self.assertEqual(w.getvalue(), "2\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("12126:\n1120091\n21560\n1684241\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "12126:\n4.1\n3.2\n3.9\nRMSE: 1.28")

    def test_solve_2 (self) :
        r = StringIO("4327:\n2604511\n1862650\n1456536\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "4327:\n3.4\n3.0\n3.2\nRMSE: 0.83")

    def test_solve_3 (self) :
        r = StringIO("430:\n2573892\n1843756\n2540558\n68149\n2143918\n164344\n")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "430:\n4.9\n3.7\n4.4\n4.1\n3.1\n3.7\nRMSE: 2.08")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

