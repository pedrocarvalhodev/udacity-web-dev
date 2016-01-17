import webapp2

main_html = """
  <html>
  	<head>
  	    <title>Greetings Page</title>
  	  </head>
  	  <body>
  	     <p>Hello Google App Engine World: Pedro ama Cibele</p>
         <form method="post">
         <br />
         "What is your name?
          <input type = "text" name = "user" maxlength = "12"
         <br />
  	  </form>
      </body>
  	  </html>
  	  """

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(main_html)
        
    def post(self):
        username = self.request.get("user")[0:11]
        self.response.write("Greetings from your computer <strong>" + username + "  <strong>")
        
app = webapp2.WSGIApplication([('/', MainPage)], debug = True)