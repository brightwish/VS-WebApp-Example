import falcon

# In Falcon, define a class for each resource and define on_* methods
# where * is any standard HTTP methods in lowercase, such as on_get.

class HelloResource:
    # In this application, the single HelloResource responds to only GET
    # requests, so it has only an on_get method.

    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200  # 200 is the default
        resp.body = "Hello, Python!"

# Resources are represented by long-lived class instances
hello = HelloResource()

# Instruct Falcon to route / and /hello to HelloResource. If you add
# other resources, use api.add_route to define the desired
# resource locators for them.
api = falcon.API()
api.add_route('/', hello)
api.add_route('/hello', hello)

if __name__ == "__main__":
    # Use Python's built-in WSGI reference implementation to run
    # a web server for the application.
    from wsgiref.simple_server import make_server

    # Run the web server on localhost:8080
    print("Starting web app server")
    srv = make_server('localhost', 8080, api)
    srv.serve_forever()
