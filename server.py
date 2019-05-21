import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.render('index.html')


def makeApp():
    return tornado.web.Application([
        (r'/', MainHandler)
    ])


if __name__ == '__main__':
    app = makeApp()
    app.listen(3000)
    tornado.ioloop.IOLoop.current().start()
