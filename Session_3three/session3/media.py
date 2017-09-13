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
        self.title=movie_name
        self.storyline=movie_intro
        self.poster_image_url=movie_img
        self.trailer_youtube_url=movie_video


