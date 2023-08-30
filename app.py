from flask import Flask
from event_controller import event_bp

app = Flask(__name__)

app.register_blueprint(event_bp, url_prefix='/events')

if __name__ == "__main__":
    app.run(debug=True)
