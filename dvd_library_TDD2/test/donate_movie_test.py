import unittest

import os, sys
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))

from movie import Movie
from library import Library


class DonateMovieTest(unittest.TestCase):
    def setUp(self):
        self.movie = Movie()
        self.library = Library()
        self.library.donate(self.movie)

    def test_movie_add_to_library(self):
        self.assertTrue(self.library.contains(self.movie))

    def test_copy_added(self):
        self.assertEqual(1, self.movie.get_copies())



if __name__ == '__main__':
    unittest.main()
