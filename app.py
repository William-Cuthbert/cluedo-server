from flask import Flask
from routes import cluedo_routes

app = Flask(__name__)
app.register_blueprint(cluedo_routes)

if __name__ == '__main__':
    app.run(debug=True)
