from flask import Flask
from flask_cors import CORS
from api.auth import auth_bp
from api.pulse import tasks_bp
from api.rooms.housepricepredictor import house_model_bp
from api.rooms.courtroomai import courtroom_bp
from api.rooms.edaexplorer import eda_bp

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

app.register_blueprint(auth_bp, url_prefix = "/syncmind/api/auth")
app.register_blueprint(tasks_bp, url_prefix =  "/syncmind/api/pulse")
app.register_blueprint(house_model_bp, url_prefix="/syncmind/api/rooms/model")
app.register_blueprint(courtroom_bp, url_prefix="/syncmind/api/rooms")
app.register_blueprint(eda_bp, url_prefix="/syncmind/api/rooms")



@app.route("/")
def index():
    return {"message": "Welcome to SyncMind backend!"}

if __name__ == "__main__":
    app.run(debug=True)
