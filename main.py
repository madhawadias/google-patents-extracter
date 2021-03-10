import gc
import os

from app import app
from routes.patent_search_route import patent_search_endpoint
from routes.patent_search_route import patent_search_send_endpoint

gc.enable()
app.register_blueprint(patent_search_endpoint)
app.register_blueprint(patent_search_send_endpoint)


@app.route("/check", methods=["GET"])
def check():
    return "200"


if __name__ == "__main__":
    app.secret_key = os.urandom(24)
    print("Running")
    gc.enable()
    app.run(host="0.0.0.0", port=5000)