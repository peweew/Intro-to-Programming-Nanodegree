# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys", "img/toy_story.jpg",
                        "https://youtu.be/5PSNL1qE6VY")         #toy_story instance


avatar = media.Movie("Avatar", "A marine on an alien planet", "img/avatar.jpg",
                     "https://youtu.be/5PSNL1qE6VY")            #avatar instance


school_rock = media.Movie("Schol of Rock",
                        "Overly enthusiastic guitarist Dewey Finn (Jack Black) gets thrown out of his bar band and finds himself in desperate need of work.",
                        "img/school_rock.jpg",
                        "https://www.youtube.com/watch?v=oP7kExN8LFA")
                              # school rock instance


edge_tomorrow =  media.Movie("Edge of tomorrow",
                             "When Earth falls under attack from invincible aliens, no military unit in the world is able to beat them.",
                             "img/edge_tomorrow.jpg",
                             "https://www.youtube.com/watch?v=yUmSVcttXnI")#  edge of tomorrow instance


interstellar = media.Movie("Interstellar", "In Earth's future, a global crop blight and second Dust Bowl are slowly rendering the planet uninhabitable. ",
                           "img/interstellar.png",
                           "https://www.youtube.com/watch?v=lZMzf-SDWP8") #intersteller instance


tomb_raider = media.Movie("Rise of tomb raider", "Set one year after Tomb Raider, Lara Croft's experience of the supernatural on Yamatai has been covered up by an organization known as Trinity, a sinister private enterprise pursuing the supernatural.",
                          "img/lara.jpg", "https://www.youtube.com/watch?v=Nd6evo2X5fw")   #tomb raider instance
 

movies = [toy_story, avatar, school_rock, edge_tomorrow, interstellar, tomb_raider]                                          # create movie array


fresh_tomatoes.open_movies_page(movies)                   #  movie website
