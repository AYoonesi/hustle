import web

urls = (
    '/', 'index',
    '/(.*)/', 'redirect',
    '/health', 'health'
)

class index:
    def GET(self):
        return 'Hello World!'

class redirect:
    def GET(self, path):
        web.seeother('/' + path)  # Redirect to the new path

class health:
    def GET(self):
        return "HAPPY"

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
