import webapp2
from google.appengine.ext import ndb

# Step 1: Define Picture Class to store links of pictures
class Picture(ndb.Model):
    link = ndb.StringProperty()
    comment = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)

# Further documentation to find out what other types of properties we can make:
# https://cloud.google.com/appengine/docs/python/ndb/properties

# DEBUG: Step 2: Populate our Datastore for Testing

# pic1 = Picture(link='http://img.bleacherreport.net/img/images/photos/003/357/607/hi-res-216c4eca516bb24626745dc1e9d0f5ab_crop_north.jpg?w=630&h=420&q=75',
#               comment='Love this drawing! Go Golden State!')

# pic2 = Picture(link='http://img.bleacherreport.net/img/images/photos/003/358/305/hi-res-3d12fb6698c432801d1b399ebe3d258f_crop_north.jpg?w=630&h=420&q=75',
#               comment='LeBron going to take it all they way!')

# pic1.put()
# pic2.put()
# Need to wait a little bit for local Datastore to update.
# import time
# time.sleep(.1)

# Our html template
HTML = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>NBA Pictures!</title>
    <style>
        input[type='text'] {
          width: 412px;
        }
        th {
          color: teal;
        }
        td {
          border: 1px solid black;
        }
        img {
          width: 450px
        }
        label {
          font-weight: bold;
        }
        .error {
          color: red;
        }
    </style>
</head>
<body>
    <h1>Hello NBA fans! Go ahead and submit a picture link and comment on the picture!</h1>
    <!-- Insert table of pictures here -->
    %s
    <br>
    <span class="error">%s</span>
    <form method="post" action="/">
        <label>Link</label><br><input type="text" name="link"><br>
        <label>Comment</label><br><textarea name="comment" rows=10 cols=66></textarea><br>
        <input type="submit">
    </form>
</body>
</html>'''

# --------------------------Handler Classes--------------------------------------

class MainPage(webapp2.RequestHandler):
    def get(self):

        # Check for error message
        error = self.request.get('error','')
        # print '#####'
        # print error
        # print '#####'

        # Query the Datastore and order earliest date first
        query = Picture.query().order(Picture.date)

        # Test to see print out the list of picture objects
        # pictures_list = query.fetch(5)

        # print '#####'
        # print len(pictures_list)
        # print pictures_list[0]
        # print '#####'

        # Test to print out all the picture objects
        # print '#####'
        # for picture in query:
        #   print picture
        # print '#####'

        # Step 3: Write information from the Datastore and build the HTML table
        table = '<table>\n<tr><th>Link</th><th>Comment</th></tr>\n'
        for picture in query:
            link = picture.link
            comment = picture.comment

            row = '<tr>\n'
            row += '<td><img src="' + link + '" alt="picture"></td>\n'
            row += '<td>' + comment + '</td>\n'
            row += '</tr>\n'

            table += row
        table += '</table>\n'

        rendered_html = HTML % (table,error)

        self.response.out.write(rendered_html)

    def post(self):
        link = self.request.get('link')
        comment = self.request.get('comment')

        # Test to see link and comment
        # print '#####'
        # print link, comment
        # print '#####'

        # Step 4: Allow ability to create picture objects and save to Datastore

        if link and comment:
            picture = Picture(link=link, comment=comment)
            picture.put()
            # DEBUG: For local development. Need to wait a little bit for the 
            # local 
            # Datastore to update
            import time
            time.sleep(.1)
            self.redirect('/')
        else:
            self.redirect('/?error=Please fill out the link and comment sections!')


router = [('/',MainPage)]

app = webapp2.WSGIApplication(router,debug=True)