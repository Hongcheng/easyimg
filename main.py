import os
import tornado.ioloop
import tornado.web
import tornado.httpclient
from util import APIBaseHandler
import first.view
import json

class MainHandler(APIBaseHandler):
	# @tornado.web.authenticated
	def get(self):
		self.write("main.html")
	
settings = {
	"debug":True,
	"static_path":os.path.join(os.path.dirname(__file__),"static"),
	"template_path":os.path.join(os.path.dirname(__file__),"templates"),
	"cookie_secret":"61oETzKXQAGaYdkL5gEmGeJJFuYh7EQnp2XdTP1o/Vo=",
	"login_url":"/login",
	# "xsrf_cookies":True,
}

application = tornado.web.Application([
	(r"/",MainHandler),
	(r"/first",first.view.APIFirstHandler),
	(r"/first/nextgroup",first.view.APIFirstNextGroup),
	(r"/first/result",first.view.APIFirstResult),
	(r"/first/groupnum",first.view.APIFirstGroupNum),
],**settings)

if __name__ == "__main__":
	application.listen(8888)
	tornado.ioloop.IOLoop.instance().start()
