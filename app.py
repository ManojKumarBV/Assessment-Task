import os
import sys
from flask import Flask
import views
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)
app.add_url_rule("/", view_func=views.root, methods=['GET'])
app.add_url_rule("/read_ocr", view_func=views.read_ocr, methods=['POST'])
print("Server Ready", flush=True)

SWAGGER_URL ='/swagger'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app-name' : "Image-Reader"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4000, debug=True)
