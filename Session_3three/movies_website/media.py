# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    # This class provides a way to store movie related information

    def __init__(self, movie_name, movie_intro, movie_img, movie_video):
        # initialize instance of class Movie
        self.movie_name=movie_name
        self.movie_intro=movie_intro
        self.movie_img=movie_img
        self.movie_video=movie_video


