import json
import falcon


class AppResource(object):

    def on_get(self, req, resp):

        print("hi")

        msg = {
            "message": "hello world"
        }
        resp.body = json.dumps(msg)


app = falcon.API()
app.add_route("/", AppResource())

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("0.0.0.0", 8080, app)
    httpd.serve_forever()
