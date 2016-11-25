# -*- coding:utf-8 -*-
import os
import traceback

from tornado import web
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.options import parse_command_line

from handle import BaseHandler, event


class MainHandler(BaseHandler):
    def initialize(self, **kwargs):
        print kwargs

        BaseHandler.initialize(self)

    def on_get(self, *args, **kwargs):
        self.write("ok1111")
        self.finish()

    @event
    def click(self):
        print self.request.arguments
        self.write(self.request.arguments)


class Application(web.Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/todos.?(?P<event_name>.*)", MainHandler, dict(hello=1)),
        ]

        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            xsrf_cookies=False,
            cookie_secret="__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__",
            # login_url="/auth/login",
            debug=True,
        )
        super(Application, self).__init__(handlers, **settings)


if __name__ == "__main__":
    parse_command_line()

    app = Application()
    # wsgi_app = wsgi.WSGIAdapter(app)

    loop = IOLoop.instance()

    print "http://{}:{}".format("localhost", 6751)

    HTTPServer(app).listen(6751)
    try:
        # server = gevent.wsgi.WSGIServer(('', 8888), wsgi_app, debug=True)
        # server.serve_forever()
        # loop.add_callback(webbrowser.open, url)
        loop.start()
    except KeyboardInterrupt:
        print(" Shutting down on SIGINT!")
        loop.stop()
        traceback.format_exc()
    finally:
        pass

        # loop.close()
        # IOLoop.current().start()
        # IOLoop.current().start()

if __name__ == '__main__':
    '''
    curl http://localhost:6751/
    curl http://localhost:6751/todos.click?hello=22222&hello=3333
    '''
