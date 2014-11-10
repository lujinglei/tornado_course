import tornado,os
import tornado.options
from  tornado.web import Application,RequestHandler
from tornado.httpserver import HTTPServer
from   tornado.options import options,define
from wtforms import Form,StringField,PasswordField

tornado.options.define("port",default=8888,help="run on the given port",type=int)
tornado.options.define("debug",default=False,help="run in debug mode")

class Main_Handlers(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",name='Jalen')
class LoginForm(Form):
    username = StringField('Username')
    password = PasswordField('Password')

class Application(tornado.web.Application):
    def __init__(self):
        handlers =[
            (r"/",Main_Handlers)
        ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static"),
            debug=True,
        )
        tornado.web.Application.__init__( self ,handlers ,**settings)

def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()


