import os
import webapp2
import jinja2
from google.appengine.ext import db

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
		print("loading sound_test.html")
		template= JINJA_ENVIRONMENT.get_template('sound_test.html')
		self.response.write(template.render())
		#self.response.headers['Content-Type'] = 'text/plain'
        #self.response.write('Hello, World!')

#class MidiFile(webapp2.RequestHandler):
#	def get(self):
#		return 

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
