
# Lession 4.7: Introducing Templates

# We introduce templates to build complicated strings using the Jinja2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-686598825

import os

import jinja2
import webapp2
import time
from google.appengine.ext import ndb 

#set User database to store the user information of club

class User(ndb.Model):
    name=ndb.StringProperty()
    age=ndb.StringProperty()
    occupation=ndb.StringProperty()
    image=ndb.StringProperty()
    self_intro=ndb.TextProperty()

#set photo database to store the photo information
class Photo(ndb.Model):
    link=ndb.StringProperty()

#check whether user's name is a registered user name.
def user_check(name):
    users=User.query()
    for user in users:
        if user.name==name:
            return True
    return False

# Set up jinja environment

template_dir = os.path.dirname(__file__)

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)


#Render Handler

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t=jinja_env.get_template(template)
        return t.render(params)

    def render(self,template, **kw):
        self.write(self.render_str(template, **kw))


#index.html page handler
class MainPage(Handler):
    def get(self):
        #items = self.request.get_all("food")
        self.render("index.html")



#Members.html page handler
class MembersHandler(Handler):
    def get(self):
        users=User.query()
        self.render("members.html",user_list=users)


class RegistrationHandler(Handler):
    def get(self):
        e=self.request.get("error")
        self.render("registration.html",error=e)
    def post(self):
        name=self.request.get("name")      #get user's input: name, age, occupation, image (in form of link), and introduction
        age=self.request.get("age")
        occupation=self.request.get("occupation")
        image=self.request.get("image")
        self_intro=self.request.get("self_intro")

        if name and not (name.isspace()) and (0<= int(age)) and (int(age)<=150) and occupation and not (occupation.isspace()) and self_intro and not (self_intro.isspace()) and image and not (image.isspace()):  #check input validity
            user=User(name=name,age=age,occupation=occupation,self_intro=self_intro,image=image)
            user.put()                     # if user's input is valid, save it in User database
            delay = 0.1                    # set delay time to allow the pages update
            time.sleep(delay)
            self.redirect("/members.html") # redirect to members.html and show all the current user information
        else:                              # if user's input is not valid, show the error message.
            self.redirect("/registration.html?error=Please input the correct user information!")


#photo.html handler
class PhotoHandler(Handler):
    def get(self): 
        images = Photo.query()
        self.render("photo.html",images = images)

#photo submission handler

class PhotosubmitHandler(Handler):
    def get(self):
        e = self.request.get("error")
        self.render("photosubmit.html",error = e)
    def post(self):
        link = self.request.get("photo_link")     # get the photo link
        user_name = self.request.get("user_name") # get user's name
        if user_check(user_name):                 # check if user is a registrated user. If yes, show the user's uploaded photo.
            photo = Photo(link=link)
            photo.put()
            delay = 0.1                           # set delay time to allow the pages update
            time.sleep(delay)
            self.redirect("/photo.html")
        else:                                     # If user has not registrated, output error message
            self.redirect("/photosubmit.html?error=You do not have right to upload photo because you do not hold club membership!")
        


#about.html handler
class AboutHandler(Handler):
    def get(self):
        self.render("about.html")

#note.html handler
class NoteHandler(Handler):
    def get(self):
        self.render("note.html")


#set the router
router=[("/", MainPage),
     ("/index.html", MainPage),
     ("/members.html",MembersHandler),
     ("/registration.html",RegistrationHandler),
     ("/photo.html",PhotoHandler),
     ("/photosubmit.html",PhotosubmitHandler),
     ("/about.html",AboutHandler),
     ("/note.html",NoteHandler)
     ]

#webapp2 run
app = webapp2.WSGIApplication(router,debug=True)
