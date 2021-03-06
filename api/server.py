import json
import falcon

from modules.body import Body
from modules.withings import Withings as w_client
from modules.fitbit import Fitbit as f_client


class AppResource(object):
    def on_get(self, req, resp):

        print("hi")

        msg = {"message": "hello world"}
        resp.body = json.dumps(msg)

    def on_post(self, req, resp):
        withings = w_client()
        body: Body = withings.fetch_last_body()
        if body.timestamp is None:
            resp.body = json.dumps({"status": "noghing"})
            return

        fitbit = f_client()
        fitbit.register(body)

        resp.body = json.dumps({"status": "tranfsered"})


class Withings(object):
    def on_get(self, req, resp):
        client = w_client()
        body = client.fetch_last_body()

        if body.timestamp is None:
            resp.body = json.dumps({"status": "nodata"})
            return

        resp.body = json.dumps(
            {
                "weight": float(body.weight),
                "fat": float(body.fat),
                "registered_at": body.timestamp.strftime("%Y-%m-%d %H:%M:%S"),
            }
        )


class Fitbit(object):
    def on_get(self, req, resp):
        client = f_client()
        resp.body = json.dumps(client.get_fat())


app = falcon.API()
app.add_route("/", AppResource())
app.add_route("/withings", Withings())
app.add_route("/fitbit", Fitbit())

if __name__ == "__main__":
    from wsgiref import simple_server

    httpd = simple_server.make_server("0.0.0.0", 8080, app)
    httpd.serve_forever()
