#!/usr/bin/env python
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

class DataHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Test")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test", DataHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
