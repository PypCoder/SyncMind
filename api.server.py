from flask import Flask, jsonify, request
from pandas_handler import get_random_task

app = Flask(__name__)

@app.route("/suggest", methods=["GET"])
def suggest_task():
    mode = request.args.get("mode", "Do")
    task = get_random_task(mode)
    if task:
        return jsonify({
            "title": task["title"],
            "description": task["description"]
        })
    else:
        return jsonify({"message": "No pending tasks found."}), 404

if __name__ == "__main__":
    app.run(debug=True)
