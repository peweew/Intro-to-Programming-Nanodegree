# Lession 4.7: Introducing Templates

# We introduce templates to build complicated strings using the Jinja2 library.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4186408748/m-686598825

import os

import jinja2
import webapp2
import time
from google.appengine.ext import ndb 

#set user class to store the user information of club

class User(ndb.Model):
    name=ndb.StringProperty()
    age=ndb.StringProperty()
    occupation=ndb.StringProperty()
    image=ndb.StringProperty()
    self_intro=ndb.TextProperty()



# Set up jinja environment

template_dir = os.path.dirname(__file__)

# Instructor Notes:
# Suggest to print out template_dir to see how the file path is being constructured.
# You can find the print out in the Logs in Google App Engine (GAE). For Windows and Mac users,
# you need to click on the "Logs" button to be able to see the print messages

# print "###" # These hash marks helps us locate our print statement from the rest of the messages
              # Google App Engine gives us
# print template_dir
# print "###"

# For Windows Users, you need to add in a logging flag for GAE to print out your
# statements appropriately. Please go here to download the "Google App Engine Troubleshooting"
# guide to learn how to add in the logging flag:
# https://www.udacity.com/course/viewer#!/c-nd000/l-4166899177/m-3974308850

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)



class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t=jinja_env.get_template(template)
        return t.render(params)

    def render(self,template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    def get(self):
        #items = self.request.get_all("food")
        self.render("index.html")


class FizzBuzzHandler(Handler):
    def get(self):
        n=self.request.get("n",0)
        n= int(n)
        self.render("fizzbuzz.html",n=n)

class MembersHandler(Handler):
    def get(self):
        users=User.query()
        ndb.delete(users)
        self.render("members.html",user_list=users)

class RegistrationHandler(Handler):
    def get(self):
        e=self.request.get("error")
        self.render("registration.html",error=e)
    def post(self):
        name=self.request.get("name")
        age=self.request.get("age")
        occupation=self.request.get("occupation")
        image=self.request.get("image")
        self_intro=self.request.get("self_intro")

        if name and age and occupation and self_intro and image: 
            user=User(name=name,age=age,occupation=occupation,self_intro=self_intro,image=image)
            user.put()
            time.sleep(0.1)
            self.redirect("/members.html") 
        else:
            self.redirect("/registration.html?error=Please input the correct user information!")


class PhotoHandler(Handler):
    def get(self):
        #items = self.request.get_all("food")
        self.render("photo.html")

class AboutHandler(Handler):
    def get(self):
        #items = self.request.get_all("food")
        self.render("about.html")

router=[("/", MainPage),("/index.html", MainPage),("/members.html",MembersHandler),("/registration.html",RegistrationHandler),("/photo.html",PhotoHandler),("/about.html",AboutHandler),]

app = webapp2.WSGIApplication(router,debug=True)
